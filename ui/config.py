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
        Form.resize(716, 516)
        Form.setStyleSheet("background-color:{rgb(255,255,255,0)}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(8, 8, 700, 500))
        self.widget.setStyleSheet("background:white;\n"
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
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.optionWidget.setFont(font)
        self.optionWidget.setStyleSheet("QListWidget::item{min-height:70px;}\n"
"QListWidget::item:selected:!active{\n"
"background: #edd1d8;color:black}\n"
"QListWidget::item:selected:active{\n"
"background: #edd1d8;;color:black;border:none}\n"
"QListWidget::item:hover{text-indent:9px;\n"
"background-color: rgba(255, 240, 240, 240);;color:black}\n"
"QListWidget\n"
"{\n"
"color:#e4c6d0;\n"
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
        font.setFamily("Arial")
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
        self.speWidget.setStyleSheet("color:#e4c6d0;\n"
"font-size:13px")
        self.speWidget.setObjectName("speWidget")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(370, 20, 70, 30))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 80, 70, 30))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 140, 70, 30))
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
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 100, 150))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.config1_2 = QtWidgets.QLabel(self.groupBox)
        self.config1_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.config1_2.setWordWrap(True)
        self.config1_2.setObjectName("config1_2")
        self.config2_2 = QtWidgets.QLabel(self.groupBox)
        self.config2_2.setGeometry(QtCore.QRect(0, 60, 100, 30))
        self.config2_2.setStyleSheet("margin:0;padding:0")
        self.config2_2.setWordWrap(True)
        self.config2_2.setObjectName("config2_2")
        self.config3_2 = QtWidgets.QLabel(self.groupBox)
        self.config3_2.setGeometry(QtCore.QRect(0, 120, 100, 30))
        self.config3_2.setWordWrap(True)
        self.config3_2.setObjectName("config3_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 20, 220, 150))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.option1 = QtWidgets.QLabel(self.groupBox_2)
        self.option1.setGeometry(QtCore.QRect(0, 0, 220, 30))
        self.option1.setObjectName("option1")
        self.option2 = QtWidgets.QLabel(self.groupBox_2)
        self.option2.setGeometry(QtCore.QRect(0, 60, 220, 30))
        self.option2.setObjectName("option2")
        self.option1_3 = QtWidgets.QLabel(self.groupBox_2)
        self.option1_3.setGeometry(QtCore.QRect(0, 120, 220, 30))
        self.option1_3.setObjectName("option1_3")
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
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;\n"
"color:#e4c6d0;\n"
"background-color:rgba(255, 244, 245, 245)")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 716, 516))
        self.frame.setStyleSheet("QFrame { \n"
"                             background-color: transparent;\n"
"                             border-top: 8px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 rgba(255, 244, 245, 245), stop: 1 transparent);\n"
"                              border-left: 8px solid qlineargradient(x0:0, x1:1,\n"
"                                stop: 0 rgba(255, 244, 245, 245), stop: 1 transparent);\n"
"                             border-bottom: 8px solid qlineargradient(y0:0, y1:1,\n"
"                                stop: 0 transparent, stop: 1  rgba(255, 244, 245, 245));\n"
"                             border-right: 8px solid qlineargradient(x0:0, x1:1,\n"
"                               stop:  0 transparent, stop: 1 rgba(255, 244, 245, 245));\n"
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
        item.setText(_translate("Form", "关于"))
        self.optionWidget.setSortingEnabled(__sortingEnabled)
        self.optionLabel.setText(_translate("Form", "Default"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.config1_2.setText(_translate("Form", "关闭后仍记录播放列表"))
        self.config2_2.setText(_translate("Form", "2"))
        self.config3_2.setText(_translate("Form", "3"))
        self.option1.setText(_translate("Form", "1"))
        self.option2.setText(_translate("Form", "2"))
        self.option1_3.setText(_translate("Form", "3"))
        self.label_3.setText(_translate("Form", "Config"))

import static.bgsrc_rc
