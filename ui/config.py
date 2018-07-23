# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(516, 416)
        Form.setStyleSheet("background-color:{rgb(255,255,255,0)}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(8, 8, 500, 400))
        self.widget.setStyleSheet("\n"
"background-color: rgb(252, 239, 232);\n"
"border-color:grey")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(8, 0, 500, 8))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.65 rgba(252, 239, 232, 0), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(8, 408, 500, 8))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.65 rgba(252, 239, 232, 0), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 8, 8, 400))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:0, y2:0, stop:0.65 rgba(252, 239, 232, 0), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(508, 8, 8, 400))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.65 rgba(252, 239, 232, 0), stop:1 rgba(255, 255, 255, 255));")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


