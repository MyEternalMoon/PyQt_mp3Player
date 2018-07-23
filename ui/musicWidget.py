# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 565)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 200, 570))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.listWidget.setStyleSheet("\n"
"\n"
"QListWidget QScrollBar:vertical{width:8px;}\n"
"QListWidget{;background-color: rgb(252, 239, 232);color: rgb(112, 112, 112);alternate-background-color: rgb(248, 235, 230);outline:0px;}\n"
"QListWidget::item:selected:!active{\n"
"border-image: url(:/bg/item.png);color:black}\n"
"QListWidget::item:selected:active{\n"
"border-image: url(:/bg/item.png);color:black}\n"
"QListWidget::item:hover{text-indent:9px;\n"
"background-color: rgb(255, 242, 223);color:black}\n"
"\n"
"\n"
"\n"
"")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import static.bgsrc_rc
