# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playListwidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(554, 404)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(4, 4, 550, 398))
        self.widget.setStyleSheet("background-color:rgba(242, 250, 255,220);\n"
"border-style:solid;\n"
"    border-width:2px;\n"
"border-color:#e9e7ef")
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QTableWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(0, 30, 551, 371))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listWidget.setStyleSheet("QTableWidget QHeaderView{border:none}\n"
"QTableWidget\n"
"{\n"
"    height:16px;\n"
"    color:rgb(112,112,112);    /*前景色：文字颜色*/\n"
"    /*gridline-color:red;   */     /*表格中的网格线条颜色*/\n"
"    border-color:#e9e7ef;\n"
"    background:rgba(240, 252, 255, 120);\n"
"    /*设置交替颜色，需要在函数属性中设置:tableWidget->setAlternatingRowColors(true)*/\n"
"    alternate-background-color: rgb(245, 245, 245);\n"
"    selection-color:black;    /*鼠标选中时前景色：文字颜色*/\n"
"    selection-background-color:lightgray;   /*鼠标选中时背景色*/ /*边框线的宽度、颜色*/\n"
"    /*border:none;*/    /*去除边界线*/\n"
"    /*border-radius:5px;*/\n"
"    /*padding:10px 10px;*/  /*表格与边框的间距*/\n"
"}\n"
"\n"
"/*设置表头属性*/\n"
"\n"
"\n"
"QTableWidget QHeaderView::section\n"
"{background:#f0fcff;\n"
"    border:none;\n"
"border-right: 2px solid;\n"
"border-color:#e9e7ef;\n"
"height:25px;\n"
"font-size:16px;\n"
"font-style:\"微软雅黑\"\n"
"  /*lightgray*/\n"
"    /*color:black;*/\n"
"    /*padding-left:4px;*/\n"
"    /*border:3px solid red;*/   /*表头边框线的宽度、颜色*/\n"
"    /*border:1px solid gray;*/\n"
"}")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setLineWidth(1)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setShowGrid(False)
        self.listWidget.setWordWrap(False)
        self.listWidget.setCornerButtonEnabled(False)
        self.listWidget.setRowCount(2)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.listWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listWidget.setHorizontalHeaderItem(2, item)
        self.listWidget.horizontalHeader().setDefaultSectionSize(162)
        self.listWidget.horizontalHeader().setHighlightSections(False)
        self.listWidget.horizontalHeader().setMinimumSectionSize(0)
        self.listWidget.horizontalHeader().setStretchLastSection(True)
        self.listWidget.verticalHeader().setVisible(False)
        self.listWidget.verticalHeader().setDefaultSectionSize(22)
        self.listWidget.verticalHeader().setHighlightSections(False)
        self.listWidget.verticalHeader().setMinimumSectionSize(0)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 551, 30))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-bottom:none;\n"
"border-color:#e9e7ef")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setIndent(10)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(500, 3, 25, 25))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/buttons/clear.png);")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 554, 404))
        self.frame.setStyleSheet("QFrame { \n"
"    \n"
"                             background-color: transparent;\n"
"                             border-top: 4px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 rgb(180, 180, 180), stop: 1 transparent);\n"
"\n"
"                              border-left: 4px solid qlineargradient(x0:0, x1:1,\n"
"                                stop: 0 rgb(180, 180, 180), stop: 1 transparent);\n"
"                            \n"
"}     ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.widget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.listWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "歌名"))
        item = self.listWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "歌手"))
        item = self.listWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "时间"))
        self.label_3.setText(_translate("Form", "播放列表（共%d首）"))

import static.bgsrc_rc
