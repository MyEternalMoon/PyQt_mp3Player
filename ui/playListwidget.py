# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playListwidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,Qt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 408)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 4, 8, 404))
        self.label.setStyleSheet("border-image: url(:/bg/lm.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(4, 0, 504, 8))
        self.label_2.setStyleSheet("border-image: url(:/bg/tm.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(8, 8, 500, 400))
        self.widget.setStyleSheet("background-color:#f0fcff")
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 30, 500, 3))
        self.line.setStyleSheet("background-color:#e9f1f6;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QTableWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(0, 33, 500, 367))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setStyleSheet("QTableWidget\n"
"{\n"
"\n"
"    color:green;    /*前景色：文字颜色*/\n"
"    /*gridline-color:red;   */     /*表格中的网格线条颜色*/\n"
"border:none;\n"
"    background:#f0fcff;\n"
"    /*设置交替颜色，需要在函数属性中设置:tableWidget->setAlternatingRowColors(true)*/\n"
"    alternate-background-color: rgb(245, 245, 245);\n"
"    selection-color:red;    /*鼠标选中时前景色：文字颜色*/\n"
"    selection-background-color:lightgray;   /*鼠标选中时背景色*/ /*边框线的宽度、颜色*/\n"
"    /*border:none;*/    /*去除边界线*/\n"
"    /*border-radius:5px;*/\n"
"    /*padding:10px 10px;*/  /*表格与边框的间距*/\n"
"}\n"
"\n"
"/*设置表头属性*/\n"
"QTableWidget QHeaderView::section\n"
"{background:#f0fcff;\n"
"    border:none;\n"
"text-align:left;\n"
"  /*lightgray*/\n"
"    /*color:black;*/\n"
"    /*padding-left:4px;*/\n"
"    /*border:3px solid red;*/   /*表头边框线的宽度、颜色*/\n"
"    /*border:1px solid gray;*/\n"
"}")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setLineWidth(0)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setAlternatingRowColors(True)
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
        self.label_3.setGeometry(QtCore.QRect(0, 0, 500, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(10)
        self.label_3.setObjectName("label_3")

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
