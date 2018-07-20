from ui.playListwidget import Ui_Form
from PyQt5 import Qt,QtWidgets,QtCore
from functions.getMp3 import *
import pygame
pattern = "%-30s%-20s%-5s"
class MyPSlider(QtWidgets.QSlider):
    """用于进度条的Slider，move的时候不改变值"""
    def __init__(self,ori, parent = None):
        super(MyPSlider, self).__init__(ori, parent)
        self.resize(150, 20)
        self.setStyleSheet("""
            QSlider::add-page:Horizontal{     
                background-color: #f0f0f4;
                height:4px;
                z-index:9;
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
        self.setValue(x / 150 * 100)
        self.parent.set(self.value())

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        self.setValue(x / 150 * 100)

    def mouseReleaseEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        self.setValue(x / 150 * 100)
        self.parent.set(self.value())

class MySlider(QtWidgets.QSlider):
    """音量的Slider，移动的时候改变值"""
    def __init__(self, ori, parent = None):
        super(MySlider, self).__init__(ori,parent)
        self.resize(150,20)
        self.setValue(80)
        self.setStyleSheet("""
    QSlider::add-page:Horizontal{     
        background-color: #f0f0f4;
        height:4px;
        z-index:9;
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
        self.setValue(x / 150 * 100)

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        self.setValue(x / 150 * 100)

    def mouseReleaseEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        self.setValue(x / 150 * 100)


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
        pygame.mixer.music.set_volume(self.parent.vSlider.value() / 100)
        self.musicpath = []
        self.updateInterface()
        self.parent.PlayButton.clicked.connect(self.playit)

        self.listWidget.itemDoubleClicked.connect(self.playfromlist)
        self.listWidget.takeItem(0)

    def changeVolume(self,v):
        if self.playing == 0:
            return
        pygame.mixer.music.set_volume(v/100)


    def playfromlist(self):
        self.index = self.listWidget.currentRow()
        self.letsPlay()

    def updateInterface(self):
        self.label_3.setText("播放列表:(共%d首)"%len(self.music))
        for i in self.music:
            self.listWidget.addItem(pattern%(i.name.strip(),i.artist.strip(),getFormattedTime(i.length)))

    def playnext(self):
        if len(self.music) == 0:
            return

        self.letsPlay()

    def playformer(self):
        if len(self.music) == 0:
            return
        if self.index <= 1:
            return
        self.index -= 2

        self.letsPlay()

    def letsPlay(self):
        '''
        按下播放键，以及定时器播放完毕，按下播放下一首时，调用
        :return:
        '''

        self.listWidget.setCurrentRow(self.index)
        if self.index >= len(self.music):
            return
        self.timerA = QtCore.QTimer(self)
        self.timerA.timeout.connect(self.letsPlay)
        self.timerA.start(self.music[self.index].length*1000+1000)
        # 自动播放下一首呵呵
        self.listWidget.setCurrentRow(self.index)
        pygame.mixer.music.load(self.music[self.index].path)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self.parent.vSlider.value()/100)

        self.n = float("%.1f" % pygame.mixer.music.get_volume())

        self.playing = 1
        self.parent.PlayButton.setStyleSheet(
            "QPushButton#PlayButton{border-image: url(:/bg/pause.png);}"
            "QPushButton#PlayButton:hover{border-image: url(:/bg/pause_hover.png);}")
        self.index += 1


    def playit(self):
        '''
        播方音乐
        :return:
        '''
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
                pygame.mixer.music.set_volume(0.8)
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
        self.music.extend(musicName[:])
        self.listWidget.clear()
        self.updateInterface()
        self.index = 0
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
        self.parent.orderButton.show()


