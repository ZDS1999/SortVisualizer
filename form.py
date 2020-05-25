# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1374, 719)
        Widget.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"	font: 25 11pt \"Roboto Light\";\n"
"	color: rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"#sortButton {\n"
"	border:none;\n"
"	background-color:  rgba(255, 0, 68,100);\n"
"	border-radius: 15%;\n"
"	font: 11pt \"Roboto\";\n"
"	color: #fff;\n"
"}\n"
"\n"
"#amountChanger, #delayChanger {\n"
"  padding-right: 10px;\n"
"	padding-left: 10px;\n"
"	border: 1px solid  rgba(255, 0, 68, 150);\n"
"	border-radius: 3%;\n"
"	background-color: #f5f5f5;\n"
"	font: 11pt \"Roboto\";\n"
"	color: rgb(255, 0, 68);\n"
"}\n"
"\n"
"#amountChanger::up-button:pressed, #amountChanger::down-button:pressed,\n"
"#delayChanger ::up-button:pressed, #delayChanger::down-button:pressed{\n"
" background-color: rgab(220, 0, 58, 255);\n"
"}\n"
"\n"
"#amountChanger::up-button, #amountChanger::down-button,\n"
"#delayChanger::up-button, #delayChanger::down-button {\n"
"  width: 16px;\n"
"  background-color: rgba(255, 0, 68, 150);\n"
"}\n"
"#amountChanger::down-button,\n"
"#delayChanger::down-button  {\n"
"	border-top:"
                        " 1px solid rgba(255, 0, 68, 180);\n"
"}\n"
"\n"
"#amountChanger::down-button:hover, #amountChanger::up-button:hover,\n"
"#delayChanger::down-button:hover, #delayChanger::up-button:hover {\n"
" background-color:rgba(255, 0, 68, 255);\n"
"}\n"
"\n"
"#amountChanger::up-button:disabled,#amountChanger::up-button:off,\n"
"#amountChanger::down-button:disabled,#amountChanger::down-button:off,\n"
"#delayChanger::up-button:disabled,#delayChanger::up-button:off,\n"
"#delayChanger::down-button:disabled,#delayChanger::down-button:off{\n"
"  background-color: rgba(0, 0, 0, 20)\n"
"}\n"
"\n"
"#amountChanger::down-button:disabled,#amountChanger::down-button:off,\n"
"#delayChanger::down-button:disabled,#delayChanger::down-button:off{\n"
"  border-top: 1px solid rgba(0, 0, 0, 20);\n"
"}\n"
"#amountChanger:disabled, #amountChanger:off,\n"
"#delayChanger:disabled, #delayChanger:off{\n"
"  border: 1px solid rgba(0, 0, 0, 20);\n"
"  color:  rgba(0, 0, 0, 50);\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(Widget)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(Widget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QSize(1000, 700))
        self.graphicsView.setStyleSheet(u"\n"
"background-color:rgb(31, 31, 31)")
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setAlignment(Qt.AlignCenter)
        self.graphicsView.setRenderHints(QPainter.Antialiasing|QPainter.HighQualityAntialiasing|QPainter.TextAntialiasing)

        self.horizontalLayout.addWidget(self.graphicsView)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.labAccessHead = QLabel(self.frame)
        self.labAccessHead.setObjectName(u"labAccessHead")
        self.labAccessHead.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.labAccessHead)

        self.labArrayAccesses = QLabel(self.frame)
        self.labArrayAccesses.setObjectName(u"labArrayAccesses")
        self.labArrayAccesses.setStyleSheet(u"color: rgba(0, 0, 0, 150);")

        self.horizontalLayout_5.addWidget(self.labArrayAccesses)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.labComparisonHead = QLabel(self.frame)
        self.labComparisonHead.setObjectName(u"labComparisonHead")
        self.labComparisonHead.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.labComparisonHead)

        self.labComparisons = QLabel(self.frame)
        self.labComparisons.setObjectName(u"labComparisons")
        self.labComparisons.setStyleSheet(u"color: rgba(0, 0, 0, 150);")

        self.horizontalLayout_3.addWidget(self.labComparisons)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.labSortWithHead = QLabel(self.frame)
        self.labSortWithHead.setObjectName(u"labSortWithHead")
        self.labSortWithHead.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.labSortWithHead)

        self.labSortWith = QLabel(self.frame)
        self.labSortWith.setObjectName(u"labSortWith")
        self.labSortWith.setStyleSheet(u"color: rgba(0, 0, 0, 150);")

        self.horizontalLayout_2.addWidget(self.labSortWith)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labAmountHead = QLabel(self.frame)
        self.labAmountHead.setObjectName(u"labAmountHead")
        self.labAmountHead.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.labAmountHead)

        self.spinColAmount = QSpinBox(self.frame)
        self.spinColAmount.setObjectName(u"spinColAmount")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinColAmount.sizePolicy().hasHeightForWidth())
        self.spinColAmount.setSizePolicy(sizePolicy2)
        self.spinColAmount.setMinimumSize(QSize(0, 0))
        self.spinColAmount.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinColAmount.setStyleSheet(u"")
        self.spinColAmount.setReadOnly(False)
        self.spinColAmount.setMinimum(50)
        self.spinColAmount.setMaximum(500)
        self.spinColAmount.setSingleStep(50)
        self.spinColAmount.setValue(100)
        self.spinColAmount.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.spinColAmount)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labDelayHead = QLabel(self.frame)
        self.labDelayHead.setObjectName(u"labDelayHead")
        self.labDelayHead.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.labDelayHead)

        self.spinDelay = QSpinBox(self.frame)
        self.spinDelay.setObjectName(u"spinDelay")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinDelay.sizePolicy().hasHeightForWidth())
        self.spinDelay.setSizePolicy(sizePolicy3)
        self.spinDelay.setMinimumSize(QSize(68, 0))
        self.spinDelay.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinDelay.setStyleSheet(u"")
        self.spinDelay.setMinimum(1)
        self.spinDelay.setMaximum(20)
        self.spinDelay.setSingleStep(1)
        self.spinDelay.setValue(1)
        self.spinDelay.setDisplayIntegerBase(10)

        self.horizontalLayout_7.addWidget(self.spinDelay)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listAlgorithms = QListWidget(self.frame)
        __qlistwidgetitem = QListWidgetItem(self.listAlgorithms)
        __qlistwidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        QListWidgetItem(self.listAlgorithms)
        __qlistwidgetitem1 = QListWidgetItem(self.listAlgorithms)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        QListWidgetItem(self.listAlgorithms)
        QListWidgetItem(self.listAlgorithms)
        QListWidgetItem(self.listAlgorithms)
        QListWidgetItem(self.listAlgorithms)
        self.listAlgorithms.setObjectName(u"listAlgorithms")
        self.listAlgorithms.setStyleSheet(u"border: 1px solid rgba(0,0,0,30);\n"
"padding-top: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"color: rgba(0,0,0,120);\n"
"font: 87 14pt \"Roboto Light\";")
        self.listAlgorithms.setFrameShape(QFrame.StyledPanel)
        self.listAlgorithms.setFrameShadow(QFrame.Sunken)
        self.listAlgorithms.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listAlgorithms.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listAlgorithms.setDragDropMode(QAbstractItemView.InternalMove)
        self.listAlgorithms.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listAlgorithms.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listAlgorithms.setTextElideMode(Qt.ElideLeft)
        self.listAlgorithms.setLayoutMode(QListView.Batched)

        self.verticalLayout.addWidget(self.listAlgorithms)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btnSort = QPushButton(self.frame)
        self.btnSort.setObjectName(u"btnSort")
        sizePolicy2.setHeightForWidth(self.btnSort.sizePolicy().hasHeightForWidth())
        self.btnSort.setSizePolicy(sizePolicy2)
        self.btnSort.setMinimumSize(QSize(176, 30))
        self.btnSort.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSort.setStyleSheet(u"")
        self.btnSort.setFlat(False)

        self.horizontalLayout_4.addWidget(self.btnSort)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addWidget(self.frame)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.labAccessHead.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Array Accesses:</p></body></html>", None))
        self.labArrayAccesses.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>0</p></body></html>", None))
        self.labComparisonHead.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Comparisions:</p></body></html>", None))
        self.labComparisons.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>0</p></body></html>", None))
        self.labSortWithHead.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Sorting with:</p></body></html>", None))
        self.labSortWith.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Select an algorithm..</p></body></html>", None))
        self.labAmountHead.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Amount of columns</p></body></html>", None))
        self.labDelayHead.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Delay</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Algorithm List", None))

        __sortingEnabled = self.listAlgorithms.isSortingEnabled()
        self.listAlgorithms.setSortingEnabled(False)
        ___qlistwidgetitem = self.listAlgorithms.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Widget", u"Bubble Sort", None));
        ___qlistwidgetitem1 = self.listAlgorithms.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Widget", u"Select Sort", None));
        ___qlistwidgetitem2 = self.listAlgorithms.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Widget", u"Insert Sort", None));
        ___qlistwidgetitem3 = self.listAlgorithms.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Widget", u"Shell Sort", None));
        ___qlistwidgetitem4 = self.listAlgorithms.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Widget", u"Merge Sort", None));
        ___qlistwidgetitem5 = self.listAlgorithms.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Widget", u"Quick Sort", None));
        ___qlistwidgetitem6 = self.listAlgorithms.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Widget", u"Heap Sort", None));
        self.listAlgorithms.setSortingEnabled(__sortingEnabled)

        self.btnSort.setText(QCoreApplication.translate("Widget", u"sort", None))
    # retranslateUi

