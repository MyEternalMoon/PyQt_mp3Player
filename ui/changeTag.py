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
        Form.resize(360, 220)
        Form.setStyleSheet("QWidget{background-color:white;border:none}\n"
"")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 360, 220))
        self.widget.setStyleSheet("QWidget{border-radius:20px}\n"
"QLineEdit{border-radius:10px;\n"
"border-style:dashed;\n"
"border-width:1px;\n"
"border-color:#db5a6b;\n"
"color:#db5a6b;\n"
"font-size:16px}\n"
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
        self.widget.setObjectName("widget")
        self.album = QtWidgets.QLineEdit(self.widget)
        self.album.setGeometry(QtCore.QRect(100, 130, 230, 25))
        self.album.setObjectName("album")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 70, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 70, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(250, 180, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.aritist = QtWidgets.QLineEdit(self.widget)
        self.aritist.setGeometry(QtCore.QRect(100, 80, 230, 25))
        self.aritist.setObjectName("aritist")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 180, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 70, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.title = QtWidgets.QLineEdit(self.widget)
        self.title.setGeometry(QtCore.QRect(100, 30, 230, 25))
        self.title.setObjectName("title")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "曲名"))
        self.label_3.setText(_translate("Form", "专辑"))
        self.pushButton.setText(_translate("Form", "确认"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.label_2.setText(_translate("Form", "艺术家"))

