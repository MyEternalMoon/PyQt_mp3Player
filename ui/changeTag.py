# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeTag.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 308)
        Form.setStyleSheet("QWidget{background-color:rgba(255, 244, 245, 240);;border:none}\n"
"")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(4, 4, 360, 300))
        self.widget.setStyleSheet("\n"
"QLineEdit{border-radius:8px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:rgb(180,180,180);\n"
"color:#db5a6b;\n"
"font-size:17px}\n"
"QLabel{color:rgb(100,100,100);font-family:\"微软雅黑 Light\";\n"
"font-size:18px\n"
"}\n"
"QPushButton{border-radius:12px;\n"
"border-width:1px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#db5a6b;\n"
"font-size:18px;\n"
"font-family:\"微软雅黑 Light\"\n"
"}\n"
"QPushButton:hover{\n"
"background:rgba(200,200,200,140);color:#4b5cc4;\n"
"border-color:#4b5cc4;\n"
"text-decoration:underline}")
        self.widget.setObjectName("widget")
        self.album = QtWidgets.QLineEdit(self.widget)
        self.album.setGeometry(QtCore.QRect(100, 190, 230, 25))
        self.album.setObjectName("album")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 90, 70, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 70, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 255, 80, 30))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton:hover{color: rgb(249, 144, 111);background:rgb(250,250,250)}\n"
"QPushButton{border:1px solid rgb(180,180,180);\n"
"border-radius:8px;background-color:white;color:rgb(100,100,100)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.aritist = QtWidgets.QLineEdit(self.widget)
        self.aritist.setGeometry(QtCore.QRect(100, 140, 230, 25))
        self.aritist.setObjectName("aritist")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(140, 255, 80, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{background-color:rgb(228, 198, 208);;border:1px solid rgb(180,180,180);border-radius:8px;color:rgb(100,100,100)}\n"
"QPushButton:hover{color: black;background-color:rgb(220, 190, 200)}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 70, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.title = QtWidgets.QLineEdit(self.widget)
        self.title.setGeometry(QtCore.QRect(100, 90, 230, 25))
        self.title.setObjectName("title")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 25, 320, 30))
        self.label_4.setStyleSheet("font-size:20px;\n"
"color:rgb(10,10,10)")
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 240, 360, 2))
        self.line.setStyleSheet("background:rgb(200,200,200)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(0, 70, 360, 2))
        self.line_2.setStyleSheet("background:rgb(200,200,200)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 368, 308))
        self.frame.setStyleSheet("QFrame { \n"
"    \n"
"                             background-color: transparent;\n"
"                             border-top: 4px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 rgb(180, 180, 180), stop: 1 transparent);\n"
"    \n"
"                              border-left: 4px solid qlineargradient(x0:0, x1:1,\n"
"                                stop: 0 rgb(180, 180, 180), stop: 1 transparent);\n"
"                             border-bottom: 4px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 transparent, stop: 1 rgb(180, 180, 180));\n"
"                             border-right: 4px solid qlineargradient(x0:0, x1:1,\n"
"                               stop:  0 transparent, stop: 1 rgb(180, 180, 180));\n"
";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.widget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.title, self.aritist)
        Form.setTabOrder(self.aritist, self.album)
        Form.setTabOrder(self.album, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "曲名"))
        self.label_3.setText(_translate("Form", "专辑"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton.setText(_translate("Form", "确认"))
        self.label_2.setText(_translate("Form", "艺术家"))
        self.label_4.setText(_translate("Form", "修改Tag只作用于本地音乐"))

