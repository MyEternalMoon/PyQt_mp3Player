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
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(710, 510)
        Form.setStyleSheet("background-color:{rgb(255,255,255,0)}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(5, 5, 700, 500))
        self.widget.setStyleSheet("background:rgb(254,255,254);\n"
"border-style:solid;\n"
"border-width:2px;\n"
"border-color:#e9e7ef")
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(4, 430, 690, 2))
        self.line.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.acceptButton = QtWidgets.QPushButton(self.widget)
        self.acceptButton.setGeometry(QtCore.QRect(460, 447, 90, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.acceptButton.setFont(font)
        self.acceptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acceptButton.setStyleSheet("QPushButton{border-radius:15px;\n"
"border-width:2px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"}\n"
"QPushButton:hover{color:#bc64a4}\n"
"")
        self.acceptButton.setObjectName("acceptButton")
        self.rejectButton = QtWidgets.QPushButton(self.widget)
        self.rejectButton.setGeometry(QtCore.QRect(580, 447, 90, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.rejectButton.setFont(font)
        self.rejectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rejectButton.setStyleSheet("QPushButton{border-radius:15px;\n"
"border-width:2px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"}QPushButton:hover{color:#bc64a4}")
        self.rejectButton.setObjectName("rejectButton")
        self.optionWidget = QtWidgets.QListWidget(self.widget)
        self.optionWidget.setGeometry(QtCore.QRect(0, 79, 180, 351))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.optionWidget.setFont(font)
        self.optionWidget.setStyleSheet("QListWidget::item{min-height:60px;}\n"
"QListWidget::item:selected:!active{\n"
"background: #edd1d8;color:black}\n"
"QListWidget::item:selected:active{\n"
"background: #edd1d8;;color:black;border:none}\n"
"QListWidget::item:hover{text-indent:9px;\n"
"background-color: rgba(255, 240, 240, 240);;color:black}\n"
"QListWidget\n"
"{\n"
"color:rgb(140,140,140);\n"
"background-color:rgba(255, 244, 245, 245);\n"
"border-bottom:none}")
        self.optionWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.optionWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.optionWidget.setLineWidth(0)
        self.optionWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.optionWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.optionWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.optionWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.optionWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.optionWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.optionWidget.setModelColumn(0)
        self.optionWidget.setBatchSize(200)
        self.optionWidget.setObjectName("optionWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.optionWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.optionWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.optionWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.optionWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.optionWidget.addItem(item)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 2, 180, 77))
        self.label.setStyleSheet("border-bottom:none;\n"
"border-top:none;\n"
"background-color:rgba(255, 244, 245, 245)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.optionLabel = QtWidgets.QLabel(self.widget)
        self.optionLabel.setGeometry(QtCore.QRect(190, 20, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setKerning(False)
        self.optionLabel.setFont(font)
        self.optionLabel.setStyleSheet("border:none;\n"
"color:grey")
        self.optionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.optionLabel.setObjectName("optionLabel")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(270, 37, 400, 2))
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(200, 70, 480, 330))
        self.widget_2.setStyleSheet("color:#e4c6d0;\n"
"\n"
"border:none")
        self.widget_2.setObjectName("widget_2")
        self.speWidget = QtWidgets.QListWidget(self.widget_2)
        self.speWidget.setGeometry(QtCore.QRect(0, 0, 480, 330))
        self.speWidget.setStyleSheet("color:grey;\n"
"font-size:13px")
        self.speWidget.setObjectName("speWidget")
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 115, 250))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.config1_2 = QtWidgets.QLabel(self.groupBox)
        self.config1_2.setGeometry(QtCore.QRect(0, 0, 115, 45))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        self.config1_2.setFont(font)
        self.config1_2.setStyleSheet("color:grey")
        self.config1_2.setWordWrap(True)
        self.config1_2.setIndent(3)
        self.config1_2.setObjectName("config1_2")
        self.config2_2 = QtWidgets.QLabel(self.groupBox)
        self.config2_2.setGeometry(QtCore.QRect(0, 50, 115, 45))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        self.config2_2.setFont(font)
        self.config2_2.setStyleSheet("color:grey;")
        self.config2_2.setWordWrap(True)
        self.config2_2.setObjectName("config2_2")
        self.config3_2 = QtWidgets.QLabel(self.groupBox)
        self.config3_2.setGeometry(QtCore.QRect(0, 110, 115, 45))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        self.config3_2.setFont(font)
        self.config3_2.setStyleSheet("color:grey")
        self.config3_2.setWordWrap(True)
        self.config3_2.setObjectName("config3_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setGeometry(QtCore.QRect(117, 20, 245, 250))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.option1 = QtWidgets.QLabel(self.groupBox_2)
        self.option1.setGeometry(QtCore.QRect(0, 0, 245, 45))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        self.option1.setFont(font)
        self.option1.setStyleSheet("color:grey")
        self.option1.setWordWrap(True)
        self.option1.setObjectName("option1")
        self.option2 = QtWidgets.QLabel(self.groupBox_2)
        self.option2.setGeometry(QtCore.QRect(0, 50, 245, 45))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        self.option2.setFont(font)
        self.option2.setStyleSheet("color:grey")
        self.option2.setWordWrap(True)
        self.option2.setObjectName("option2")
        self.option1_3 = QtWidgets.QLabel(self.groupBox_2)
        self.option1_3.setGeometry(QtCore.QRect(0, 110, 245, 45))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(11)
        self.option1_3.setFont(font)
        self.option1_3.setStyleSheet("color:grey")
        self.option1_3.setWordWrap(True)
        self.option1_3.setObjectName("option1_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 20, 78, 250))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 120, 78, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{border-radius:15px;\n"
"border-width:2px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"}\n"
"QPushButton:hover{color:#bc64a4}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 60, 78, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{border-radius:15px;\n"
"border-width:2px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"}\n"
"QPushButton:hover{color:#bc64a4}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 78, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{border-radius:15px;\n"
"border-width:2px;\n"
"border-color:#e4c6d0;\n"
"border-style:solid;\n"
"background:white;\n"
"color:#e4c6d0;\n"
"}\n"
"QPushButton:hover{color:#bc64a4}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.label_2.setStyleSheet("QLabel{border:none;\n"
"background-color:rgba(255, 244, 245, 245);\n"
"border-image: url(:/bg/config_hover.png);}\n"
"QLabel:hover{border-image: url(:/bg/config.png);}\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(80, 30, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;\n"
"color:rgb(112,112,112);\n"
"background-color:rgba(255, 244, 245, 245)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(550, 300, 121, 121))
        self.label_4.setStyleSheet("border:none;\n"
"border-image: url(:/bg/sakura_PNG43.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 710, 510))
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
        self.widget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Config"))
        self.acceptButton.setText(_translate("Form", "确认"))
        self.rejectButton.setText(_translate("Form", "取消"))
        __sortingEnabled = self.optionWidget.isSortingEnabled()
        self.optionWidget.setSortingEnabled(False)
        item = self.optionWidget.item(0)
        item.setText(_translate("Form", "基础设置"))
        item = self.optionWidget.item(1)
        item.setText(_translate("Form", "用户设置"))
        item = self.optionWidget.item(2)
        item.setText(_translate("Form", "个性化"))
        item = self.optionWidget.item(3)
        item.setText(_translate("Form", "帮助"))
        item = self.optionWidget.item(4)
        item.setText(_translate("Form", "关于"))
        self.optionWidget.setSortingEnabled(__sortingEnabled)
        self.optionLabel.setText(_translate("Form", "Default"))
        self.config1_2.setText(_translate("Form", "1"))
        self.config2_2.setText(_translate("Form", "2"))
        self.config3_2.setText(_translate("Form", "3"))
        self.option1.setText(_translate("Form", "1"))
        self.option2.setText(_translate("Form", "2"))
        self.option1_3.setText(_translate("Form", "3"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton.setText(_translate("Form", "1"))
        self.label_3.setText(_translate("Form", "设置"))

import static.bgsrc_rc
