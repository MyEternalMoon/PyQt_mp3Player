from ui.playListwidget import Ui_Form
from PyQt5 import Qt,QtWidgets,QtCore
from functions.getMp3 import *
import pygame
pattern = "%-25s%-20s%5s"
class playListWidget(Ui_Form,QtWidgets.QWidget):


    def __init__(self,parent = None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.playing = 0
        self.index = 0
        self.parent = parent
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.music = []

        pygame.mixer.init()
        self.musicpath = []
        self.updateInterface()
        self.parent.PlayButton.clicked.connect(self.playit)
        self.parent.NextButton.clicked.connect(self.letsPlay)
        self.listWidget.itemDoubleClicked.connect(self.playfromlist)
        self.listWidget.takeItem(0)


    def playfromlist(self):
        self.index = self.listWidget.currentRow()
        self.letsPlay()

    def updateInterface(self):
        self.label_3.setText("播放列表:(共%d首)"%len(self.music))
        for i in self.music:
            self.listWidget.addItem(pattern%(i.name.strip(),i.artist.strip(),getFormattedTime(i.length)))

    def letsPlay(self):

        self.listWidget.setCurrentRow(self.index)
        if self.index == len(self.music):
            return
        self.timerA = QtCore.QTimer(self)
        self.timerA.timeout.connect(self.letsPlay)
        self.timerA.start(self.music[self.index].length*1000+1000)
        # 自动播放下一首呵呵
        pygame.mixer.music.load(self.music[self.index].path)
        pygame.mixer.music.play()
        self.n = float("%.1f" % pygame.mixer.music.get_volume())

        self.playing = 1
        self.parent.PlayButton.setStyleSheet(
            "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
            "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
        self.index += 1

    def playit(self):
        if self.listWidget.currentRow() != -1:
            if self.playing == 1:
                self.parent.PlayButton.setStyleSheet(
                    "QPushButton#PlayButton{border-image: url(:/bg/play.png);}"
                    "QPushButton#PlayButton:hover{border-image: url(:/bg/play_hover.png);}")
                self.t = QtCore.QTimer()
                self.t.setInterval(60)
                self.t.timeout.connect(self.go)
                self.t.start()
                self.playing = 2
            elif self.playing == 2:
                self.n = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(1)
                self.parent.PlayButton.setStyleSheet(
                    "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
                    "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
                self.playing = 1
                pygame.mixer.music.unpause()
            else:
                self.parent.PlayButton.setStyleSheet(
                    "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
                    "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
                self.playing = 1
                pygame.mixer.music.play()


    def addNews(self, musicName):
        self.music = []
        """
        当双击的时候就把list里边后边的歌都加入playList里面，也可以一首一首加，用后面的方法
        一旦使用addNews，就把播放列表全部更新，并立刻播放
        :param musicName:
        :param musicPath:
        :return:
        """
        self.music = musicName[:]
        self.updateInterface()
        self.letsPlay()

    def go(self):
        '''定时器行为'''
        if self.n <= 0:
            pygame.mixer.music.pause()
            self.t.stop()
            self.n = 1.0
        else:
            self.n -= 0.05
            pygame.mixer.music.set_volume(self.n)

    def focusOutEvent(self, QFocusEvent):
        self.parent.listShowing = False
        self.hide()
        self.parent.orderButton.show()


