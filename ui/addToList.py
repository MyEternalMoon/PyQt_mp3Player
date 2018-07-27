# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addToList.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(5, 5, 290, 390))
        self.widget.setStyleSheet("background:white \n"
";border:rgb(181, 181, 181)")
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(0, 40, 290, 301))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget::item{min-height:30px;}\n"
"QListWidget::item:selected:!active{\n"
"background: #edd1d8;color:black}\n"
"QListWidget::item:selected:active{\n"
"background: #edd1d8;;color:black;border:none}\n"
"QListWidget::item:hover{text-indent:9px;\n"
"background-color: rgba(255, 240, 240, 240);;color:black}\n"
"QListWidget\n"
"{border:none;\n"
"color:#e4c6d0;\n"
"background-color:rgba(255, 244, 245, 245);\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.aButton = QtWidgets.QPushButton(self.widget)
        self.aButton.setGeometry(QtCore.QRect(100, 355, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.aButton.setFont(font)
        self.aButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aButton.setStyleSheet("QPushButton{border-radius:10px;\n"
"border-width:2px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"}\n"
"QPushButton:hover{color:#bc64a4}\n"
"")
        self.aButton.setObjectName("aButton")
        self.rButton = QtWidgets.QPushButton(self.widget)
        self.rButton.setGeometry(QtCore.QRect(190, 355, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.rButton.setFont(font)
        self.rButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rButton.setStyleSheet("QPushButton{border-radius:10px;\n"
"border-width:2px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"}\n"
"QPushButton:hover{color:#bc64a4}\n"
"")
        self.rButton.setObjectName("rButton")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 40, 300, 1))
        self.line.setStyleSheet("background:rgb(181, 181, 181)")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(0, 342, 300, 1))
        self.line_2.setStyleSheet("background:rgb(181, 181, 181)")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(5, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#e4c6d0;")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 400))
        self.frame.setStyleSheet("QFrame { \n"
"    \n"
"                             background-color: qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 rgba(255, 244, 245, 245), stop: 1 transparent);\n"
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
        self.widget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.aButton.setText(_translate("Form", "保存"))
        self.rButton.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "选择歌单"))

