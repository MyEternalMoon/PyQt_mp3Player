from ui.playListwidget import Ui_Form
from PyQt5 import Qt, QtWidgets, QtCore,QtGui
from functions.getMp3 import *
import pygame
import random
pattern = "%-30s%-20s%-5s"


class MusicPlayController(QtCore.QThread):
    timeOver = QtCore.pyqtSignal(name="timeover")
    oneSecPass = QtCore.pyqtSignal(int)
    timeEdit = QtCore.pyqtSignal(int)

    def __init__(self,parent):
        super(MusicPlayController, self).__init__()
        self.parent = parent
        self.timeLim = -1
        self.timeCur = 0
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.oneSecPassed)
        self.timer.start()
        self.parent.processEdited[int].connect(self.timeCurReset)

    def stopped(self):
        self.timer.stop()

    def continued(self):
        self.timer.start()

    def timeCurReset(self,t):
        self.timeCur = t
        self.timeEdit.emit(t)

    def timeLimNew(self,t,string):
        self.timeLim = t
        self.timeCur = 0

    def oneSecPassed(self):
        if self.timeLim == -1:
            return
        if self.timeLim == self.timeCur:
            self.timeOver.emit()
        else:
            self.timeCur += 1
            self.oneSecPass.emit(self.timeCur)


class MyPSlider(QtWidgets.QSlider):

    """用于进度条的Slider，move的时候不改变值"""
    processChanged = QtCore.pyqtSignal(float)
    valueChange = QtCore.pyqtSignal(int)

    def __init__(self,ori, parent = None):
        super(MyPSlider, self).__init__(ori, parent)
        self.parent = parent
        self.resize(250, 20)
        self.y = self.maximum()
        self.setStyleSheet("""
        
            QSlider::add-page:Horizontal{     
                background-color: #f0f0f4;
                height:4px;

        }
             QSlider::sub-page:Horizontal 
            {
                background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e96443, stop:1 #904e95);
                height:4px;
             }
            QSlider::groove:Horizontal 
            {
                background:transparent;
               height:6px;
            }
            QSlider::handle:Horizontal 
            {
                background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, 
    stop:0.6 #e96443, stop:0.778409 rgba(255, 255, 255, 255));
 
    width: 15px;
    margin-top: -5px;
    margin-bottom: -5px;
    border-radius: 6px;


            }

        """)

    def oneSecPassed(self):
        self.setValue(self.value()+1)

    def updateMax(self,p,string):
        self.y = p
        self.setMaximum(p)
        self.setValue(0)

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 250:
            self.setValue(self.maximum()-1)
        else:
            self.setValue(x / 250 * self.maximum())

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 250:
            self.setValue(self.maximum() - 1)
        else:
            self.setValue(int(x / 250 * self.maximum()))
        self.valueChange.emit(self.value())

    def mouseReleaseEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 250:
            self.setValue(self.maximum()-1)
            self.processChanged.emit((249 / 250))
        elif x <= 0:
            self.setValue(0)
            self.processChanged.emit(0)
        else:
            self.setValue(int(x / 250 * self.maximum()))
            self.processChanged.emit((x/250))


class MySlider(QtWidgets.QSlider):

    """音量的Slider，移动的时候改变值"""
    volumeChanged = QtCore.pyqtSignal(float)

    def __init__(self, ori, parent = None):
        super(MySlider, self).__init__(ori,parent)
        self.resize(180,20)
        self.setValue(80)
        self.setStyleSheet("""
    QSlider::add-page:Horizontal{     
        background-color: #f0f0f4;
        height:4px;
}
     QSlider::sub-page:Horizontal 
    {
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e96443, stop:1 #904e95);
        height:4px;
     }
    QSlider::groove:Horizontal 
    {
        background:transparent;
       height:6px;
    }
    QSlider::handle:Horizontal 
    {

        background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, 
    stop:0.6 #e96443, stop:0.778409 rgba(255, 255, 255, 255));
 
    width: 15px;
    margin-top: -5px;
    margin-bottom: -5px;
    border-radius: 6px;


    }
    
""")

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 150:
            self.setValue(180)
            self.volumeChanged.emit(1)
        elif x < 0:
            self.setValue(0)
            self.volumeChanged.emit(0)
        else:
            self.setValue(x / 180 * 100)
        self.volumeChanged.emit(x/180)

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 150:
            self.setValue(180)
            self.volumeChanged.emit(1)
        elif x < 0:
            self.setValue(0)
            self.volumeChanged.emit(0)
        else:
            self.setValue(x / 180 * 100)
            self.volumeChanged.emit(x/180)

    def mouseReleaseEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 150:
            self.setValue(180)
            self.volumeChanged.emit(1)
        elif x < 0:
            self.setValue(0)
            self.volumeChanged.emit(0)
        else:
            self.setValue(x / 180 * 100)
            self.volumeChanged.emit(x/180)


class PlayListWidget(Ui_Form, QtWidgets.QWidget):

    playStopped = QtCore.pyqtSignal(name="playStopped")
    playContinued = QtCore.pyqtSignal()
    playStarted = QtCore.pyqtSignal(int,str)
    processEdited = QtCore.pyqtSignal(int)
    playCrushed = QtCore.pyqtSignal(str)
    musicOutted = QtCore.pyqtSignal()

    def __init__(self,parent = None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.playing = 0
        self.currentIndex = None
        self.parent = parent
        self.control = MusicPlayController(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.music = []  # singleMusic list, mixer plays from its path

        pygame.mixer.init()
        self.musicpath = []  # not useful yet
        self.listName = ""
        self.play_mode = 1  # 1 == in order; 2 == random; 3 == single;
        self.shuffled = False  # flag of random order shuffled
        self.initialize_list_from_cache()

        self.resize(550,self.height())

        self.listWidget.setRowCount(len(self.music))
        self.listWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem(" 音乐标题"))
        self.listWidget.horizontalHeaderItem(0).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(" 歌手"))
        self.listWidget.horizontalHeaderItem(1).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(" 时长"))
        self.listWidget.horizontalHeaderItem(2).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listWidget.horizontalHeader().setDisabled(True)
        self.listWidget.setColumnWidth(0, 224)
        self.listWidget.setColumnWidth(1, 224)
        self.listWidget.setColumnWidth(2, 88)
        self.updateInterface()

        '''Signals and slots'''
        self.control.oneSecPass.connect(self.parent.oneSecPassed)
        self.control.timeEdit.connect(self.parent.updateLabel)
        self.control.timeOver.connect(self.play_over)
        self.playStopped.connect(self.control.stopped)
        self.playContinued.connect(self.control.continued)
        self.playStarted[int,str].connect(self.control.timeLimNew)
        self.playStarted[int,str].connect(self.parent.initLabel)
        self.listWidget.itemDoubleClicked.connect(self.play_from_list)
        self.pushButton.setCursor(Qt.Qt.PointingHandCursor)
        self.pushButton.clicked.connect(self.clear_list)

    def initialize_list_from_cache(self):
        if self.parent.customInfo["MemoryPlayList"] == "1":
            _ = getMp3ToPlayList('.')
            self.music.extend(_)
            self.listName = "上一次播放列表"
            self.updateInterface()

        else:
            self.music = []

    def updateInterface(self):
        """
        update listWidget interface once some changes happen.
        :return:
        """
        self.listWidget.setRowCount(len(self.music))
        self.label_3.setText(f"播放列表:<{self.listName}>, (共{len(self.music)}首) ")
        for i in range(len(self.music)):
            self.listWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.music[i].name))
            self.listWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.music[i].artist))
            self.listWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(getFormattedTime(self.music[i].length)))

    """The three functions below are connected with the signal from content menu of MusicWidget"""
    def deleteMusic(self, music):
        """
        this is a bit different. It really works only when the music to be deleted is playing or in list.
        we can not delete music from play list(It has no popMenu)
        :param music: singleMusic object
        :return:
        """
        if pygame.mixer.music.get_busy() and self.music[self.currentIndex-1].path == music.path:
            pygame.mixer.music.stop()
            del self.music[self.currentIndex]
            # self.currentIndex -= 1
            self.letsPlay()
        elif pygame.mixer.music.get_busy():
            del self.music[self.currentIndex]
        if not len(self.music):
            self.currentIndex = None

    def addToPlay(self, music):
        """
        add single music to play list and play it immediately.
        shut down the current music and do play_over, the place of insertion is currentIndex + 1 or 0
        :param music: singleMusic object
        :return:
        """
        if self.playing == 1 or self.playing == 2:
            pygame.mixer.music.stop()
            self.music.insert(self.currentIndex + 1, music)
            self.updateInterface()
            self.play_over()
            # self.letsPlay()
        else:
            self.music.insert(0, music)
            self.updateInterface()
            self.currentIndex = 0
            self.letsPlay()

    def addListToList(self, List, title):
        """
        add a whole customer's list to play list but do not play it immediately. update listWidget
        :param List: list object of singleMusic
        :param title: title of the list(Maybe useful latter to decide whether the list is already in)
        :return: None
        """
        if len(List) == 0:
            return
        self.music = []
        if self.listName == title:
            self.listWidget.clearContents()
            self.currentIndex = -1
        self.listName = title
        self.music.extend(List)
        self.currentIndex = -1
        # if self.playing == 0:
        #     self.currentIndex = temp = -1
        # else:
        #     temp = self.currentIndex
        # for i in range(len(List)):
        #     self.music.insert(temp+i+1,List[i])
        if self.play_mode == 2:
            random.shuffle(self.music)
            self.shuffled = True
        self.updateInterface()
        self.play_over()
        # self.letsPlay()

    def addToList(self, music):
        """
        add an single music into playing list but do not play it immediately. and update listWidget.
        :param music: singleMusic object
        :return: None
        """
        if self.playing == 0:
            self.music.insert(0, music)
            self.updateInterface()
            self.currentIndex = 0
        else:
            self.music.insert(self.currentIndex + 1, music)
            self.updateInterface()

    """The two functions below are connected with the signal from content menu of MainWindow's slider 
     to change volume and progress"""
    def change_progress(self, p):
        """
        By the signal of parent's pSlider(MouseRelease only)
        if we turn back, the music has to be reloaded. after this, emit a signal to controller and labels.
        :param p: percentage of progress
        :return: None
        """
        if self.playing == 0:
            self.parent.pSlider.setValue(0)
            return
        pygame.mixer.music.load(self.music[self.currentIndex].path)
        pygame.mixer.music.play(start=int(p * self.music[self.currentIndex].length))
        self.processEdited.emit(int(p * self.music[self.currentIndex].length))

    def change_volume(self, v):
        """
        By the signal of parent's vSlider(by clicking or SoundButton), and change volume.
        :param v: volume, it has been transformed
        :return: None
        """
        if self.playing == 0:
            return
        pygame.mixer.music.set_volume(v)

    def play_from_list(self):
        """
        When double clicked the music in this dialog's listWidget, play it.
        :return: None
        """
        self.currentIndex = self.listWidget.currentRow()
        self.letsPlay()

    def letsPlay(self):
        '''
        The most important implementation of the whole software.
        Bugs may frequently occur, I want to write its doc later(tomorrow maybe)
        :return: None
        '''

        if self.currentIndex is None:
            return
        if self.currentIndex >= len(self.music):
            if self.parent.customInfo['circle'] == "1":
                self.currentIndex = 0
            else:
                self.currentIndex -= 1
                pygame.mixer.music.stop()
                return
        self.listWidget.selectRow(self.currentIndex)
        # if not self.music[self.currentIndex].isEnabled:
        #     self.play_over()
        try:
            pygame.mixer.music.load(self.music[self.currentIndex].path)
        except pygame.error:
            self.playCrushed.emit(self.music[self.currentIndex].path)
            del self.music[self.currentIndex]
            self.updateInterface()
        else:
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(self.parent.vSlider.value()/100)
            self.playStarted.emit(self.music[self.currentIndex].length,
                                  self.music[self.currentIndex].name+" - "+self.music[self.currentIndex].artist)
            self.playing = 1
            self.parent.PlayButton.setStyleSheet(
                "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
                "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")

    def play_over(self):
        """
        when the the controller(a timer) times out or other signals like play_latter or functions that need to
        end the current playing, like add new music or list
        the implementation is a bit strange but useful
        play_mode is to control the order of music by set the currentIndex
        Obviously, when we finished one music, we should add 1 to currentIndex(mode 1 and 2),
        and in mode 3, it doesn't change
        :return: None
        """
        if self.play_mode == 1:
            self.currentIndex += 1
            self.shuffled = False
        elif self.play_mode == 2:
            if not self.shuffled:
                self.shuffled = True
                random.shuffle(self.music)
                self.updateInterface()
                self.currentIndex = 0
            else:
                self.currentIndex += 1
        else:
            self.shuffled = False
        self.letsPlay()

    """The three functions below is connected to the click of the parent's three buttons
    (play/pause), next, former"""
    def play_it(self):
        '''
        Control the player and icons with the parent's play/pause button.
        :return: None
        '''

        if self.listWidget.currentRow() != -1:
            if self.playing == 1:
                self.parent.PlayButton.setStyleSheet(
                    "QPushButton#PlayButton{border-image: url(:/bg/play.png);}"
                    "QPushButton#PlayButton:hover{border-image: url(:/bg/play_hover.png);}")
                pygame.mixer.music.pause()
                self.playing = 2
                self.playStopped.emit()
            elif self.playing == 2:
                # self.n = pygame.mixer.music.get_volume()
                # pygame.mixer.music.set_volume(0.8)
                self.parent.PlayButton.setStyleSheet(
                    "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
                    "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
                pygame.mixer.music.unpause()
                self.playing = 1
                self.playContinued.emit()
            else:
                pygame.mixer.music.load(self.music[self.currentIndex].path)
                self.parent.PlayButton.setStyleSheet(
                    "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
                    "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
                self.playing = 1
                pygame.mixer.music.play()

    def play_next(self):
        """
        connected with parent's signal. if no music is in list, do nothing. if there is, change currentIndex
        according to play_mode.(play_over did this)
        :return: None
        """
        if self.currentIndex is None:
            return
        self.play_over()

    def play_former(self):
        """
        connected with parent's signal. if no music is in list, do nothing. if there is, change currentIndex
        according to play_mode.(It doesn't connect to play_over)
        :return: None
        """
        if self.currentIndex is None:
            return
        if len(self.music) == 0:
            return
        if self.currentIndex == 0:
            return
        if self.play_mode != 3:
            self.currentIndex -= 1
        self.letsPlay()

    def changeOrder(self):
        """
        connected with parent's signal. the icon is changed in parent's function
        and we only change the mode code, it works only when play_over works.
        :return: None
        """
        if self.play_mode == 3:
            self.play_mode = 1
        else:
            self.play_mode += 1

    def addNews(self, mu):
        """
        When double clicked a list in mainWindow, it emits a signal connected to this
        and add all the music of the list to player's list, and before it we cleared all music in it initially
        after adding, we playIt right now.
        :param mu: all music in the list(it is a list)
        :return:None
        """
        self.listName = "本地音乐"
        self.music = []
        self.music.extend(mu[:])
        if self.play_mode == 2 and not self.shuffled:
            random.shuffle(self.music)
            self.shuffled = True
        self.listWidget.clearContents()
        self.updateInterface()
        self.currentIndex = 0
        self.letsPlay()

    def clear_list(self):
        """
        stop and clear all the music in list
        :return:
        """
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        self.listWidget.clearContents()
        self.music = []
        self.listWidget.setRowCount(0)
        self.musicOutted.emit()
        self.playStopped.emit()
        self.playing = 0
        self.currentIndex = None

    def go(self):
        """
        I forget about this emmmm... BTW, It doesn't seem useful
        :return: None
        """
        if self.n <= 0:
            pygame.mixer.music.pause()
            self.t.stop()
            self.n = 1.0
        else:
            self.n -= 0.05
            pygame.mixer.music.set_volume(self.n)

    # def mouseReleaseEvent(self, QMouseEvent):
    #     """
    #     when focus out, show parent's showListButton and hide the playDiglog
    #     (maybe it can be replaced by a signal and slot)
    #     :param QFocusEvent:
    #     :return: None
    #     """
    #     if QMouseEvent.x() < self.x() or QMouseEvent.y() < self.y() or QMouseEvent.y() > self.y()+self.height():
    #         self.hide()
    #
    def focusOutEvent(self, QFocusEvent):
        """
        when focus out, show parent's showListButton and hide the playDiglog
        (maybe it can be replaced by a signal and slot)
        :param QFocusEvent:
        :return: None
        """
        self.parent.listShowing = False
        self.hide()
        self.parent.showListButton.show()

    def closeEvent(self, QCloseEvent):
        """
        connected to EndSignal, when close the MainWindow, we close this first(only way), and
        the music fade out in 1 second, and the whole project is closed.
        :param QCloseEvent:
        :return: None
        """
        if self.playing == 1:
            pygame.mixer.music.fadeout(1000)
        if self.parent.customInfo["MemoryPlayList"] == "1":
            savePlayList('.', self.music)
            print("saving")
        else:
            savePlayList('.', self.music)
