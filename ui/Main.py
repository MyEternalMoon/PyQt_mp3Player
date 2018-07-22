# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 750))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bg/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"background-color: rgb(252, 239, 232);")
        self.centralwidget.setObjectName("centralwidget")
        self.LowerNav = QtWidgets.QWidget(self.centralwidget)
        self.LowerNav.setGeometry(QtCore.QRect(0, 670, 1000, 80))
        self.LowerNav.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LowerNav.setStyleSheet("background-color: #edd1d8;")
        self.LowerNav.setObjectName("LowerNav")
        self.PlayButton = QtWidgets.QPushButton(self.LowerNav)
        self.PlayButton.setGeometry(QtCore.QRect(470, 10, 60, 60))
        self.PlayButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PlayButton.setStyleSheet("QPushButton#PlayButton{border-image: url(:/bg/play.png);}\n"
"\n"
"QPushButton#PlayButton:hover{border-image: url(:/bg/play_hover.png);}")
        self.PlayButton.setText("")
        self.PlayButton.setFlat(False)
        self.PlayButton.setObjectName("PlayButton")
        self.cTimeLabel = QtWidgets.QLabel(self.LowerNav)
        self.cTimeLabel.setGeometry(QtCore.QRect(20, 30, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cTimeLabel.setFont(font)
        self.cTimeLabel.setToolTipDuration(-2)
        self.cTimeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.cTimeLabel.setObjectName("cTimeLabel")
        self.eTimeLabel = QtWidgets.QLabel(self.LowerNav)
        self.eTimeLabel.setGeometry(QtCore.QRect(330, 30, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eTimeLabel.setFont(font)
        self.eTimeLabel.setToolTipDuration(-2)
        self.eTimeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.eTimeLabel.setObjectName("eTimeLabel")
        self.FormerButton = QtWidgets.QPushButton(self.LowerNav)
        self.FormerButton.setGeometry(QtCore.QRect(410, 20, 40, 40))
        self.FormerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FormerButton.setStyleSheet("QPushButton#FormerButton{border-image: url(:/bg/former.png)}\n"
"QPushButton#FormerButton:hover{\n"
"    border-image: url(:/bg/former_hover.png)}")
        self.FormerButton.setText("")
        self.FormerButton.setObjectName("FormerButton")
        self.NextButton = QtWidgets.QPushButton(self.LowerNav)
        self.NextButton.setGeometry(QtCore.QRect(550, 20, 40, 40))
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setStyleSheet("QPushButton#NextButton{border-image: url(:/bg/next.png)}\n"
"QPushButton#NextButton:hover{\n"
"    border-image: url(:/bg/next_hover.png)}")
        self.NextButton.setText("")
        self.NextButton.setObjectName("NextButton")
        self.SoundButton = QtWidgets.QPushButton(self.LowerNav)
        self.SoundButton.setGeometry(QtCore.QRect(630, 25, 18, 28))
        self.SoundButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SoundButton.setStyleSheet("border-image: url(:/bg/audio.png);")
        self.SoundButton.setText("")
        self.SoundButton.setObjectName("SoundButton")
        self.lyricButton = QtWidgets.QPushButton(self.LowerNav)
        self.lyricButton.setGeometry(QtCore.QRect(870, 25, 30, 30))
        self.lyricButton.setObjectName("lyricButton")
        self.orderButton = QtWidgets.QPushButton(self.LowerNav)
        self.orderButton.setGeometry(QtCore.QRect(920, 25, 30, 30))
        self.orderButton.setStyleSheet("")
        self.orderButton.setObjectName("orderButton")
        self.TopNav = QtWidgets.QWidget(self.centralwidget)
        self.TopNav.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.TopNav.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.TopNav.setStyleSheet("\n"
"background-color: #edd1d8;")
        self.TopNav.setObjectName("TopNav")
        self.SearchEdit = QtWidgets.QLineEdit(self.TopNav)
        self.SearchEdit.setGeometry(QtCore.QRect(180, 18, 265, 24))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(9)
        self.SearchEdit.setFont(font)
        self.SearchEdit.setStyleSheet("border-radius:7px;\n"
"background-color: rgb(228, 198, 208)\n"
"")
        self.SearchEdit.setInputMask("")
        self.SearchEdit.setText("")
        self.SearchEdit.setMaxLength(25)
        self.SearchEdit.setFrame(False)
        self.SearchEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.SearchEdit.setObjectName("SearchEdit")
        self.exitButton = QtWidgets.QPushButton(self.TopNav)
        self.exitButton.setGeometry(QtCore.QRect(960, 20, 20, 20))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("QPushButton#exitButton{border-image: url(:/bg/exit.png);}\n"
"QPushButton#exitButton:hover{\n"
"    border-image: url(:/bg/exit_hover.png);}")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        self.hideButton = QtWidgets.QPushButton(self.TopNav)
        self.hideButton.setGeometry(QtCore.QRect(930, 20, 20, 20))
        self.hideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hideButton.setStyleSheet("QPushButton#hideButton{\n"
"    border-image: url(:/bg/hide.png);}\n"
"QPushButton#hideButton:hover{\n"
"    border-image: url(:/bg/hide_hover.png);}")
        self.hideButton.setText("")
        self.hideButton.setObjectName("hideButton")
        self.searchButton = QtWidgets.QPushButton(self.TopNav)
        self.searchButton.setGeometry(QtCore.QRect(445, 18, 25, 24))
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setStyleSheet("QPushButton#searchButton{\n"
"border-image: url(:/bg/search.png);}")
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")
        self.welcomeInfoLabel = QtWidgets.QLabel(self.TopNav)
        self.welcomeInfoLabel.setGeometry(QtCore.QRect(10, 18, 140, 24))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.welcomeInfoLabel.setFont(font)
        self.welcomeInfoLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.welcomeInfoLabel.setStyleSheet("QLabel#welcomeInfoLabel{color: rgb(252, 252, 252)}\n"
"QLabel#welcomeInfoLabel:hover{\n"
"    color: rgb(170, 255, 255)}")
        self.welcomeInfoLabel.setText("")
        self.welcomeInfoLabel.setObjectName("welcomeInfoLabel")
        self.line_8 = QtWidgets.QFrame(self.TopNav)
        self.line_8.setGeometry(QtCore.QRect(910, 15, 3, 30))
        self.line_8.setStyleSheet("\n"
"background-color: rgb(252, 239, 232);")
        self.line_8.setLineWidth(0)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.configButton = QtWidgets.QPushButton(self.TopNav)
        self.configButton.setGeometry(QtCore.QRect(870, 20, 20, 20))
        self.configButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configButton.setStyleSheet("QPushButton#hideButton{\n"
"    border-image: url(:/bg/hide.png);}\n"
"QPushButton#hideButton:hover{\n"
"    border-image: url(:/bg/hide_hover.png);}")
        self.configButton.setText("")
        self.configButton.setObjectName("configButton")
        self.Leftnav = QtWidgets.QWidget(self.centralwidget)
        self.Leftnav.setGeometry(QtCore.QRect(0, 60, 200, 610))
        self.Leftnav.setObjectName("Leftnav")
        self.PlaylistWidget = QtWidgets.QListWidget(self.Leftnav)
        self.PlaylistWidget.setGeometry(QtCore.QRect(0, 43, 200, 565))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.PlaylistWidget.setFont(font)
        self.PlaylistWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.PlaylistWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.PlaylistWidget.setToolTip("")
        self.PlaylistWidget.setStyleSheet("\n"
"QListWidget{background-color: rgb(252, 239, 232);color: rgb(112, 112, 112);outline:0px}\n"
"\n"
"QListWidget::item:selected:!active{\n"
"border-image: url(:/bg/item.png);color:black}\n"
"QListWidget::item:selected:active{\n"
"border-image: url(:/bg/item.png);color:black}\n"
"QListWidget::item:hover{text-indent:9px;\n"
"background-color: rgb(255, 242, 223);color:black}\n"
"\n"
"")
        self.PlaylistWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlaylistWidget.setLineWidth(0)
        self.PlaylistWidget.setAutoScroll(False)
        self.PlaylistWidget.setAutoScrollMargin(16)
        self.PlaylistWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.PlaylistWidget.setTabKeyNavigation(False)
        self.PlaylistWidget.setDragEnabled(True)
        self.PlaylistWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.PlaylistWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.PlaylistWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.PlaylistWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.PlaylistWidget.setMovement(QtWidgets.QListView.Static)
        self.PlaylistWidget.setProperty("isWrapping", False)
        self.PlaylistWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.PlaylistWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.PlaylistWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.PlaylistWidget.setUniformItemSizes(False)
        self.PlaylistWidget.setBatchSize(200)
        self.PlaylistWidget.setWordWrap(False)
        self.PlaylistWidget.setSelectionRectVisible(False)
        self.PlaylistWidget.setObjectName("PlaylistWidget")
        self.line_3 = QtWidgets.QFrame(self.Leftnav)
        self.line_3.setGeometry(QtCore.QRect(0, 40, 200, 2))
        self.line_3.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.newListButton = QtWidgets.QPushButton(self.Leftnav)
        self.newListButton.setGeometry(QtCore.QRect(165, 10, 25, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.newListButton.setFont(font)
        self.newListButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newListButton.setStyleSheet("QPushButton#newListButton:hover{\n"
"    border-image: url(:/bg/add_hover.png);}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-image: url(:/bg/add.png);\n"
"color:#75878a;\n"
"    border:0px;\n"
"}")
        self.newListButton.setText("")
        self.newListButton.setFlat(True)
        self.newListButton.setObjectName("newListButton")
        self.toListButton = QtWidgets.QPushButton(self.Leftnav)
        self.toListButton.setGeometry(QtCore.QRect(0, 3, 90, 37))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.toListButton.setFont(font)
        self.toListButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toListButton.setStyleSheet("color:#75878a;\n"
"border:0px;")
        self.toListButton.setObjectName("toListButton")
        self.moveUpButton = QtWidgets.QPushButton(self.Leftnav)
        self.moveUpButton.setGeometry(QtCore.QRect(130, 10, 25, 25))
        self.moveUpButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.moveUpButton.setStyleSheet("QPushButton:hover{\n"
"    border-image: url(:/bg/moveup_hover.png);;}\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"    \n"
"    border-image: url(:/bg/moveup.png);\n"
"color:#75878a;\n"
"    border:0px;\n"
"}")
        self.moveUpButton.setText("")
        self.moveUpButton.setObjectName("moveUpButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(200, 60, 1, 610))
        self.line.setStyleSheet("\n"
"background-color: rgb(228, 198, 208);")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(201, 60, 800, 230))
        self.widget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.widget.setObjectName("widget")
        self.picLabel = QtWidgets.QLabel(self.widget)
        self.picLabel.setGeometry(QtCore.QRect(37, 28, 140, 140))
        self.picLabel.setText("")
        self.picLabel.setObjectName("picLabel")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 60, 30))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(228, 198, 208);\n"
"border-radius:6px;\n"
"color:#f47983")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ListNameLabel = QtWidgets.QLabel(self.widget)
        self.ListNameLabel.setGeometry(QtCore.QRect(290, 20, 280, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.ListNameLabel.setFont(font)
        self.ListNameLabel.setObjectName("ListNameLabel")
        self.PlayAllButton = QtWidgets.QPushButton(self.widget)
        self.PlayAllButton.setGeometry(QtCore.QRect(330, 140, 90, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.PlayAllButton.setFont(font)
        self.PlayAllButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PlayAllButton.setStyleSheet("QPushButton\n"
"{\n"
"    border:0px;\n"
"}")
        self.PlayAllButton.setFlat(False)
        self.PlayAllButton.setObjectName("PlayAllButton")
        self.editListButton = QtWidgets.QPushButton(self.widget)
        self.editListButton.setGeometry(QtCore.QRect(220, 140, 90, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.editListButton.setFont(font)
        self.editListButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editListButton.setStyleSheet("\n"
"QPushButton{\n"
"    background-color:#fff2df;\n"
"    border-radius:4px;\n"
"    border:0px;\n"
"\n"
"}\n"
"QPushButton#editListButton:hover{\n"
"    color: rgb(249, 144, 111);}")
        self.editListButton.setFlat(True)
        self.editListButton.setObjectName("editListButton")
        self.delListButton = QtWidgets.QPushButton(self.widget)
        self.delListButton.setGeometry(QtCore.QRect(720, 180, 60, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.delListButton.setFont(font)
        self.delListButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delListButton.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:5px;\n"
"background-color:#e4c6d0;\n"
"    border:0px;\n"
"}QPushButton#delListButton:hover{\n"
"    color: rgb(249, 144, 111);}")
        self.delListButton.setObjectName("delListButton")
        self.descriptionEidt = QtWidgets.QLineEdit(self.widget)
        self.descriptionEidt.setEnabled(False)
        self.descriptionEidt.setGeometry(QtCore.QRect(220, 60, 520, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.descriptionEidt.setFont(font)
        self.descriptionEidt.setMouseTracking(False)
        self.descriptionEidt.setStyleSheet("color:#75878a;")
        self.descriptionEidt.setMaxLength(40)
        self.descriptionEidt.setFrame(False)
        self.descriptionEidt.setObjectName("descriptionEidt")
        self.heartLabel = QtWidgets.QLabel(self.widget)
        self.heartLabel.setGeometry(QtCore.QRect(730, 20, 45, 45))
        self.heartLabel.setStyleSheet("border-image: url(:/bg/love.png);")
        self.heartLabel.setText("")
        self.heartLabel.setObjectName("heartLabel")
        self.timesLabel = QtWidgets.QLabel(self.widget)
        self.timesLabel.setGeometry(QtCore.QRect(220, 95, 500, 25))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.timesLabel.setFont(font)
        self.timesLabel.setStyleSheet("color:#75878a;")
        self.timesLabel.setText("")
        self.timesLabel.setObjectName("timesLabel")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(30, 15, 154, 3))
        self.line_4.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(QtCore.QRect(30, 177, 154, 3))
        self.line_5.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(29, 15, 3, 164))
        self.line_6.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_6.setLineWidth(0)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setGeometry(QtCore.QRect(183, 15, 3, 164))
        self.line_7.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_7.setLineWidth(0)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 290, 760, 2))
        self.line_2.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.itemWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.itemWidget.setGeometry(QtCore.QRect(202, 300, 800, 370))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.itemWidget.setFont(font)
        self.itemWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.itemWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.itemWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.itemWidget.setTabKeyNavigation(True)
        self.itemWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.itemWidget.setObjectName("itemWidget")
        self.itemWidget.setColumnCount(0)
        self.itemWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PlayButton.setToolTip(_translate("MainWindow", "Let\'s start"))
        self.cTimeLabel.setText(_translate("MainWindow", "00:00"))
        self.eTimeLabel.setText(_translate("MainWindow", "00:00"))
        self.lyricButton.setText(_translate("MainWindow", "PushButton"))
        self.orderButton.setText(_translate("MainWindow", "show"))
        self.SearchEdit.setPlaceholderText(_translate("MainWindow", "搜索歌曲，用户，歌单"))
        self.exitButton.setToolTip(_translate("MainWindow", "Quit"))
        self.hideButton.setToolTip(_translate("MainWindow", "hide"))
        self.searchButton.setToolTip(_translate("MainWindow", "Press Enter"))
        self.configButton.setToolTip(_translate("MainWindow", "hide"))
        self.newListButton.setToolTip(_translate("MainWindow", "新建"))
        self.toListButton.setToolTip(_translate("MainWindow", "单击转到本地歌曲/我的歌单 "))
        self.toListButton.setText(_translate("MainWindow", "我的歌单"))
        self.moveUpButton.setToolTip(_translate("MainWindow", "上移"))
        self.label_2.setText(_translate("MainWindow", "歌单"))
        self.ListNameLabel.setText(_translate("MainWindow", "这是一个好听的歌单名字"))
        self.PlayAllButton.setText(_translate("MainWindow", "全部播放"))
        self.editListButton.setText(_translate("MainWindow", "修改简介"))
        self.delListButton.setText(_translate("MainWindow", "删除"))
        self.descriptionEidt.setText(_translate("MainWindow", "歌单简介：通过修改简介按钮来修改公开的歌单简介"))

import static.bgsrc_rc