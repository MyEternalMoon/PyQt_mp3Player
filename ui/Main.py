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
        MainWindow.resize(1100, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bg/heart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"background-color: rgb(252, 239, 232);")
        self.centralwidget.setObjectName("centralwidget")
        self.LowerNav = QtWidgets.QWidget(self.centralwidget)
        self.LowerNav.setGeometry(QtCore.QRect(0, 720, 1101, 80))
        self.LowerNav.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LowerNav.setStyleSheet("\n"
"background-color: #edd1d8;")
        self.LowerNav.setObjectName("LowerNav")
        self.PlayButton = QtWidgets.QPushButton(self.LowerNav)
        self.PlayButton.setGeometry(QtCore.QRect(520, 10, 60, 60))
        self.PlayButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PlayButton.setStyleSheet("QPushButton#PlayButton{border-image: url(:/bg/play.png);}\n"
"\n"
"QPushButton#PlayButton:hover{\n"
"border-image: url(:/bg/play_hover.png);}")
        self.PlayButton.setText("")
        self.PlayButton.setFlat(False)
        self.PlayButton.setObjectName("PlayButton")
        self.cTimeLabel = QtWidgets.QLabel(self.LowerNav)
        self.cTimeLabel.setGeometry(QtCore.QRect(30, 30, 50, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cTimeLabel.setFont(font)
        self.cTimeLabel.setToolTipDuration(-2)
        self.cTimeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.cTimeLabel.setObjectName("cTimeLabel")
        self.eTimeLabel = QtWidgets.QLabel(self.LowerNav)
        self.eTimeLabel.setGeometry(QtCore.QRect(330, 30, 50, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.eTimeLabel.setFont(font)
        self.eTimeLabel.setToolTipDuration(-2)
        self.eTimeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.eTimeLabel.setObjectName("eTimeLabel")
        self.FormerButton = QtWidgets.QPushButton(self.LowerNav)
        self.FormerButton.setGeometry(QtCore.QRect(460, 20, 40, 40))
        self.FormerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FormerButton.setStyleSheet("QPushButton#FormerButton{border-image: url(:/bg/former.png)}\n"
"QPushButton#FormerButton:hover{\n"
"    border-image: url(:/bg/former_hover.png)}")
        self.FormerButton.setText("")
        self.FormerButton.setObjectName("FormerButton")
        self.NextButton = QtWidgets.QPushButton(self.LowerNav)
        self.NextButton.setGeometry(QtCore.QRect(610, 20, 40, 40))
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setStyleSheet("QPushButton#NextButton{border-image: url(:/bg/next.png)}\n"
"QPushButton#NextButton:hover{\n"
"    border-image: url(:/bg/next_hover.png)}")
        self.NextButton.setText("")
        self.NextButton.setObjectName("NextButton")
        self.SoundButton = QtWidgets.QPushButton(self.LowerNav)
        self.SoundButton.setGeometry(QtCore.QRect(710, 30, 28, 28))
        self.SoundButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SoundButton.setStyleSheet("border-image: url(:/buttons/sound_on.png);")
        self.SoundButton.setText("")
        self.SoundButton.setObjectName("SoundButton")
        self.lyricButton = QtWidgets.QPushButton(self.LowerNav)
        self.lyricButton.setGeometry(QtCore.QRect(870, 30, 25, 25))
        self.lyricButton.setText("")
        self.lyricButton.setFlat(True)
        self.lyricButton.setObjectName("lyricButton")
        self.showListButton = QtWidgets.QPushButton(self.LowerNav)
        self.showListButton.setGeometry(QtCore.QRect(1020, 30, 28, 28))
        self.showListButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showListButton.setStyleSheet("border-image: url(:/bg/list.png);")
        self.showListButton.setText("")
        self.showListButton.setObjectName("showListButton")
        self.line_9 = QtWidgets.QFrame(self.LowerNav)
        self.line_9.setGeometry(QtCore.QRect(0, 0, 1100, 4))
        self.line_9.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_9.setLineWidth(0)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.line_12 = QtWidgets.QFrame(self.LowerNav)
        self.line_12.setGeometry(QtCore.QRect(0, 76, 1100, 4))
        self.line_12.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_12.setLineWidth(0)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.playOrderButton = QtWidgets.QPushButton(self.LowerNav)
        self.playOrderButton.setGeometry(QtCore.QRect(970, 30, 30, 30))
        self.playOrderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playOrderButton.setToolTip("")
        self.playOrderButton.setStyleSheet("border-image: url(:/order/ordered_order.png);")
        self.playOrderButton.setText("")
        self.playOrderButton.setObjectName("playOrderButton")
        self.TopNav = QtWidgets.QWidget(self.centralwidget)
        self.TopNav.setGeometry(QtCore.QRect(0, 0, 1101, 60))
        self.TopNav.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.TopNav.setStyleSheet("\n"
"background-color: #edd1d8;")
        self.TopNav.setObjectName("TopNav")
        self.SearchEdit = QtWidgets.QLineEdit(self.TopNav)
        self.SearchEdit.setGeometry(QtCore.QRect(190, 18, 265, 24))
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
        self.exitButton.setGeometry(QtCore.QRect(1050, 20, 20, 20))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("QPushButton#exitButton{border-image: url(:/bg/exit.png);}\n"
"QPushButton#exitButton:hover{\n"
"    border-image: url(:/bg/exit_hover.png);}")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        self.hideButton = QtWidgets.QPushButton(self.TopNav)
        self.hideButton.setGeometry(QtCore.QRect(1020, 20, 20, 20))
        self.hideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hideButton.setStyleSheet("QPushButton#hideButton{\n"
"    border-image: url(:/bg/hide.png);}\n"
"QPushButton#hideButton:hover{\n"
"    border-image: url(:/bg/hide_hover.png);}")
        self.hideButton.setText("")
        self.hideButton.setObjectName("hideButton")
        self.searchButton = QtWidgets.QPushButton(self.TopNav)
        self.searchButton.setGeometry(QtCore.QRect(450, 18, 25, 24))
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
        self.line_8.setGeometry(QtCore.QRect(1000, 15, 3, 30))
        self.line_8.setStyleSheet("\n"
"background-color: rgb(252, 239, 232);")
        self.line_8.setLineWidth(0)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.configButton = QtWidgets.QPushButton(self.TopNav)
        self.configButton.setGeometry(QtCore.QRect(960, 20, 20, 20))
        self.configButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configButton.setStyleSheet("QPushButton{\n"
"    border-image: url(:/bg/config.png);;}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/bg/config_hover.png);}")
        self.configButton.setText("")
        self.configButton.setObjectName("configButton")
        self.line_10 = QtWidgets.QFrame(self.TopNav)
        self.line_10.setGeometry(QtCore.QRect(0, 56, 1100, 4))
        self.line_10.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_10.setLineWidth(0)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.TopNav)
        self.line_11.setGeometry(QtCore.QRect(0, 0, 1100, 4))
        self.line_11.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_11.setLineWidth(0)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.Leftnav = QtWidgets.QWidget(self.centralwidget)
        self.Leftnav.setGeometry(QtCore.QRect(0, 60, 200, 659))
        self.Leftnav.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Leftnav.setObjectName("Leftnav")
        self.PlaylistWidget = QtWidgets.QListWidget(self.Leftnav)
        self.PlaylistWidget.setGeometry(QtCore.QRect(0, 38, 200, 260))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.PlaylistWidget.setFont(font)
        self.PlaylistWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.PlaylistWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.PlaylistWidget.setToolTip("")
        self.PlaylistWidget.setStyleSheet("\n"
"QListWidget QScrollBar:vertical{width:8px;}\n"
"QListWidget{;background-color: rgb(252, 239, 232);color: rgb(112, 112, 112);alternate-background-color: rgb(248, 235, 230);outline:0px;}\n"
"QListWidget::item:selected:!active{\n"
"border-image: url(:/bg/item.png);color:black}\n"
"QListWidget::item:selected:active{\n"
"border-image: url(:/bg/item.png);color:black}\n"
"QListWidget::item:hover{text-indent:9px;\n"
"background-color: rgb(255, 242, 223);color:black}\n"
"\n"
"\n"
"\n"
"")
        self.PlaylistWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlaylistWidget.setLineWidth(0)
        self.PlaylistWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.PlaylistWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.PlaylistWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.PlaylistWidget.setAutoScroll(True)
        self.PlaylistWidget.setAutoScrollMargin(16)
        self.PlaylistWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.PlaylistWidget.setTabKeyNavigation(False)
        self.PlaylistWidget.setDragEnabled(True)
        self.PlaylistWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.PlaylistWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.PlaylistWidget.setAlternatingRowColors(True)
        self.PlaylistWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.PlaylistWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
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
        self.line_3.setGeometry(QtCore.QRect(0, 35, 200, 2))
        self.line_3.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.newListButton = QtWidgets.QPushButton(self.Leftnav)
        self.newListButton.setGeometry(QtCore.QRect(168, 10, 22, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.newListButton.setFont(font)
        self.newListButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newListButton.setStyleSheet("QPushButton#newListButton:hover{\n"
"    border-image: url(:/bg/add_hover.png);}\n"
"\n"
"QPushButton\n"
"{background:\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.06 rgb(255, 242, 223), stop:1 rgb(228, 198, 208,50));\n"
"    border-image: url(:/bg/add.png);\n"
"color:#75878a;\n"
"    border:0px;\n"
"}")
        self.newListButton.setText("")
        self.newListButton.setFlat(True)
        self.newListButton.setObjectName("newListButton")
        self.toListButton = QtWidgets.QPushButton(self.Leftnav)
        self.toListButton.setGeometry(QtCore.QRect(0, 0, 90, 35))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.toListButton.setFont(font)
        self.toListButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toListButton.setToolTip("")
        self.toListButton.setStyleSheet("color:#75878a;\n"
"border:0px;\n"
"background:\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.06 rgb(255, 242, 223), stop:1 rgb(228, 198, 208,50));")
        self.toListButton.setObjectName("toListButton")
        self.moveUpButton = QtWidgets.QPushButton(self.Leftnav)
        self.moveUpButton.setGeometry(QtCore.QRect(140, 10, 22, 22))
        self.moveUpButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.moveUpButton.setStyleSheet("QPushButton:hover{\n"
"    border-image: url(:/bg/moveup_hover.png);;}\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"    background:\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.06 rgb(255, 242, 223), stop:1 rgb(228, 198, 208,50));\n"
"    border-image: url(:/bg/moveup.png);\n"
"color:#75878a;\n"
"    border:0px;\n"
"}")
        self.moveUpButton.setText("")
        self.moveUpButton.setObjectName("moveUpButton")
        self.toListButton_2 = QtWidgets.QPushButton(self.Leftnav)
        self.toListButton_2.setGeometry(QtCore.QRect(0, 300, 90, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.toListButton_2.setFont(font)
        self.toListButton_2.setToolTip("")
        self.toListButton_2.setStyleSheet("color:#75878a;\n"
"border:0px;\n"
"background:\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.06 rgb(255, 242, 223), stop:1 rgb(228, 198, 208,50));")
        self.toListButton_2.setObjectName("toListButton_2")
        self.line_13 = QtWidgets.QFrame(self.Leftnav)
        self.line_13.setGeometry(QtCore.QRect(0, 300, 200, 2))
        self.line_13.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_13.setLineWidth(0)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.Leftnav)
        self.line_14.setGeometry(QtCore.QRect(0, 330, 200, 2))
        self.line_14.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_14.setLineWidth(0)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.label = QtWidgets.QLabel(self.Leftnav)
        self.label.setGeometry(QtCore.QRect(0, 300, 201, 32))
        self.label.setStyleSheet("background:\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.06 rgb(255, 242, 223), stop:1 rgb(228, 198, 208,50));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Leftnav)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 201, 35))
        self.label_3.setStyleSheet("background:\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.06 rgb(255, 242, 223), stop:1 rgb(228, 198, 208,50));")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.refreshButton = QtWidgets.QPushButton(self.Leftnav)
        self.refreshButton.setGeometry(QtCore.QRect(170, 306, 21, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.refreshButton.setFont(font)
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshButton.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    border-image: url(:/buttons/refresh.png);\n"
"\n"
"color:#75878a;\n"
"    border:0px;\n"
"}")
        self.refreshButton.setText("")
        self.refreshButton.setFlat(True)
        self.refreshButton.setObjectName("refreshButton")
        self.label_3.raise_()
        self.label.raise_()
        self.PlaylistWidget.raise_()
        self.line_3.raise_()
        self.newListButton.raise_()
        self.toListButton.raise_()
        self.moveUpButton.raise_()
        self.toListButton_2.raise_()
        self.line_13.raise_()
        self.line_14.raise_()
        self.refreshButton.raise_()
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(200, 65, 2, 650))
        self.line.setStyleSheet("\n"
"background-color: rgb(228, 198, 208);")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(201, 60, 900, 258))
        self.widget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.widget.setObjectName("widget")
        self.picLabel = QtWidgets.QLabel(self.widget)
        self.picLabel.setGeometry(QtCore.QRect(37, 50, 140, 140))
        self.picLabel.setText("")
        self.picLabel.setObjectName("picLabel")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(230, 35, 60, 30))
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
        self.ListNameLabel.setGeometry(QtCore.QRect(300, 35, 280, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.ListNameLabel.setFont(font)
        self.ListNameLabel.setObjectName("ListNameLabel")
        self.PlayAllButton = QtWidgets.QPushButton(self.widget)
        self.PlayAllButton.setGeometry(QtCore.QRect(350, 155, 90, 25))
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
        self.editListButton.setGeometry(QtCore.QRect(240, 155, 90, 25))
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
        self.delListButton.setGeometry(QtCore.QRect(790, 195, 60, 30))
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
        self.descriptionEidt.setGeometry(QtCore.QRect(230, 75, 550, 30))
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
        self.heartLabel.setGeometry(QtCore.QRect(800, 35, 45, 45))
        self.heartLabel.setStyleSheet("border-image: url(:/bg/love.png);")
        self.heartLabel.setText("")
        self.heartLabel.setObjectName("heartLabel")
        self.timesLabel = QtWidgets.QLabel(self.widget)
        self.timesLabel.setGeometry(QtCore.QRect(230, 115, 500, 25))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        self.timesLabel.setFont(font)
        self.timesLabel.setStyleSheet("color:#75878a;")
        self.timesLabel.setText("")
        self.timesLabel.setObjectName("timesLabel")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(30, 37, 154, 3))
        self.line_4.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(QtCore.QRect(30, 199, 154, 3))
        self.line_5.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(29, 37, 3, 164))
        self.line_6.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_6.setLineWidth(0)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setGeometry(QtCore.QRect(183, 37, 3, 164))
        self.line_7.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_7.setLineWidth(0)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(200, 318, 900, 2))
        self.line_2.setStyleSheet("background-color: rgb(228, 198, 208);")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.listMusicWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.listMusicWidget.setGeometry(QtCore.QRect(202, 320, 897, 397))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.listMusicWidget.setFont(font)
        self.listMusicWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listMusicWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listMusicWidget.setToolTip("")
        self.listMusicWidget.setStyleSheet("QTableWidget\n"
"{\n"
"     border:none;    \n"
"    background-color: rgb(252, 239, 232);\n"
"    color:rgb(112, 112, 112);    /*前景色：文字颜色*/\n"
"    /*gridline-color:red;   */     /*表格中的网格线条颜色*/\n"
"\n"
"    border-color:rgba(245, 231, 236, 220); \n"
"    /*设置交替颜色，需要在函数属性中设置:tableWidget->setAlternatingRowColors(true)*/\n"
"    alternate-background-color:rgb(248, 235, 230);\n"
"    selection-color:black;    /*鼠标选中时前景色：文字颜色*/ \n"
"    selection-background-color:rgba(245, 231, 236, 220);   /*鼠标选中时背景色*/\n"
"\n"
"    /*border-radius:5px;*/\n"
"    /*表格与边框的间距*/\n"
"}\n"
"\n"
"/*设置表头属性*/\n"
"QTableWidget::item\n"
"{\n"
"    min-width: 106.75px;\n"
"    min-height: 50px;\n"
"}\n"
"QTableWidget QHeaderView::section\n"
"{\n"
"\n"
"    background-color: rgba(237, 209, 216, 200);/*qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.08 rgba(252, 239, 232, 255), stop:1 rgb(228, 198, 208,30));\n"
"    /*color:black;*/\n"
"    color:rgb(112,112,112);\n"
"   border:2px solid;\n"
"border-right:1px solid;\n"
"border-top:0;\n"
"border-left:0;\n"
"    border-color:rgb(228, 198, 208);\n"
"    height:27px;\n"
"    font-size:19px;\n"
"\n"
"font-family:\"微软雅黑\";\n"
"\n"
"    \n"
"}\n"
"")
        self.listMusicWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listMusicWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listMusicWidget.setLineWidth(1)
        self.listMusicWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listMusicWidget.setAutoScrollMargin(16)
        self.listMusicWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listMusicWidget.setTabKeyNavigation(False)
        self.listMusicWidget.setProperty("showDropIndicator", False)
        self.listMusicWidget.setDragDropOverwriteMode(False)
        self.listMusicWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listMusicWidget.setAlternatingRowColors(True)
        self.listMusicWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listMusicWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listMusicWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.listMusicWidget.setShowGrid(False)
        self.listMusicWidget.setGridStyle(QtCore.Qt.NoPen)
        self.listMusicWidget.setWordWrap(True)
        self.listMusicWidget.setCornerButtonEnabled(False)
        self.listMusicWidget.setRowCount(10)
        self.listMusicWidget.setColumnCount(4)
        self.listMusicWidget.setObjectName("listMusicWidget")
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listMusicWidget.setItem(1, 2, item)
        self.listMusicWidget.horizontalHeader().setVisible(True)
        self.listMusicWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.listMusicWidget.horizontalHeader().setDefaultSectionSize(288)
        self.listMusicWidget.horizontalHeader().setHighlightSections(False)
        self.listMusicWidget.horizontalHeader().setMinimumSectionSize(0)
        self.listMusicWidget.horizontalHeader().setStretchLastSection(True)
        self.listMusicWidget.verticalHeader().setVisible(False)
        self.listMusicWidget.verticalHeader().setCascadingSectionResizes(False)
        self.listMusicWidget.verticalHeader().setDefaultSectionSize(25)
        self.listMusicWidget.verticalHeader().setHighlightSections(False)
        self.listMusicWidget.verticalHeader().setMinimumSectionSize(0)
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(0, 0, 3, 800))
        self.line_15.setStyleSheet("\n"
"background-color: rgb(228, 198, 208);")
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setLineWidth(0)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(1097, 0, 3, 800))
        self.line_16.setStyleSheet("\n"
"background-color: rgb(228, 198, 208);")
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setLineWidth(0)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setObjectName("line_16")
        self.LowerNav.raise_()
        self.TopNav.raise_()
        self.Leftnav.raise_()
        self.widget.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.listMusicWidget.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PlayButton.setToolTip(_translate("MainWindow", "Let\'s start"))
        self.cTimeLabel.setText(_translate("MainWindow", "00:00"))
        self.eTimeLabel.setText(_translate("MainWindow", "00:00"))
        self.showListButton.setToolTip(_translate("MainWindow", "list"))
        self.SearchEdit.setPlaceholderText(_translate("MainWindow", "搜索歌曲，用户，歌单"))
        self.exitButton.setToolTip(_translate("MainWindow", "Quit"))
        self.hideButton.setToolTip(_translate("MainWindow", "hide"))
        self.searchButton.setToolTip(_translate("MainWindow", "Press Enter"))
        self.configButton.setToolTip(_translate("MainWindow", "hide"))
        self.newListButton.setToolTip(_translate("MainWindow", "新建列表"))
        self.toListButton.setText(_translate("MainWindow", "我的歌单"))
        self.moveUpButton.setToolTip(_translate("MainWindow", "上移"))
        self.toListButton_2.setText(_translate("MainWindow", "本地音乐"))
        self.refreshButton.setToolTip(_translate("MainWindow", "刷新"))
        self.label_2.setText(_translate("MainWindow", "歌单"))
        self.ListNameLabel.setText(_translate("MainWindow", "这是一个好听的歌单名字"))
        self.PlayAllButton.setText(_translate("MainWindow", "全部播放"))
        self.editListButton.setText(_translate("MainWindow", "修改简介"))
        self.delListButton.setText(_translate("MainWindow", "删除"))
        self.descriptionEidt.setText(_translate("MainWindow", "歌单简介：通过修改简介按钮来修改公开的歌单简介"))
        __sortingEnabled = self.listMusicWidget.isSortingEnabled()
        self.listMusicWidget.setSortingEnabled(False)
        self.listMusicWidget.setSortingEnabled(__sortingEnabled)

import static.bgsrc_rc
