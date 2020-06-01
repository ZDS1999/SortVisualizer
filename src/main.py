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
            # view control
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene_height = self.ui.graphicsView.height()
        self.scene_width = self.ui.graphicsView.width()
        self.col_heights = []
        self.col_items = []
        self.algorithm_list = {}
        # (-1) - App started    (0) - App ready to sort
        # (1)  - App sorting    (2) - App sorted
        self.app_state = -1
            # sort control
        self.col_amount = 100
        self.sort_delay = 1
        self.algorithm_key = 0
        self.sorter = Sorter(self.algorithm_key, self.sort_delay, self.col_amount, self.col_heights)

        # view settings
        self.setWindowTitle('Sort Visualizer')
        self.setFixedSize(self.width(), self.height())
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.horizontalScrollBar().blockSignals(True) # avoid scrolling
        self.ui.graphicsView.verticalScrollBar().blockSignals(True)
        self.ui.spinDelay.setDisabled(True)
        self.ui.spinColAmount.setDisabled(True)
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
        '''
        only works in three conditions:
            1. starting app
            2. spin amount
            3. state 2 → 0, press btnSort when it's text is new sort
        functions:
            1. reset display labels and their correspoing class variables
            2. reset scene and render it again with correspoing variables
        '''
        # reset label
        self.ui.labTime.setText('0')
        self.ui.labComparisons.setText('0')
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
        '''
        only works when: state 0 → 1, press btnSort when it's content is sort
        function: create a new thread and render it with current state
        '''
        self.sorter = Sorter(self.algorithm_key, self.sort_delay, self.col_amount, self.col_heights)
        # swap columns in scene
        self.sorter.signals.sig_swap.connect(self.swap_columns)
        # adjust certain column height
        self.sorter.signals.sig_adjust.connect(self.adjust_column)
        # show done animation
        self.sorter.signals.sig_sort_done.connect(self.sort_done)
        # change lab comparisons num
        self.sorter.signals.sig_compare.connect(self.ui.labComparisons.setNum)
        # change app_state when finishing
        self.sorter.signals.sig_change_button_status.connect(self.sort_button_status)
        # change lab time when finishing
        self.sorter.signals.sig_time.connect(self.ui.labTime.setNum)

    @QtCore.Slot()
    def list_clicked(self, item):
        dprint('FUNCTION: list_clicked')
        dprint('\ttext: {}'.format(item.text()))
        dprint('\tapp_state = {}'.format(self.app_state))
        # enter ready state when first clicked
        if self.app_state == -1:
            self.ui.btnSort.setEnabled(True)
            self.ui.spinColAmount.setEnabled(True)
            self.ui.spinDelay.setEnabled(True)

            self.app_state = 0
            self.sort_button_status(self.app_state)

        # render labSortWith's text
        if self.app_state == 0:
            text = item.text()
            dprint('\talgorithm {} → {}'.format(self.algorithm_key, self.algorithm_list[text]))
            self.algorithm_key = self.algorithm_list[text]
            self.ui.labSortWith.setText(text)
        # test
        # self.adjust_column(1, self.scene_height)
        # self.swap_columns(1, 2)

    @QtCore.Slot()
    def spinAmount_changed(self):
        '''re render the scene'''
        dprint('FUNCTION: spinAmount_changed')
        if self.app_state == 0:
            dprint('\tamount {} → {}'.format(self.col_amount, self.ui.spinColAmount.value()))
            self.col_amount = self.ui.spinColAmount.value()
            self.columns_setup()

    @QtCore.Slot()
    def spinDelay_changed(self):
        '''re render the sorter(thread)'''
        dprint('FUNCTION: spinDelay_changed')
        if self.app_state == 0:
            dprint('\tdelay {} → {}'.format(self.sort_delay, self.ui.spinDelay.value()))
            self.sort_delay = self.ui.spinDelay.value()

    @QtCore.Slot()
    def sort_button_status(self, state):
        '''
            transit to a new state and set labels and button
        '''
        dprint('FUNCTION: sort_button_status')
        dprint('\tstate {} → {}'.format(self.app_state, state))
        style = ''
        btn_text = ''
        if state == 0:
            self.ui.spinColAmount.setEnabled(True)
            self.ui.spinDelay.setEnabled(True)
            self.ui.listAlgorithms.setEnabled(True)
            btn_text = 'sort'
            style = 'background-color: rgba(255,0,68,255); color: #fff'
        elif state == 1:
            self.ui.spinColAmount.setEnabled(False)
            self.ui.spinDelay.setEnabled(False)
            self.ui.listAlgorithms.setEnabled(False)
            btn_text = 'cancel'
            style = 'background-color: #000; color: #fff'
        elif state == 2:
            btn_text = 'new sort'
            style = 'background-color: rgba(85,0,255,255); color: #fff'
        self.app_state = state
        self.ui.btnSort.setText(btn_text)
        self.ui.btnSort.setStyleSheet(style)

    @QtCore.Slot()
    def btnSort_clicked(self):
        '''
            transit to a new state and control sort process
        states
            -1 → 0 → 1
                  ↖ ↙
                   2

            -1 → 0 choose algorithm
             0 → 1 sort
             1 → 2 cancel
             2 → 0 new sort
        '''
        dprint('FUNCTION: btnSort_clicked')
        # ready to start -> running
        if self.app_state == 0:
            self.sort_button_status(1)
            self.thread_update()
            globals.RET_FLAG = False
            self.sorter.start()
        # running -> finished
        elif self.app_state == 1:
            globals.RET_FLAG = True
            self.sort_button_status(2)
        # finished -> ready to start
        elif self.app_state == 2:
            self.scene.clear()
            self.columns_setup()
            self.sort_button_status(0)
        else:
            print('app state not found')
            sys.exit(1)

    @QtCore.Slot()
    def swap_columns(self, left, right):
        '''change two different columns in the scene'''
        left_rect = self.col_items[left].rect()
        right_rect = self.col_items[right].rect()
        left_xpos = left_rect.left()
        right_xpos = right_rect.left()

        left_rect.moveLeft(right_xpos)
        right_rect.moveLeft(left_xpos)

        self.col_items[left].setRect(left_rect)
        self.col_items[right].setRect(right_rect)

        self.col_items[left], self.col_items[right] = self.col_items[right], self.col_items[left]

    @QtCore.Slot()
    def adjust_column(self, pos, height):
        '''adjust the height of the col_items[pos] to height'''
        rect = self.col_items[pos].rect()
        # only need to adjust height and ypos
        rect.setY(self.scene_height - height)
        rect.setHeight(height)
        self.col_items[pos].setRect(rect)

    @QtCore.Slot()
    def sort_done(self, n):
        self.col_items[n].setBrush(QtGui.QBrush(QtGui.QColor(0, 200, 0)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())
