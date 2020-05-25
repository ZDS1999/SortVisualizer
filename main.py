from form import Ui_Widget
from algorithm import Sorter
from globals import *
from PySide2 import QtCore, QtWidgets, QtGui
import sys
import random


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # class variables
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene_height = self.ui.graphicsView.height()
        self.scene_width = self.ui.graphicsView.width()
        self.col_amount = 0
        self.col_heights = []
        self.col_items = []
        # (-1) - App started    (0) - App ready to sort
        # (1)  - App sorting    (2) - App sorted
        self.app_state = 0  # here should be changed !!!!
        self.comparisons = 0
        self.sort_delay = 0
        self.algorithm_key = 0
        self.sorter = Sorter(self.algorithm_key, self.sort_delay, self.col_amount, self.col_heights)

        # view settings
        self.setFixedSize(self.width(), self.height())
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.horizontalScrollBar().blockSignals(True) # avoid scrolling
        self.ui.graphicsView.verticalScrollBar().blockSignals(True)
        self.columns_setup(1, 50)

        # signal connect
        self.ui.btnSort.clicked.connect(self.btnSort_clicked)
        self.ui.spinDelay.valueChanged.connect(self.spin_changed)
        self.ui.spinColAmount.valueChanged.connect(self.spin_changed)

        # show widget
        self.show()

    def columns_setup(self, ms, amount):
        # reset columns
        self.scene.clear()
        self.col_heights.clear()
        self.col_items.clear()

        # copy delay, amount to class attribute
        self.sort_delay = ms
        self.col_amount = amount

        # compute width of all columns
        col_width = self.scene_width / amount

        # create heights for all columns in scene
        height_increment = self.scene_height / amount
        height = 0
        for i in range(amount):
            height += height_increment
            self.col_heights.append(height)

        dprint('column number: {}'.format(len(self.col_heights)))

        # shuffle heights
        random.shuffle(self.col_heights)

        # apply columns to scene
        xpos = 0
        for i in range(amount):
            ypos = self.scene_height - self.col_heights[i]
            rect_item = QtWidgets.QGraphicsRectItem()
            # column location in scene
            rect_item.setRect(xpos, ypos, col_width, self.col_heights[i])
            # column background color
            rect_item.setBrush(QtGui.QBrush(QtGui.Qt.red))
            # column border width
            if amount <= 200:
                rect_item.setPen(QtGui.QPen(QtGui.Qt.black, 2))
            elif 200 < amount <= 300:
                rect_item.setPen(QtGui.QPen(QtGui.Qt.black, 1))
            else:
                rect_item.setPen(QtGui.Qt.NoPen)
            # add item to scene
            self.scene.addItem(rect_item)
            self.col_items.append(rect_item)
            # update xpos
            xpos += col_width

        self.thread_update(ms, self.algorithm_key)

    def thread_update(self, ms, sort_with):
        self.sorter = Sorter(sort_with, ms, self.col_amount, self.col_heights)
        self.sorter.signals.sig_compare.connect(self.on_comparsion)
        self.sorter.signals.sig_sort_done.connect(self.sort_done)
        self.sorter.signals.sig_change_button_status.connect(self.sort_button_status)
        self.sorter.signals.sig_array_access.connect(self.ui.labArrayAccesses.setNum)

    def sort_button_status(self, state):
        style = ''
        btn_text = ''
        if self.app_state == 0:
            self.ui.spinColAmounts.setEnabled(False)
            self.ui.spinDelay.setEnabled(False)
            btn_text = 'sort'
            style = 'background-color: rgba(255,0,68,255); color: #fff'
        elif self.app_state == 1:
            self.ui.spinColAmounts.setEnabled(True)
            self.ui.spinDelay.setEnabled(True)
            btn_text = 'cancel'
            style = 'background-color: #000; color: #fff'
        elif self.app_state == 2:
            btn_text = 'new sort'
            style = 'background-color: rgba(85,0,255,255); color: #fff'
        self.app_state = state
        self.ui.btnSort.setText(btn_text)
        self.ui.btnSort.setStyleSheet(style)

    @QtCore.Slot()
    def spin_changed(self):
        if self.app_state == 0:
            ms = self.ui.spinDelay.value()
            amount = self.ui.spinColAmounts.value()
            self.columns_setup(ms, amount)

    @QtCore.Slot()
    def btnSort_clicked(self):
        if self.app_state == 0:
            dprint('app state transits from 0 to 1')
            self.sort_button_status(1)
            self.comparisons = 0
            self.thread_update(self.sort_delay, self.algorithm_key)
            self.sorter.start()
        elif self.app_state == 1:
            dprint('app state transits from 1 to 2')
            self.sorter.terminate()
            self.sort_button_status(2)
        elif self.app_state == 2:
            dprint('app state transits from 2 to 0')
            self.scene.clear()
            self.col_heights.clear()
            self.columns_setup(self.sort_delay, self.col_amount)
            self.sort_button_status(0)
        else:
            print('app state not found')
            sys.exit(1)

    @QtCore.Slot()
    def on_comparsion(self, left, right):
        left_rect = self.col_items[left].rect()
        right_rect = self.col_items[right].rect()
        left_xpos = left_rect.left()
        right_xpos = right_rect.left()

        left_rect.moveLeft(right_xpos)
        right_rect.moveLeft(left_xpos)

        self.col_items[left].setRect(left_rect)
        self.col_items[right].setRect(right_rect)

        self.col_items[left], self.col_items[right] = self.col_items[right], self.col_items[left]
        self.comparisons += 1
        self.ui.labComparisons.setNum(self.comparisons)

    @QtCore.Slot()
    def sort_done(self, n):
        self.col_items[n].setBrush(QtGui.QBrush(QtGui.QColor(0, 200, 0)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())
