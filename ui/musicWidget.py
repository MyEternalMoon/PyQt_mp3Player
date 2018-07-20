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
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.listWidget.setStyleSheet("\n"
"QListWidget{background-color: rgb(252, 239, 232);color: rgb(112, 112, 112);}\n"
"\n"
"QListWidget::item:selected:!active{\n"
"background-color: rgb(237, 209, 216);color:black}\n"
"QListWidget::item:selected:active{\n"
"background-color:  rgb(237, 209, 216);color:black}\n"
"QListWidget::item:hover{\n"
"background-color: rgb(255, 242, 223);color:black}")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

