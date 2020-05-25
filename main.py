from form import Ui_Widget
from algorithm import Sorter
from globals import dprint
import globals
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
        self.col_heights = []
        self.col_items = []
        self.algorithm_list = {}
        # (-1) - App started    (0) - App ready to sort
        # (1)  - App sorting    (2) - App sorted
        self.app_state = -1
        self.comparisons = 0
        self.col_amount = 100
        self.sort_delay = 0
        self.algorithm_key = 0
        self.sorter = Sorter(self.algorithm_key, self.sort_delay, self.col_amount, self.col_heights)

        # view settings
        self.setFixedSize(self.width(), self.height())
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.horizontalScrollBar().blockSignals(True) # avoid scrolling
        self.ui.graphicsView.verticalScrollBar().blockSignals(True)
        self.columns_setup()
        for i in range(self.ui.listAlgorithms.count()):
            item = self.ui.listAlgorithms.item(i)
            item.setSizeHint(QtCore.QSize(item.sizeHint().width(), 40))
            self.algorithm_list[item.text()] = i

        # signal connect
        self.ui.btnSort.clicked.connect(self.btnSort_clicked)
        self.ui.spinDelay.valueChanged.connect(self.spinDelay_changed)
        self.ui.spinColAmount.valueChanged.connect(self.spinAmount_changed)
        self.ui.listAlgorithms.itemClicked.connect(self.list_clicked)

        # show widget
        self.show()

    def columns_setup(self):
        # reset label
        self.ui.labArrayAccesses.setText('0')
        self.ui.labComparisons.setText('0')
        self.comparisons = 0
        # reset columns
        self.scene.clear()
        self.col_heights.clear()
        self.col_items.clear()
        # compute width of all columns
        col_width = self.scene_width / self.col_amount
        # create heights for all columns in scene
        height_increment = self.scene_height / self.col_amount
        height = 0
        for i in range(self.col_amount):
            height += height_increment
            self.col_heights.append(height)
        # shuffle heights
        random.shuffle(self.col_heights)
        # apply columns to scene
        xpos = 0
        for i in range(self.col_amount):
            ypos = self.scene_height - self.col_heights[i]
            rect_item = QtWidgets.QGraphicsRectItem()
            # column location in scene
            rect_item.setRect(xpos, ypos, col_width, self.col_heights[i])
            # column background color
            rect_item.setBrush(QtGui.QBrush(QtGui.Qt.red))
            # column border width
            if self.col_amount <= 200:
                rect_item.setPen(QtGui.QPen(QtGui.Qt.black, 2))
            elif 200 < self.col_amount <= 300:
                rect_item.setPen(QtGui.QPen(QtGui.Qt.black, 1))
            else:
                rect_item.setPen(QtGui.Qt.NoPen)
            # add item to scene
            self.scene.addItem(rect_item)
            self.col_items.append(rect_item)
            # update xpos
            xpos += col_width

    def thread_update(self):
        self.sorter = Sorter(self.algorithm_key, self.sort_delay, self.col_amount, self.col_heights)
        self.sorter.access_count = 0
        self.sorter.signals.sig_compare.connect(self.on_comparsion)
        self.sorter.signals.sig_sort_done.connect(self.sort_done)
        self.sorter.signals.sig_change_button_status.connect(self.sort_button_status)
        self.sorter.signals.sig_array_access.connect(self.ui.labArrayAccesses.setNum)

    def sort_button_status(self, state):
        dprint('FUNCTION: sort_button_status')
        dprint('\tstate = {}'.format(self.app_state))
        style = ''
        btn_text = ''
        if state == 0:
            self.ui.spinColAmount.setEnabled(True)
            self.ui.spinDelay.setEnabled(True)
            btn_text = 'sort'
            style = 'background-color: rgba(255,0,68,255); color: #fff'
        elif state == 1:
            self.ui.spinColAmount.setEnabled(False)
            self.ui.spinDelay.setEnabled(False)
            btn_text = 'cancel'
            style = 'background-color: #000; color: #fff'
        elif state == 2:
            btn_text = 'new sort'
            style = 'background-color: rgba(85,0,255,255); color: #fff'
        self.app_state = state
        dprint('\tstate → {}'.format(self.app_state))
        self.ui.btnSort.setText(btn_text)
        self.ui.btnSort.setStyleSheet(style)

    @QtCore.Slot()
    def list_clicked(self, item):
        dprint('FUNCTION: list_clicked')
        dprint('\ttext: {}'.format(item.text()))
        dprint('\tapp_state = {}'.format(self.app_state))
        if self.app_state == -1:
            self.ui.btnSort.setEnabled(True)
            self.ui.spinColAmount.setEnabled(True)
            self.ui.spinDelay.setEnabled(True)

            self.app_state = 0
            self.sort_button_status(self.app_state)

        if self.app_state == 0:
            text = item.text()
            algorithm_key = self.algorithm_list[text]
            self.ui.labSortWith.setText(text)

    @QtCore.Slot()
    def spinAmount_changed(self):
        if self.app_state == 0:
            self.col_amount = self.ui.spinColAmount.value()
            self.columns_setup()

    def spinDelay_changed(self):
        if self.app_state == 0:
            self.sort_delay = self.ui.spinDelay.value()
            self.thread_update()


    def btnSort_clicked(self):
        dprint('FUNCTION: btnSort_clicked')
        dprint('FUNCTION: on_btnSort_clicked')
        # ready to start -> running
        if self.app_state == 0:
            dprint('\tapp_state 0 → 1')
            self.sort_button_status(1)
            self.thread_update()
            globals.RET_FLAG = False
            self.sorter.start()
        # running -> finished
        elif self.app_state == 1:
            dprint('\tapp_state 1 → 2')
            globals.RET_FLAG = True
            self.sort_button_status(2)
        # finished -> ready to start
        elif self.app_state == 2:
            dprint('\tapp_state 2 → 0')
            self.scene.clear()
            self.columns_setup()
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
