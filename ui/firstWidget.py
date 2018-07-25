# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 330)
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(11)
        Form.setFont(font)
        Form.setStyleSheet("QWidget{background-color:white;border:none}\n"
"QLabel{color:#808080;font-family:\"微软雅黑 Light\";\n"
"font-size:18px\n"
"}\n"
"QPushButton{border-radius:12px;\n"
"border-width:1px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"font-size:17px;\n"
"font-family:\"微软雅黑 Light\"\n"
"}\n"
"QPushButton:hover{color:#4b5cc4;\n"
"border-color:#4b5cc4;\n"
"text-decoration:underline}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 471, 331))
        self.widget.setObjectName("widget")
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setGeometry(QtCore.QRect(15, 140, 440, 25))
        self.label3.setWordWrap(True)
        self.label3.setObjectName("label3")
        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setGeometry(QtCore.QRect(15, 40, 345, 25))
        self.label1.setObjectName("label1")
        self.label4 = QtWidgets.QLabel(self.widget)
        self.label4.setGeometry(QtCore.QRect(15, 190, 170, 25))
        self.label4.setObjectName("label4")
        self.pushButton1 = QtWidgets.QPushButton(self.widget)
        self.pushButton1.setGeometry(QtCore.QRect(365, 40, 90, 25))
        self.pushButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton1.setObjectName("pushButton1")
        self.randomButton = QtWidgets.QPushButton(self.widget)
        self.randomButton.setGeometry(QtCore.QRect(365, 190, 90, 25))
        self.randomButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.randomButton.setObjectName("randomButton")
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setGeometry(QtCore.QRect(15, 90, 345, 25))
        self.label2.setObjectName("label2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 190, 150, 25))
        self.lineEdit.setStyleSheet("border-radius:10px;\n"
"border-style:dashed;\n"
"border-width:1px;\n"
"border-color:#db5a6b;\n"
"color:#db5a6b;\n"
"font-size:16px")
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton2 = QtWidgets.QPushButton(self.widget)
        self.pushButton2.setGeometry(QtCore.QRect(365, 90, 90, 25))
        self.pushButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton2.setObjectName("pushButton2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(230, 240, 231, 25))
        self.checkBox.setStyleSheet("color:#808080;font-family:\"微软雅黑 Light\";\n"
"font-size:15px")
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label3.setText(_translate("Form", "我们将把图像文件储存在这里：%s"))
        self.label1.setText(_translate("Form", "我们将创建一个新文件夹：%s"))
        self.label4.setText(_translate("Form", "取选个好听的名字吧~"))
        self.pushButton1.setText(_translate("Form", "选择路径"))
        self.randomButton.setText(_translate("Form", "随机"))
        self.label2.setText(_translate("Form", "也许需要设置本地音乐位置：%s"))
        self.pushButton2.setText(_translate("Form", "选择路径"))
        self.checkBox.setText(_translate("Form", "English Style Random Name"))

