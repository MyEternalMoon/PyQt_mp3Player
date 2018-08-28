# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 380)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bg/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(5, 5, 400, 370))
        self.widget_2.setStyleSheet("background-color:rgba(255, 244, 245, 240);")
        self.widget_2.setObjectName("widget_2")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 60))
        self.widget.setStyleSheet("background-color: rgba(228, 198, 208,230);")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 15, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(40,40,40)")
        self.label_2.setObjectName("label_2")
        self.picLabel = QtWidgets.QLabel(self.widget_2)
        self.picLabel.setGeometry(QtCore.QRect(60, 150, 120, 120))
        self.picLabel.setText("")
        self.picLabel.setObjectName("picLabel")
        self.acceptButton = QtWidgets.QPushButton(self.widget_2)
        self.acceptButton.setGeometry(QtCore.QRect(80, 315, 80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acceptButton.setFont(font)
        self.acceptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acceptButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.acceptButton.setStyleSheet("QPushButton{background-color:rgb(228, 198, 208);;border:1px solid rgb(180,180,180);border-radius:8px;color:rgb(100,100,100)}\n"
"QPushButton:hover{color: black;background-color:rgb(220, 190, 200)}")
        self.acceptButton.setFlat(True)
        self.acceptButton.setObjectName("acceptButton")
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.nameLineEdit.setGeometry(QtCore.QRect(50, 90, 300, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setKerning(True)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.nameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nameLineEdit.setMaxLength(20)
        self.nameLineEdit.setFrame(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.rejectButton = QtWidgets.QPushButton(self.widget_2)
        self.rejectButton.setGeometry(QtCore.QRect(240, 315, 80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.rejectButton.setFont(font)
        self.rejectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rejectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rejectButton.setStyleSheet("QPushButton:hover{color: rgb(249, 144, 111);background:rgb(250,250,250)}\n"
"QPushButton{border:1px solid rgb(180,180,180);\n"
"border-radius:8px;background-color:white;color:rgb(100,100,100)}")
        self.rejectButton.setObjectName("rejectButton")
        self.fileDialogButton = QtWidgets.QPushButton(self.widget_2)
        self.fileDialogButton.setGeometry(QtCore.QRect(220, 240, 90, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.fileDialogButton.setFont(font)
        self.fileDialogButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileDialogButton.setStyleSheet("QPushButton{background:rgba(230,230,230,80);border:1px solid rgb(200,200,200);\n"
"border-radius:4px;color:rgb(90,90,90)}\n"
"QPushButton:hover{background:rgb(225, 225, 235);color: black;border-color:rgb(140,140,140)}")
        self.fileDialogButton.setObjectName("fileDialogButton")
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setGeometry(QtCore.QRect(0, 300, 400, 2))
        self.line.setStyleSheet("background-color: rgb(200,200,200)")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setGeometry(QtCore.QRect(55, 275, 130, 3))
        self.line_2.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setGeometry(QtCore.QRect(55, 142, 130, 3))
        self.line_3.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setGeometry(QtCore.QRect(55, 143, 3, 134))
        self.line_4.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(185, 143, 3, 134))
        self.line_5.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 410, 380))
        self.frame.setStyleSheet("QFrame { \n"
"    \n"
"                             background-color: transparent;\n"
"                             border-top: 5px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 rgb(180, 180, 180), stop: 1 transparent);\n"
"    \n"
"                              border-left: 5px solid qlineargradient(x0:0, x1:1,\n"
"                                stop: 0 rgb(180, 180, 180), stop: 1 transparent);\n"
"                             border-bottom: 5px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 transparent, stop: 1 rgb(180, 180, 180));\n"
"                             border-right: 5px solid qlineargradient(x0:0, x1:1,\n"
"                               stop:  0 transparent, stop: 1 rgb(180, 180, 180));\n"
";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.widget_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New"))
        self.label_2.setText(_translate("Dialog", "新建歌单"))
        self.acceptButton.setText(_translate("Dialog", "创建"))
        self.acceptButton.setShortcut(_translate("Dialog", "Return"))
        self.nameLineEdit.setPlaceholderText(_translate("Dialog", " 请输入新的歌单标题"))
        self.rejectButton.setText(_translate("Dialog", "取消"))
        self.rejectButton.setShortcut(_translate("Dialog", "Esc"))
        self.fileDialogButton.setText(_translate("Dialog", "选择头像"))

