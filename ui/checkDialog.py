# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 180)
        Dialog.setStyleSheet("background-color: #e9e7ef")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 360, 180))
        self.widget.setObjectName("widget")
        self.acceptButton = QtWidgets.QPushButton(self.widget)
        self.acceptButton.setGeometry(QtCore.QRect(130, 135, 70, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.acceptButton.setFont(font)
        self.acceptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acceptButton.setStyleSheet("\n"
"QPushButton{background-color:rgb(228, 198, 208);;border:0px;border-radius:5px;}\n"
"\n"
"QPushButton:hover{color: rgb(249, 144, 111);}")
        self.acceptButton.setAutoDefault(False)
        self.acceptButton.setFlat(False)
        self.acceptButton.setObjectName("acceptButton")
        self.rejectButton = QtWidgets.QPushButton(self.widget)
        self.rejectButton.setGeometry(QtCore.QRect(250, 135, 70, 30))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(10)
        self.rejectButton.setFont(font)
        self.rejectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rejectButton.setStyleSheet("QPushButton:hover{color: rgb(249, 144, 111);}\n"
"QPushButton{border:1px;\n"
"border-radius:5px;background-color:white}")
        self.rejectButton.setAutoDefault(False)
        self.rejectButton.setFlat(False)
        self.rejectButton.setObjectName("rejectButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(25, 30, 310, 70))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.acceptButton.setText(_translate("Dialog", "删除"))
        self.acceptButton.setShortcut(_translate("Dialog", "Return"))
        self.rejectButton.setText(_translate("Dialog", "取消"))
        self.rejectButton.setShortcut(_translate("Dialog", "Esc"))

