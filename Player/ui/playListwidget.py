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
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(0, 33, 500, 367))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setStyleSheet("\n"
"QListWidget{color: rgb(112, 112, 112);outline:0px;color:grey}\n"
"\n"
"QListWidget::item:selected:!active{background-color:#e9f1f6;\n"
"color:black}\n"
"QListWidget::item:selected:active{background-color:#e9f1f6;\n"
"color:black}\n"
"QListWidget::item:hover{background-color:#e3f9fd;text-indent:9px;\n"
"color:black}\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setLineWidth(0)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
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
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "dfgh"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Form", "播放列表（共%d首）"))

import static.bgsrc_rc
