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
        Dialog.resize(370, 270)
        Dialog.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(5, 5, 360, 260))
        self.widget.setStyleSheet("\n"
"background-color:rgba(255, 244, 245, 240);")
        self.widget.setObjectName("widget")
        self.acceptButton = QtWidgets.QPushButton(self.widget)
        self.acceptButton.setGeometry(QtCore.QRect(140, 220, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.acceptButton.setFont(font)
        self.acceptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acceptButton.setStyleSheet("\n"
"QPushButton{background-color:rgb(228, 198, 208);;border:1px solid rgb(180,180,180);border-radius:5px;color:rgb(100,100,100)}\n"
"\n"
"QPushButton:hover{color: rgb(249, 144, 111);background-color:rgb(220, 190, 200)}")
        self.acceptButton.setAutoDefault(False)
        self.acceptButton.setFlat(False)
        self.acceptButton.setObjectName("acceptButton")
        self.rejectButton = QtWidgets.QPushButton(self.widget)
        self.rejectButton.setGeometry(QtCore.QRect(250, 220, 80, 30))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(10)
        self.rejectButton.setFont(font)
        self.rejectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rejectButton.setStyleSheet("QPushButton:hover{color: rgb(249, 144, 111);background:rgb(250,250,250)}\n"
"QPushButton{border:1px solid rgb(180,180,180);\n"
"border-radius:5px;background-color:white;color:rgb(100,100,100)}")
        self.rejectButton.setAutoDefault(False)
        self.rejectButton.setFlat(False)
        self.rejectButton.setObjectName("rejectButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(25, 80, 310, 90))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(90,90,90);\n"
"background-color:transparent\n"
"\n"
"")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 200, 360, 1))
        self.line.setStyleSheet("background:rgb(200,200,200)")
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 360, 1))
        self.line_2.setStyleSheet("background:rgb(200,200,200)")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(25, 10, 310, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color:rgb(80,80,80);\n"
"background-color:transparent")
        self.title.setText("")
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 370, 270))
        self.frame.setStyleSheet("QFrame { \n"
"    \n"
"                             background-color: transparent;\n"
"                             border-top: 5px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 rgb(160, 160, 160), stop: 1 transparent);\n"
"    \n"
"                              border-left: 5px solid qlineargradient(x0:0, x1:1,\n"
"                                stop: 0 rgb(160, 160, 160), stop: 1 transparent);\n"
"                             border-bottom: 5px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 transparent, stop: 1 rgb(160, 160, 160));\n"
"                             border-right: 5px solid qlineargradient(x0:0, x1:1,\n"
"                               stop:  0 transparent, stop: 1 rgb(160, 160, 160));\n"
";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.widget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.acceptButton.setText(_translate("Dialog", "删除"))
        self.acceptButton.setShortcut(_translate("Dialog", "Return"))
        self.rejectButton.setText(_translate("Dialog", "取消"))
        self.rejectButton.setShortcut(_translate("Dialog", "Esc"))

