from ui.Main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from functions import Configs, ListOperation
from widgets import NewListDialog,sureDialog,musicWidget,configDialog,playListDialog
from functions import getMp3
import os


class PlayerMainWinodw(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        super(QtWidgets.QMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.flag = False
        self.LM = True
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.currentIndex = None
        self.user = ""
        self.listShowing = False

        self.playing = False
        self.MyList = ListOperation.loadList()
        self.musicStorage = "."
        self.MyMusic = []
        self.ConfigInfo = {}
        self.pSlider = playListDialog.MyPSlider(Qt.Qt.Horizontal, self)
        self.pSlider.resize(200, 20)
        self.pSlider.move(90, 700)
        self.vSlider = playListDialog.MySlider(Qt.Qt.Horizontal, self)
        self.vSlider.move(670, 700)
        self.pl = playListDialog.playListWidget(self)
        self.pl.move(500, 262)
        self.pl.hide()
        self.vSlider.valueChanged[int].connect(self.pl.changeVolume)
        self.MusicWidget = musicWidget.MusicWidget(self)
        self.MusicWidget.move(0,103)
        self.MusicWidget.hide()


        # connect slot with signal
        self.exitButton.clicked.connect(self.close)
        self.hideButton.clicked.connect(self.showMinimized)
        self.picLabel.setScaledContents(True)
        self.editListButton.hide()
        self.PlayAllButton.hide()
        self.toListButton.setToolTip("点击切换我的歌单/所有本地歌曲")
        # Initialize some information
        self.initConfigs()
        self.initMusicList()
        self.initInterfaceInfo()
        self.timesLabel.setText("播放次数：unKnown")
        self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
        # self.PlayButton.clicked.connect(self.playMusic)
        self.newListButton.clicked.connect(self.createNewList)
        #self.PlayAllButton.clicked.connect(self.playMusic)
        self.PlaylistWidget.currentItemChanged.connect(self.updateInterface)
        self.delListButton.clicked.connect(self.deleteList)
        self.editListButton.clicked.connect(self.desChange)
        self.toListButton.clicked.connect(self.toMusic)
        self.moveUpButton.clicked.connect(self.moveUp)
        self.configButton.clicked.connect(self.editConfig)
        self.descriptionEidt.installEventFilter(self)
        self.orderButton.clicked.connect(self.showList)
        self.NextButton.clicked.connect(self.pl.playnext)
        self.FormerButton.clicked.connect(self.pl.playformer)


    def set(self,v):
        """
        调整歌曲播放进度
        :param int:
        :return:
        """
        pass

    def showList(self):
        if self.listShowing:
            pass
        else:
            self.orderButton.hide()

            self.pl.show()
            self.listShowing = True
            self.pl.setFocus()
            self.orderButton.setCheckable(False)

    def editConfig(self):
        f = configDialog.configWidget(self)
        f.move(300,100)
        f.show()

    def moveUp(self):
        if self.currentIndex is None or self.currentIndex == 0:
            pass
        else:
            ListOperation.moveUp(self.MyList,self.currentIndex)
            if len(self.MyList[self.currentIndex].name) >= 9:
                self.PlaylistWidget.item(self.currentIndex).setText(
                    self.MyList[self.currentIndex].name[0:8] + "...")
            else:
                self.PlaylistWidget.item(self.currentIndex).setText(
                    self.MyList[self.currentIndex].name)
            self.PlaylistWidget.item(self.currentIndex).setToolTip(self.MyList[self.currentIndex].name)

            if len(self.MyList[self.currentIndex-1].name) >= 9:
                self.PlaylistWidget.item(self.currentIndex - 1).setText(
                    self.MyList[self.currentIndex - 1].name[0:8]+"...")
            else:
                self.PlaylistWidget.item(self.currentIndex - 1).setText(self.MyList[self.currentIndex - 1].name)
            self.PlaylistWidget.item(self.currentIndex-1).setToolTip(self.MyList[self.currentIndex-1].name)
            #self.PlaylistWidget.takeItem(self.currentIndex)
            self.PlaylistWidget.setCurrentRow(self.currentIndex-1)
            self.updateInterface()

    def toMusic(self):
        if self.LM:
            self.LM = False
            self.MusicWidget.show()
            self.toListButton.setText("本地音乐")
            self.newListButton.hide()
            self.widget.hide()
        else:
            self.LM = True
            self.MusicWidget.hide()
            self.toListButton.setText("我的歌单")
            self.newListButton.show()
            self.widget.show()

    def initConfigs(self):
        self.ConfigInfo = Configs.initconfig()
        self.musicStorage = self.ConfigInfo["musicStorage"]

    def initMusicList(self):
        raw_list = os.listdir(self.musicStorage)
        for i in raw_list:
            if i.endswith(".mp3"):
                self.MyMusic.append(i)

    def initInterfaceInfo(self):
        for i in range(len(self.MyList)):
            if len(self.MyList[i].name) >= 9:
                self.PlaylistWidget.addItem(self.MyList[i].name[0:8]+"...")
            else:
                self.PlaylistWidget.addItem(self.MyList[i].name)
            p = self.PlaylistWidget.item(i)
            p.setToolTip(self.MyList[i].name)


        if self.ConfigInfo["userName"] == "Administrator":
            self.welcomeInfoLabel.setText("欢迎，请登录！")
        else:
            if len(self.ConfigInfo["userName"]) > 9:
                self.welcomeInfoLabel.setText("欢迎！"+self.ConfigInfo["userName"][0:8]+"...")
            else:
                self.welcomeInfoLabel.setText("欢迎！"+self.ConfigInfo["userName"])
            self.welcomeInfoLabel.setToolTip(self.ConfigInfo["userName"])


    def updateList(self):
        self.PlaylistWidget.clear()
        for i in range(len(self.MyList)):
            if len(self.MyList[i].name) >= 9:
                self.PlaylistWidget.addItem(self.MyList[i].name[0:8]+"..")
            else:
                self.PlaylistWidget.addItem(self.MyList[i].name)
            p = self.PlaylistWidget.item(i)
            p.setToolTip(self.MyList[i].name)

    def createNewList(self):
        if NewListDialog.listDialog(self).exec_():
            self.updateList()
            self.PlaylistWidget.setCurrentRow(self.PlaylistWidget.count()-1)
            self.updateInterface()

    def updateInterface(self):
        self.currentIndex = self.PlaylistWidget.currentRow()
        if self.currentIndex is None:
            self.editListButton.clicked.connect(self.desChange)
            self.descriptionEidt.setFrame(False)
            self.descriptionEidt.setStyleSheet("color:#75878a;")
            self.editListButton.setEnabled(True)
            self.timesLabel.setText("播放次数：unKnown")
            self.editListButton.hide()
            self.PlayAllButton.hide()
        else:
            self.ListNameLabel.setText(self.MyList[self.currentIndex].name)
            self.descriptionEidt.setText(self.MyList[self.currentIndex].description)
            self.timesLabel.setText("播放次数：%d"%self.MyList[self.currentIndex].times)
            self.editListButton.show()
            self.PlayAllButton.show()
            if self.MyList[self.currentIndex].picPath is not None:
                if os.path.isfile(self.MyList[self.currentIndex].picPath):
                    self.picLabel.setPixmap(QtGui.QPixmap(self.MyList[self.currentIndex].picPath))
                else:
                    self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
            else:
                self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))

    def deleteList(self):
        if self.currentIndex is None:
            pass
        else:
            self.sure = sureDialog.sureDialog(self.MyList[self.currentIndex].name,self)
            if self.sure.exec_():
                try:
                    os.remove(self.MyList[self.currentIndex].picPath)
                except:
                    pass
                ListOperation.deleteList(self.currentIndex, self.MyList)
                self.currentIndex = None
                self.ListNameLabel.setText("")
                self.descriptionEidt.setText("")
                self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
                self.updateList()


    def desChange(self):
        if self.currentIndex is None:
            pass
        # elif self.descriptionEidt.isEnabled():
        #     pass
        else:
            self.descriptionEidt.setReadOnly(False)
            self.editListButton.setEnabled(False)
            self.descriptionEidt.setEnabled(True)
            self.descriptionEidt.setFrame(True)
            self.descriptionEidt.setStyleSheet("background-color:white;")
            self.descriptionEidt.setFocus()

    # def playMusic(self):
    #     if self.currentIndex is None:
    #         return
    #     if self.playing:
    #         self.PlayButton.setStyleSheet(
    #             "QPushButton#PlayButton{border-image: url(:/bg/play.png);}"
    #             "QPushButton#PlayButton:hover{border-image: url(:/bg/play_hover.png);}")
    #         self.playing = False
    #     else:
    #         self.PlayButton.setStyleSheet(
    #             "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
    #             "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
    #         self.playing = True
          #  self.MyList[self.currentIndex].times += 1
          #  self.updateInterface()

    def eventFilter(self, obj, event):
        if self.descriptionEidt.isEnabled() == True:
            if obj == self.descriptionEidt:
                if event.type() == QtCore.QEvent.FocusOut:
                    self.MyList[self.currentIndex].ChangeDescription(self.descriptionEidt.text())
                    ListOperation.pureSave(self.MyList)
                    self.descriptionEidt.setEnabled(False)
                    self.descriptionEidt.setFrame(False)
                    self.descriptionEidt.setStyleSheet("color:#75878a;")
                    self.editListButton.setEnabled(True)
                    self.descriptionEidt.setReadOnly(True)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def mouseMoveEvent(self, event):
        if self.flag == True:
            self.move(Qt.QPoint(self.pos() + event.pos() - self.currentPos))
            self.setCursor(Qt.QCursor(Qt.Qt.ClosedHandCursor))

    def mouseReleaseEvent(self,event):
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))
        self.flag = False

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if event.buttons() == QtCore.Qt.LeftButton and 0 < y < 60:
            self.currentPos = event.pos()
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))
            self.flag = True

    def closeEvent(self, event):
        """Save configs when you quit"""
        Configs.saveConfig(self.ConfigInfo)
        ListOperation.pureSave(self.MyList)

    # def drawShadow(self, painter):
    #     # 绘制左上角、左下角、右上角、右下角、上、下、左、右边框
    #     self.pixmaps = list()
    #     self.pixmaps.append(("./src/left_top.jpg"))
    #     self.pixmaps.append(("./src/left_bottom.jpg"))
    #     self.pixmaps.append(("./src/right_top.jpg"))
    #     self.pixmaps.append(("./src/right_bottom.jpg"))
    #     self.pixmaps.append(("./src/top_mid.jpg"))
    #     self.pixmaps.append(str("./src/bottom_mid.jpg"))
    #     self.pixmaps.append(("./src/left_mid.png"))
    #     self.pixmaps.append(("./src/right_mid.png"))
    #     painter.drawPixmap(0, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[0]))  # 左上角
    #     painter.drawPixmap(self.width() - self.SHADOW_WIDTH, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
    #                        QPixmap(self.pixmaps[2]))  # 右上角
    #     painter.drawPixmap(0, self.height() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
    #                        QPixmap(self.pixmaps[1]))  # 左下角
    #     painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH, self.SHADOW_WIDTH,
    #                        self.SHADOW_WIDTH, QPixmap(self.pixmaps[3]))  # 右下角
    #     painter.drawPixmap(0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height() - 2 * self.SHADOW_WIDTH,
    #                        QPixmap(self.pixmaps[6]).scaled(self.SHADOW_WIDTH,
    #                                                        self.height() - 2 * self.SHADOW_WIDTH))  # 左
    #     painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
    #                        self.height() - 2 * self.SHADOW_WIDTH, QPixmap(self.pixmaps[7]).scaled(self.SHADOW_WIDTH,
    #                                                                                               self.height() - 2 * self.SHADOW_WIDTH))  # 右
    #     painter.drawPixmap(self.SHADOW_WIDTH, 0, self.width() - 2 * self.SHADOW_WIDTH, self.SHADOW_WIDTH,
    #                        QPixmap(self.pixmaps[4]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
    #                                                        self.SHADOW_WIDTH))  # 上
    #     painter.drawPixmap(self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH, self.width() - 2 * self.SHADOW_WIDTH,
    #                        self.SHADOW_WIDTH, QPixmap(self.pixmaps[5]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
    #                                                                           self.SHADOW_WIDTH))  # 下
    #
    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     self.drawShadow(painter)
    #     painter.setPen(Qt.Qt.NoPen)
    #     #painter.setBrush(Qt.Qt.white)
    #     painter.drawRect(QRect(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width() - 2 * self.SHADOW_WIDTH,
    #                            self.height() - 2 * self.SHADOW_WIDTH))




