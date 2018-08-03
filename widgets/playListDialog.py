from ui.playListwidget import Ui_Form
from PyQt5 import Qt,QtWidgets,QtCore
from functions.getMp3 import *
import pygame
import random
import time
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

    def timeLimNew(self,t):
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

    def __init__(self,ori, parent = None):
        super(MyPSlider, self).__init__(ori, parent)
        self.parent = parent
        self.resize(200, 20)
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
                height: 30px;
                width:10px;

        	border-image: url(:/bg/sound.png);
                margin: -8 0px; 
            }

        """)

    def oneSecPassed(self):
        self.setValue(self.value()+1)

    def updateMax(self,p):
        self.y = p
        self.setMaximum(p)
        self.setValue(0)

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 200:
            self.setValue(self.maximum()-1)
        else:
            self.setValue(x / 200 * self.maximum())

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 200:
            self.setValue(self.maximum() - 1)
        else:
            self.setValue(x / 200 * self.maximum())

    def mouseReleaseEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 200:
            self.setValue(self.maximum()-1)
            self.processChanged.emit((199 / 200))
        elif x <= 0:
            self.setValue(0)
            self.processChanged.emit(0)
        else:
            self.setValue(x / 200 * self.maximum())
            self.processChanged.emit((x/200))


class MySlider(QtWidgets.QSlider):
    """音量的Slider，移动的时候改变值"""
    volumeChanged = QtCore.pyqtSignal(float)
    def __init__(self, ori, parent = None):
        super(MySlider, self).__init__(ori,parent)
        self.resize(150,20)
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
        height: 30px;
        width:10px;
       
	border-image: url(:/bg/sound.png);
        margin: -8 0px; 
    }
    
""")

    def mousePressEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 150:
            self.setValue(150)
            self.volumeChanged.emit(1)
        elif x < 0:
            self.setValue(0)
            self.volumeChanged.emit(0)
        else:
            self.setValue(x / 150 * 100)
        self.volumeChanged.emit(x/150)

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 150:
            self.setValue(150)
            self.volumeChanged.emit(1)
        elif x < 0:
            self.setValue(0)
            self.volumeChanged.emit(0)
        else:
            self.setValue(x / 150 * 100)
            self.volumeChanged.emit(x/150)

    def mouseReleaseEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        if x > 150:
            self.setValue(150)
            self.volumeChanged.emit(1)
        elif x < 0:
            self.setValue(0)
            self.volumeChanged.emit(0)
        else:
            self.setValue(x / 150 * 100)
            self.volumeChanged.emit(x/150)



class playListWidget(Ui_Form,QtWidgets.QWidget):

    playStopped = QtCore.pyqtSignal(name="playStopped")
    playContinued = QtCore.pyqtSignal()
    playStarted = QtCore.pyqtSignal(int)
    processEdited = QtCore.pyqtSignal(int)
    playCrushed = QtCore.pyqtSignal(str)

    def __init__(self,parent = None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.playing = 0
        self.currentIndex = 0
        self.parent = parent
        self.control = MusicPlayController(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.music = []

        pygame.mixer.init()
        self.musicpath = []
        self.listName = ""
        self.play_mode = 1 # 1 == in order; 2 == random; 3 == single;
        self.shuffled = False
        self.updateInterface()
        '''信号与槽'''
        self.control.oneSecPass.connect(self.parent.oneSecPassed)
        self.control.timeEdit.connect(self.parent.updateLabel)
        self.control.timeOver.connect(self.play_over)
        # self.parent.PlayButton.clicked.connect(self.playit)
        self.playStopped.connect(self.control.stopped)
        self.playContinued.connect(self.control.continued)
        self.playStarted[int].connect(self.control.timeLimNew)
        self.playStarted[int].connect(self.parent.initLabel)
        self.listWidget.itemDoubleClicked.connect(self.playfromlist)
        self.listWidget.setRowCount(len(self.music))
        self.listWidget.setColumnWidth(0,202)
        self.listWidget.setColumnWidth(1, 202)
        self.listWidget.setColumnWidth(2, 82)

    def updateInterface(self):
        """
        更新播放列表，每当有新的music加入时更新
        :return:
        """
        self.listWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem(" 音乐标题"))
        self.listWidget.horizontalHeaderItem(0).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(" 歌手"))
        self.listWidget.horizontalHeaderItem(1).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(" 时长"))
        self.listWidget.horizontalHeaderItem(2).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listWidget.horizontalHeader().setDisabled(True)
        self.listWidget.setRowCount(len(self.music))

        self.label_3.setText("播放列表:(共%d首)"%len(self.music))
        for i in range(len(self.music)):
            self.listWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.music[i].name))
            self.listWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.music[i].artist))
            self.listWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(getFormattedTime(self.music[i].length)))


    '''以下三个函数对应来自MusicWidget右键菜单的信号'''
    def deleteMusic(self, music):
        if pygame.mixer.music.get_busy() and self.music[self.currentIndex-1].path == music.path:
            pygame.mixer.music.stop()
            del self.music[self.currentIndex]
            # self.currentIndex -= 1
            self.letsPlay()
        elif pygame.mixer.music.get_busy():
            del self.music[self.currentIndex]

    def addToPlay(self, music):
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
        if len(List) == 0:
            return
        self.listName = title
        if self.playing == 0:
            self.currentIndex = temp = 0
        else:
            temp = self.currentIndex
        for i in range(len(List)):
            self.music.insert(temp+i+1,List[i])
        if self.play_mode == 2 and not self.shuffled:
            random.shuffle(self.music)
            self.shuffled = True
        self.updateInterface()
        self.play_over()
        # self.letsPlay()

    def addToList(self,music):
        if self.playing == 0:
            self.music.insert(0, music)
            self.updateInterface()
            self.currentIndex = 0
        else:
            self.music.insert(self.currentIndex + 1,music)
            self.updateInterface()


    '''以下两个函数对应来自slider的信号，改变音量和进度'''
    def changeProgress(self,p):
        if self.playing == 0:
            self.parent.pSlider.setValue(0)
            return
        pygame.mixer.music.load(self.music[self.currentIndex].path)
        pygame.mixer.music.play(start=int(p * self.music[self.currentIndex].length))
        self.processEdited.emit(int(p * self.music[self.currentIndex].length))

    def changeVolume(self,v):
        if self.playing == 0:
            return
        pygame.mixer.music.set_volume(v)


    def playfromlist(self):
        """
        从播放列表双击播放
        :return:
        """
        self.currentIndex = self.listWidget.currentRow()
        self.letsPlay()


    def playnext(self):
        self.play_over()

    def playformer(self):
        if len(self.music) == 0:
            return
        if self.currentIndex == 0:
            return
        if self.play_mode != 3:
            self.currentIndex -= 1
        self.letsPlay()


    def letsPlay(self):
        '''
        按下播放键，以及定时器播放完毕，按下播放下一首时，调用
        :return:
        '''

        if self.currentIndex >= len(self.music):
            self.currentIndex = 0
        self.listWidget.selectRow(self.currentIndex)
        if not self.music[self.currentIndex].isEnabled:
            self.play_over()
        try:
            pygame.mixer.music.load(self.music[self.currentIndex].path)
        except pygame.error:
            self.playCrushed.emit(self.music[self.currentIndex].path)
            del self.music[self.currentIndex]
            self.updateInterface()
        else:
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(self.parent.vSlider.value()/100)
            self.playStarted.emit(self.music[self.currentIndex].length)
            # self.n = float("%.1f" % pygame.mixer.music.get_volume())
            self.playing = 1
            self.parent.PlayButton.setStyleSheet(
                "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
                "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")

    def play_over(self):
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


    def playit(self):
        '''
        由播放按钮控制的播放暂停与继续
        :return:
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

    def changeOrder(self):
        if self.play_mode == 3:
            self.play_mode = 1
        else:
            self.play_mode += 1

    def addNews(self, mu):
        self.music = []
        """
        当双击的时候就把list里边后边的歌都加入playList里面，也可以一首一首加，用后面的方法
        一旦使用addNews，就把播放列表全部更新，并立刻播放
        :param musicName:
        :param musicPath:
        :return:
        """
        self.music.extend(mu[:])
        if self.play_mode == 2 and not self.shuffled:
            random.shuffle(self.music)
            self.shuffled = True
        self.listWidget.clear()
        self.updateInterface()
        self.currentIndex = 0
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
        '''
        当失去聚焦时，hide，并显示showButton
        :param QFocusEvent:
        :return:
        '''
        self.parent.listShowing = False
        self.hide()
        self.parent.showListButton.show()


