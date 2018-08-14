from PyQt5 import QtWidgets,QtGui,QtCore
from ui.musicWidget import Ui_Form
from functions import getMp3,MusicList
from widgets.child.tagDialog import tagDialog
import pygame


class MyThread(QtCore.QThread):

    DoneSearchSignal = QtCore.pyqtSignal(list)

    def __init__(self, parent = None):
        super(MyThread, self).__init__(parent)
        self.working = True
        self.music = []
        self.start()

    def start(self):
        self.music = getMp3.getMp3()
        self.DoneSearchSignal.emit(self.music)
        self.close()


class MusicWidget(QtWidgets.QWidget,Ui_Form):
    '''
    三个signal 先传给父窗口，再间接给子窗口pl
    '''
    deleteSingal = QtCore.pyqtSignal(MusicList.singleMusic)
    addToListSignal = QtCore.pyqtSignal(MusicList.singleMusic)
    addToPlaySignal = QtCore.pyqtSignal(MusicList.singleMusic)
    addToMusicListSignal = QtCore.pyqtSignal(MusicList.singleMusic)

    def __init__(self,parent=None,trueparent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.playing = 0 # 0 stopped, 1 playing, 2 paused
        self.parent = trueparent
        self.currentIndex = -1
        self.music = getMp3.getMp3FromCache("./music/")
        for i in self.music:
            if i.isEnabled:
                self.listWidget.addItem(i.name)
        pygame.mixer.init()
        self.my_thread = None
        self.popMenu = QtWidgets.QMenu()
        P = QtWidgets.QAction('播放', self)
        N = QtWidgets.QAction('添加到下一首播放', self)
        D = QtWidgets.QAction('删除', self)
        C = QtWidgets.QAction("修改tag信息",self)
        L = QtWidgets.QAction("添加到歌单", self)
        self.musicStorage = "./music/"
        self.popMenu.addAction(P)
        self.popMenu.addAction(N)
        self.popMenu.addAction(L)
        self.popMenu.addAction(D)
        self.popMenu.addAction(C)
        self.popMenu.setStyleSheet("QMenu{background-color:rgba(255, 240, 245, 245);"
                                   "font-size:16px;padding:3px 10px;font-family:\"微软雅黑\";"
                                   "color:rgb(112,112,112);""border:1px solid #DBDBDB}"
                                   "QMenu::item{background:transparent;"
                                   "height:18px;"
                                   "border-bottom:1px solid #DBDBDB;padding:6px}"
                                   "QMenu::item:selected{background:rgba(245, 231, 236, 220);color:black }")
        P.triggered.connect(self.addToPlay)
        N.triggered.connect(self.addToList)
        L.triggered.connect(self.addToMusicList)
        D.triggered.connect(self.deleteMusic)
        C.triggered.connect(self.change_tag)
        self.listWidget.itemDoubleClicked.connect(self.playtolist)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested[QtCore.QPoint].connect(self.showContentMenu)

    def updateLocalMusic(self):
        self.music = getMp3.getMp3FromStore(self.parent.customInfo['MusicStorage'])
        self.updateInterface()

    def updateInterface(self):
        self.listWidget.clear()
        for i in range(len(self.music)):
            self.listWidget.addItem(self.music[i].name)
            if not self.music[i].isEnabled:
                self.listWidget.item(i).setForeground(QtGui.QBrush(Qt.Qt.red))

        self.listWidget.setCurrentRow(-1)
        self.currentIndex = -1

    def showContentMenu(self,point):
        self.currentIndex = self.listWidget.currentRow()
        self.popMenu.exec_(QtGui.QCursor.pos())

    def deleteMusic(self):
        if self.currentIndex == -1:
            pass
        else:
            self.parent.sure.label.setText(
                "确认要删除歌曲《%s》吗？" % self.music[self.currentIndex].name)
            if self.parent.sure.exec_():
                if getMp3.deleteMusic(self.music[self.currentIndex]):
                    self.deleteSingal.emit(self.music[self.currentIndex])
                    self.updateLocalMusic()

    def addToPlay(self):
        if self.currentIndex == -1:
            pass
        else:
            self.addToPlaySignal.emit(self.music[self.currentIndex])

    def addToList(self):
        if self.currentIndex == -1:
            pass
        else:
            self.addToListSignal.emit(self.music[self.currentIndex])

    def change_tag(self):
        d = tagDialog(self.music[self.currentIndex], self.parent)
        if d.exec_():
            self.updateLocalMusic()

    def addToMusicList(self):
        if self.currentIndex == -1:
            pass
        else:
            self.addToMusicListSignal.emit(self.music[self.currentIndex])

    def get_all_mp3(self):
        self.my_thread = MyThread(self)
        self.my_thread.start()
        self.my_thread.DoneSearchSignal[list].connect(self.get_all_music)

    def get_all_music(self, lis):
        self.music = lis

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
        emit = self.music[:]
        emit.insert(0, self.music[self.currentIndex])
        del emit[self.currentIndex+1]
        self.parent.pl.addNews(emit)

    def closeEvent(self, QCloseEvent):
        getMp3.saveMp3("./music/", self.music)
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

