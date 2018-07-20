# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playingwidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.centeralwidget = QtWidgets.QWidget(Form)
        self.centeralwidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.centeralwidget.setObjectName("centeralwidget")
        self.lyricBrowser = QtWidgets.QTextBrowser(self.centeralwidget)
        self.lyricBrowser.setGeometry(QtCore.QRect(100, 100, 600, 450))
        self.lyricBrowser.setStyleSheet("")
        self.lyricBrowser.setObjectName("lyricBrowser")
        self.bgLabel = QtWidgets.QLabel(self.centeralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.infoLabel = QtWidgets.QLabel(self.centeralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(100, 30, 600, 50))
        self.infoLabel.setObjectName("infoLabel")
        self.bgLabel.raise_()
        self.infoLabel.raise_()
        self.lyricBrowser.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lyricBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gdfhsdfhgt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">dsfsdfg</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">sdfghjsd</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">sdfjg</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">sdfgjh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">adsfbjhk</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">sdafbjk</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">asdgkfj</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt;\">\'asdkjgf </span></p></body></html>"))
        self.infoLabel.setText(_translate("Form", "<html><head/><body><p>sdfg</p></body></html>"))

