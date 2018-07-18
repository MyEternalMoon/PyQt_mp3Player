from PyQt5 import QtWidgets,QtGui,QtCore
from ui.musicWidget import Ui_Form
from functions import getMp3
import pygame

class MusicWidget(QtWidgets.QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.playing = 0 # 0 stopped, 1 playing, 2 paused
        self.parent = parent
        self.currentIndex = -1
        self.allMusic = getMp3.getMp3FromStore("./music/")
        for i in self.allMusic:
            self.listWidget.addItem(i.name)
        pygame.mixer.init()
       # self.parent.PlayButton.clicked.connect(self.playit)
        self.parent.FormerButton.clicked.connect(self.playformer)
        self.parent.NextButton.clicked.connect(self.playnext)
        self.listWidget.currentRowChanged.connect(self.changeMusic)
        self.listWidget.itemDoubleClicked.connect(self.playtolist)
       # self.show()



    def playformer(self):
        if self.listWidget.currentRow() == 0 or self.listWidget.currentRow() == -1:
            pass
        else:
            self.listWidget.setCurrentRow(self.listWidget.currentRow()-1)
            #self.playit()

    def playnext(self):
        if self.listWidget.currentRow() == self.listWidget.count()-1 or self.listWidget.currentRow() == -1:
            pass
        else:
            self.listWidget.setCurrentRow(self.listWidget.currentRow()+1)
            #self.playit()

    def changeMusic(self):
        pygame.mixer.music.load(self.allMusic[self.listWidget.currentRow()].path)

        self.parent.PlayButton.setStyleSheet(
            "QPushButton#PlayButton{border-image: url(:/bg/play.png);}"
            "QPushButton#PlayButton:hover{border-image: url(:/bg/play_hover.png);}")
        self.playing = 0

        pygame.mixer.music.load(self.allMusic[self.listWidget.currentRow()].path)

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

