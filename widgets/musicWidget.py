from PyQt5 import QtWidgets,QtGui,QtCore
from ui.musicWidget import Ui_Form
from functions import getMp3,MusicList
import pygame

class MusicWidget(QtWidgets.QWidget,Ui_Form):
    '''
    三个signal 先传给父窗口，再间接给子窗口pl
    '''
    deleteSingal = QtCore.pyqtSignal(MusicList.singleMusic)
    addToListSignal = QtCore.pyqtSignal(MusicList.singleMusic)
    addToPlaySignal = QtCore.pyqtSignal(MusicList.singleMusic)


    def __init__(self,parent=None,trueparent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.playing = 0 # 0 stopped, 1 playing, 2 paused
        self.parent = trueparent
        self.currentIndex = -1
        self.allMusic = getMp3.getMp3FromStore("./music/")
        for i in self.allMusic:
            self.listWidget.addItem(i.name)
        pygame.mixer.init()

        self.popMenu = QtWidgets.QMenu()
        P = QtWidgets.QAction('播放', self)
        N = QtWidgets.QAction('添加到下一首播放', self)
        D = QtWidgets.QAction('删除', self)
        self.popMenu.addAction(P)
        self.popMenu.addAction(N)
        self.popMenu.addAction(D)
        P.triggered.connect(self.addToPlay)
        N.triggered.connect(self.addToList)
        D.triggered.connect(self.deleteMusic)
       # self.parent.PlayButton.clicked.connect(self.playit)
       #  self.parent.FormerButton.clicked.connect(self.playformer)
       #  self.parent.NextButton.clicked.connect(self.playnext)
       #  self.listWidget.currentRowChanged.connect(self.changeMusic)
        self.listWidget.itemDoubleClicked.connect(self.playtolist)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested[QtCore.QPoint].connect(self.showContentMenu)
       # self.show()

    def updateInterface(self):
        self.listWidget.clear()
        for i in self.allmusic:
            self.listWidget.addItem(i.name)
        self.listWidget.setCurrentRow(-1)
        self.currentIndex = -1

    def showContentMenu(self,point):
        self.currentIndex = self.listWidget.currentRow()
        self.popMenu.exec_(QtGui.QCursor.pos())

    def deleteMusic(self):
        if self.currentIndex == -1:
            pass
        else:
            if getMp3.deleteMusic(self.allMusic[self.currentIndex]):
                self.deleteSingal.emit(self.allMusic[self.currentIndex])
                self.allMusic = getMp3.getMp3FromStore("./music/")
                self.updateInterface()

    def addToPlay(self):
        if self.currentIndex == -1:
            pass
        else:
            self.addToPlaySignal.emit(self.allMusic[self.currentIndex])

    def addToList(self):
        if self.currentIndex == -1:
            pass
        else:
            self.addToListSignal.emit(self.allMusic[self.currentIndex])
    # def playformer(self):
    #     if self.listWidget.currentRow() == 0 or self.listWidget.currentRow() == -1:
    #         pass
    #     else:
    #         self.listWidget.setCurrentRow(self.listWidget.currentRow()-1)
    #         #self.playit()
    #
    # def playnext(self):
    #     if self.listWidget.currentRow() == self.listWidget.count()-1 or self.listWidget.currentRow() == -1:
    #         pass
    #     else:
    #         self.listWidget.setCurrentRow(self.listWidget.currentRow()+1)
    #         #self.playit()

    # def changeMusic(self):
    #     pygame.mixer.music.load(self.allMusic[self.listWidget.currentRow()].path)
    #
    #     self.parent.PlayButton.setStyleSheet(
    #         "QPushButton#PlayButton{border-image: url(:/bg/play.png);}"
    #         "QPushButton#PlayButton:hover{border-image: url(:/bg/play_hover.png);}")
    #     self.playing = 0
    #
    #     pygame.mixer.music.load(self.allMusic[self.listWidget.currentRow()].path)

    def playtolist(self):
        self.currentIndex = self.listWidget.currentRow()
        self.parent.pl.addNews(self.allMusic)

    # def playit(self):
    #     if self.listWidget.currentRow() != -1:
    #         if self.playing == 1:
    #             self.parent.PlayButton.setStyleSheet(
    #                 "QPushButton#PlayButton{border-image: url(:/bg/play.png);}"
    #                 "QPushButton#PlayButton:hover{border-image: url(:/bg/play_hover.png);}")
    #             pygame.mixer.music.pause()
    #             self.playing = 2
    #         elif self.playing == 2:
    #             self.parent.PlayButton.setStyleSheet(
    #                 "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
    #                 "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
    #             self.playing = 1
    #             pygame.mixer.music.unpause()
    #         else:
    #             self.parent.PlayButton.setStyleSheet(
    #                 "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
    #                 "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
    #             self.playing = 1
    #             pygame.mixer.music.play()

