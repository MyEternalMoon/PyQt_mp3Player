from ui.Main import Ui_MainWindow
from ui.loading import Ui_Form
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from functions import Configs, ListOperation
from widgets import NewListDialog, musicWidget,configDialog,playListDialog
from functions import getMp3,MusicList
from widgets.child import addToListDialog, sureDialog
from PIL import Image
import os
import random


class MyLabel(QtWidgets.QLabel):

    picChange = QtCore.pyqtSignal()

    def __init__(self,parent=None):
        super(MyLabel, self).__init__(parent)
        self.parent = parent
        self.setGeometry(237, 110, 140, 140)
        self.setCursor(Qt.QCursor(Qt.Qt.PointingHandCursor))
        self.setToolTip("修改头像")

    def mouseReleaseEvent(self, QMouseEvent):
        if self.parent.currentIndex is not None:
            self.picChange.emit()


class PlayerMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    playListSignal = QtCore.pyqtSignal(list,str)
    orderChangedSignal = QtCore.pyqtSignal()
    D = QtWidgets.QAction("从列表中删除   ")
    P = QtWidgets.QAction("播放   ")

    def __init__(self,parent = None):
        super(QtWidgets.QMainWindow,self).__init__(parent)

        self.setupUi(self)
        self._padding = 3
        self._bottom_rect = [QtCore.QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]
        self.flag = False
        self.LM = True
        self.resizing = False

        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.currentIndex = None
        self.currentListMusicIndex = None
        self.user = ""
        self.listShowing = False

        self.playing = False
        self.MyList = ListOperation.loadList()
        self.musicStorage = "."
        self.MyMusic = []
        self.ConfigInfo = {}
        self.customInfo = {}

        self.config = configDialog.configWidget()
        self.adD = addToListDialog.ListDialog(self.MyList)
        self.adD.hide()
        self.config.hide()
        self.scroll = QtWidgets.QScrollBar()
        self.scroll.setStyleSheet("""QScrollBar:vertical {     
                           border-radius:4px;         
                           border: none;
                           background:transparent;
                           width:10px;
                           height:410px;

                       }
                       QScrollBar::down-arrow{height:0px}
                       QScrollBar::handle:vertical {
                       border-radius:4px;
                       border:none;
                       background:rgba(112,112,112,0.5);

                       }
                       QScrollBar::down-arrow{width:0px}
               """)

        self.sure = sureDialog.sureDialog(self)
        self.sure.hide()
        self.scroll.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listMusicWidget.setVerticalScrollBar(self.scroll)
        self.pl = playListDialog.PlayListWidget(self)
        self.pl.hide()
        self.pSlider = playListDialog.MyPSlider(Qt.Qt.Horizontal, self.LowerNav)
        self.pSlider.move(100, 43)
        self.pSlider.setWindowFlags(Qt.Qt.WindowStaysOnTopHint)
        self.vSlider = playListDialog.MySlider(Qt.Qt.Horizontal, self.LowerNav)
        self.vSlider.move(760, 34)

        self.MusicWidget = musicWidget.MusicWidget(self.Leftnav,self)
        self.MusicWidget.move(0, 333)
        self.MusicWidget.resize(200, 300)
        self.line_12.setCursor(Qt.QCursor(Qt.Qt.SizeVerCursor))

        self.listMusicWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  音乐标题"))
        self.listMusicWidget.horizontalHeaderItem(0).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listMusicWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("  歌手"))
        self.listMusicWidget.horizontalHeaderItem(1).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listMusicWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("  专辑"))
        self.listMusicWidget.horizontalHeaderItem(2).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listMusicWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("  时长"))
        self.listMusicWidget.horizontalHeaderItem(3).setTextAlignment(Qt.Qt.AlignLeft | Qt.Qt.AlignVCenter)
        self.listMusicWidget.horizontalHeader().setDisabled(True)
        self.listMusicWidget.setColumnWidth(0, 300)
        self.listMusicWidget.setColumnWidth(1, 240)
        self.listMusicWidget.setColumnWidth(2, 250)
        self.listMusicWidget.setColumnWidth(3, 105)

        self.picLabel = MyLabel(self)
        self.popMenu = QtWidgets.QMenu()
        self.popMenu.addAction(self.P)
        self.popMenu.addAction(self.D)
        self.popMenu.setStyleSheet("QMenu{background-color:rgb(252, 239, 232);"
                                   "font-size:16px;padding:3px 10px;"
                                   "font-family:\"微软雅黑\";"
                                   "color:rgb(112,112,112);"
                                   "border:1px solid #DBDBDB}"
                                   "QMenu::item{height:18px;"
                                   "background:transparent;"
                                   " border-bottom:1px solid #DBDBDB;"
                                   "padding:6px}"
                                   "QMenu::item:selected{background:rgba(245, 231, 236, 220);"
                                   "color:black }")
        self.listMusicWidget.customContextMenuRequested[QtCore.QPoint].connect(self.show_content_menu)
        self.listMusicWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.D.triggered.connect(self.delete_from_list)
        self.P.triggered.connect(self.play_to_list)

        # connect slot with signal
        self.picLabel.setScaledContents(True)
        self.editListButton.hide()
        self.PlayAllButton.hide()
        # Initialize some information
        self.initConfigs()
        self.initMusicList()
        self.initInterfaceInfo()
        self.timesLabel.setText("播放次数：unKnown")
        self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))

        self.orderChangedSignal.connect(self.pl.changeOrder)
        self.playListSignal[list, str].connect(self.pl.addListToList)
        self.PlayButton.clicked.connect(self.pl.play_it)
        self.exitButton.clicked.connect(self.myclose)
        self.hideButton.clicked.connect(self.showMinimized)
        self.vSlider.volumeChanged[float].connect(self.pl.change_volume)
        self.pSlider.valueChange[int].connect(self.updateLabel)
        self.pSlider.processChanged[float].connect(self.pl.change_progress)
        self.newListButton.clicked.connect(self.createNewList)
        self.PlaylistWidget.currentItemChanged.connect(self.updateInterface)
        self.delListButton.clicked.connect(self.deleteList)
        self.editListButton.clicked.connect(self.desChange)
        self.moveUpButton.clicked.connect(self.moveUp)
        self.configButton.clicked.connect(self.editConfig)
        self.descriptionEidt.installEventFilter(self)
        self.showListButton.clicked.connect(self.showList)
        self.NextButton.clicked.connect(self.pl.play_next)
        self.FormerButton.clicked.connect(self.pl.play_former)
        self.pl.playStarted[int,str].connect(self.pSlider.updateMax)
        self.pl.playCrushed[str].connect(self.crushed)
        self.MusicWidget.deleteSingal[MusicList.singleMusic].connect(self.pl.deleteMusic)
        self.MusicWidget.addToPlaySignal[MusicList.singleMusic].connect(self.pl.addToPlay)
        self.MusicWidget.addToListSignal[MusicList.singleMusic].connect(self.pl.addToList)
        self.MusicWidget.addToMusicListSignal[MusicList.singleMusic].connect(self.add_to_music_list)
        self.PlayAllButton.clicked.connect(self.playList)
        self.playOrderButton.clicked.connect(self.change_order)
        self.SoundButton.clicked.connect(self.volumeZero)
        self.PlaylistWidget.itemDoubleClicked.connect(self.playList)
        self.refreshButton.clicked.connect(self.MusicWidget.updateLocalMusic)
        self.picLabel.picChange.connect(self.change_head)

    def delete_from_list(self):
        if self.currentIndex is None or self.currentListMusicIndex is None:
            return
        del self.MyList[self.currentIndex].musicContent[self.currentListMusicIndex]
        self.updateListContent()

    def play_to_list(self):
        if self.currentIndex is None or self.currentListMusicIndex is None:
            return
        self.pl.addToPlay(self.MyList[self.currentIndex].musicContent[self.currentListMusicIndex])

    def change_order(self):
        if self.pl.play_mode == 1:
            self.playOrderButton.setStyleSheet("border-image: url(:/order/random_order.png);")
            self.playOrderButton.setToolTip("Random")
        elif self.pl.play_mode == 2:
            self.playOrderButton.setStyleSheet("border-image: url(:/order/single_order.png);")
            self.playOrderButton.setToolTip("Single")
        else:
            self.playOrderButton.setStyleSheet("border-image: url(:/order/ordered_order.png);")
            self.playOrderButton.setToolTip("In order")
        self.orderChangedSignal.emit()

    def playList(self):
        if self.currentIndex is None:
            return
        if len(self.MyList[self.currentIndex].musicContent) > 0:
            self.MyList[self.currentIndex].times += 1
            self.playListSignal.emit(self.MyList[self.currentIndex].musicContent,self.MyList[self.currentIndex].name)
            self.updateInterface()

    def add_to_music_list(self, m):
        self.adD.List = self.MyList
        self.adD.initInterface()
        self.adD.setGeometry(self.x() + 400, self.y() + 200, 300, 400)
        if self.adD.exec_():
            self.MyList[self.adD.ListSelected].AddNewMusic(m)
            self.updateListContent()

    def initLabel(self,t,string):
        self.cTimeLabel.setText(getMp3.getFormattedTime(0))
        self.eTimeLabel.setText(getMp3.getFormattedTime(t))
        self.titleLabel.setText(string)

    def updateLabel(self,p):
        self.cTimeLabel.setText(getMp3.getFormattedTime(p))

    def oneSecPassed(self,p):
        self.cTimeLabel.setText(getMp3.getFormattedTime(p))
        self.pSlider.oneSecPassed()

    def showList(self):
        self.pl.move(600, self.height() - self.LowerNav.height() - self.pl.height())
        if self.listShowing:
            pass
        else:
            self.showListButton.hide()

            self.pl.show()
            self.listShowing = True
            self.pl.setFocus()
            self.showListButton.setCheckable(False)

    def editConfig(self):
        self.config.setGeometry(self.x()+220,self.y()+120,716,516)
        if self.config.exec_():
            pass

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
            self.PlaylistWidget.setCurrentRow(self.currentIndex-1)
            self.updateInterface()

    def initConfigs(self):
        self.ConfigInfo = Configs.initconfig()
        self.customInfo = self.ConfigInfo["config"]


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
        self.updateListContent()

    def updateListContent(self):
        if self.currentIndex == -1 or self.currentIndex is None:
            self.listMusicWidget.clearContents()
            return
        else:
            self.listMusicWidget.clearContents()
            self.listMusicWidget.setRowCount(len(self.MyList[self.currentIndex].musicContent))
            # print(self.MyList[self.currentIndex].musicContent)

            for i in range(len(self.MyList[self.currentIndex].musicContent)):
                self.listMusicWidget.setItem(i, 0,QtWidgets.QTableWidgetItem
                (' '+self.MyList[self.currentIndex].musicContent[i].name))
                self.listMusicWidget.setItem(i, 1, QtWidgets.QTableWidgetItem
                (' '+self.MyList[self.currentIndex].musicContent[i].artist))
                self.listMusicWidget.setItem(i, 2, QtWidgets.QTableWidgetItem
                (' ' + self.MyList[self.currentIndex].musicContent[i].album))
                self.listMusicWidget.setItem(i, 3, QtWidgets.QTableWidgetItem
                (' '+getMp3.getFormattedTime(self.MyList[self.currentIndex].musicContent[i].length)))
                if not self.MyList[self.currentIndex].musicContent[i].isEnabled:
                    self.listMusicWidget.item(i, 0).setForeground(QtGui.QBrush(Qt.Qt.red))
                    self.listMusicWidget.item(i, 1).setForeground(QtGui.QBrush(Qt.Qt.red))
                    self.listMusicWidget.item(i, 2).setForeground(QtGui.QBrush(Qt.Qt.red))
                    self.listMusicWidget.item(i, 3).setForeground(QtGui.QBrush(Qt.Qt.red))

    def updateList(self):
        if len(self.MyList) == 0:
            self.PlaylistWidget.clear()
        self.PlaylistWidget.clear()
        for i in range(len(self.MyList)):
            if len(self.MyList[i].name) >= 9:
                self.PlaylistWidget.addItem(self.MyList[i].name[0:8]+"..")
            else:
                self.PlaylistWidget.addItem(self.MyList[i].name)
            p = self.PlaylistWidget.item(i)
            p.setToolTip(self.MyList[i].name)

    def updateInterface(self):
        self.currentIndex = self.PlaylistWidget.currentRow()
        self.currentListMusicIndex = None
        if self.currentIndex is None or self.currentIndex == -1:
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
            self.updateListContent()
            self.PlayAllButton.show()
            if self.MyList[self.currentIndex].picPath is not None:
                if os.path.isfile(self.MyList[self.currentIndex].picPath):
                    self.picLabel.setPixmap(QtGui.QPixmap(self.MyList[self.currentIndex].picPath))
                else:
                    self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
            else:
                self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))

    def createNewList(self):
        n = NewListDialog.listDialog(None, self)
        n.setGeometry(self.x() + 325, self.y() + 160, 420, 384)
        if n.exec_():
            self.currentIndex = len(self.MyList) - 1
            self.updateList()
            self.PlaylistWidget.setCurrentRow(self.PlaylistWidget.count() - 1)
            self.updateInterface()

    def deleteList(self):
        """delete the list from storeage and update the list items
            We also delete its head and raise a warning first"""
        if self.currentIndex is None:
            pass
        else:
            self.sure.label.setText("确认要删除歌单《%s》吗？"%(self.MyList[self.currentIndex].name))
            if self.sure.exec_():
                try:
                    os.remove(self.MyList[self.currentIndex].picPath)
                except:
                    pass
                ListOperation.deleteList(self.currentIndex, self.MyList)
                self.currentIndex -= 1
                self.ListNameLabel.setText("")
                self.descriptionEidt.setText("")
                self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
                self.updateList()
                self.updateListContent()

    # def changeVolume(self,q):
    #     """Just Change the style sheet of button(Not useful now)"""
    #     if q != 0:
    #         self.SoundButton.setStyleSheet("border-image: url(:/buttons/sound_on.png);")
    #     else:
    #         self.SoundButton.setStyleSheet("border-image: url(:/buttons/sound_off.png);")
    #     self.pl.changeVolume(q)

    def volumeZero(self):
        """By pressing the SoundButton, we change the value of slider and the icon of the button
            At the same time, the slider emits signal to change volume"""
        if self.vSlider.value() <= 0:
            self.SoundButton.setStyleSheet("border-image: url(:/buttons/sound_on.png);")
            self.vSlider.setValue(80)
            self.vSlider.volumeChanged.emit(self.vSlider.value())
        else:
            self.SoundButton.setStyleSheet("border-image: url(:/buttons/sound_off.png);")
            self.vSlider.setValue(0)
            self.vSlider.volumeChanged.emit(self.vSlider.value())

    def desChange(self):
        """when you press the editButton, we make the lineEdit enabled"""
        if self.currentIndex is None:
            return
        else:
            self.descriptionEidt.setReadOnly(False)
            self.editListButton.setEnabled(False)
            self.descriptionEidt.setEnabled(True)
            self.descriptionEidt.setFrame(True)
            self.descriptionEidt.setStyleSheet("background-color:white;")
            self.descriptionEidt.setFocus()

    def myclose(self):
        """
        when clicked the exitButton, we close the playDialog first and fade out the music.
        :return: None
        """
        self.pl.close()
        e = QtCore.QTimer(self)
        self.MusicWidget.close()
        e.timeout.connect(self.close)
        e.start(1100)
        self.hide()

    def change_head(self):
        if self.currentIndex is None:
            return
        f = QtWidgets.QFileDialog.getOpenFileName(self, "选择头像", "C:\\", "Picture files(*.jpg;*.png)")
        pic_path = None
        im = None
        if f[0] != "":
            im = Image.open(f[0])
            n = "./Head/%dhead.png" % random.randint(10000000000, 99999999999)
            pic_path = n
        if im is not None:
            im.save(pic_path, "png")
            try:
                os.remove(self.MyList[self.currentIndex].picPath)
            except:
                pass
            self.MyList[self.currentIndex].picPath = pic_path
            self.updateInterface()

    def crushed(self, n):
        """
        When we can't play the music
        we can rewrite it with a better way -- store path instead of music object
        :param n: index of crushed music
        :return: None"""
        ListOperation.dealCrush(self.MyList, n)
        self.updateInterface()

    def show_content_menu(self, point):
        """
        when left button was pressed in listWidget on the right side, we do play and delete functions
        """
        self.currentListMusicIndex = self.listMusicWidget.currentRow()
        self.popMenu.exec_(QtGui.QCursor.pos())

    def eventFilter(self, obj, event):
        """
        When lineEdit focuses out, disable it and change style sheets.
        :param obj:
        :param event:
        :return: True, False(overwrite)
        """
        if self.descriptionEidt.isEnabled() == True:
            if obj == self.descriptionEidt:
                if event.type() == QtCore.QEvent.FocusOut:
                    self.MyList[self.currentIndex].ChangeDescription(self.descriptionEidt.text())
                    # ListOperation.pureSave(self.MyList)
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
        if self.flag:
            self.move(Qt.QPoint(self.pos() + event.pos() - self.currentPos))
            self.setCursor(Qt.QCursor(Qt.Qt.ClosedHandCursor))
        if self.resizing:
            self.resize(self.width(), event.pos().y())

    def mouseReleaseEvent(self,event):
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))
        self.flag = False
        self.resizing = False

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if event.buttons() == QtCore.Qt.LeftButton and 0 < y < 60:
            self.currentPos = event.pos()
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))
            self.flag = True
        elif event.buttons() == QtCore.Qt.LeftButton and event.pos() in self._bottom_rect:
            self.resizing = True
            self.setCursor(Qt.QCursor(Qt.Qt.SizeVerCursor))

    def resizeEvent(self, event):
        changed = self.height() - 800
        self.LowerNav.move(0, 720 + changed)
        self.MusicWidget.resize(200,300+ changed)
        self.line.resize(2,650 + changed)
        self.listMusicWidget.resize(897, 397 + changed)
        self._bottom_rect = [QtCore.QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]

    def mouseDoubleClickEvent(self, event):
        """双击后恢复原状"""
        if 0 < event.y() < self.TopNav.height():
            self.resize(1100,800)

    def closeEvent(self, event):
        """Save configs and list information when you quit"""
        Configs.saveConfig(self.ConfigInfo)
        ListOperation.pureSave(self.MyList)
