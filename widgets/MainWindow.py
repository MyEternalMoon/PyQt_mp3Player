from ui.Main import Ui_MainWindow
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
        self.setGeometry(227, 90, 190, 190)
        self.setCursor(Qt.QCursor(Qt.Qt.PointingHandCursor))
        self.setToolTip("修改头像")

    def mouseReleaseEvent(self, QMouseEvent):
        if self.parent.currentIndex is not None:
            self.picChange.emit()


class PlayerMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    playListSignal = QtCore.pyqtSignal(list,str)
    StopSearchingSingal = QtCore.pyqtSignal()
    orderChangedSignal = QtCore.pyqtSignal()
    D = QtWidgets.QAction("从列表中删除   ")
    P = QtWidgets.QAction("播放   ")

    def __init__(self,parent = None):
        super(QtWidgets.QMainWindow,self).__init__(parent)

        self.setupUi(self)
        self._padding = 3
        self._bottom_rect = [QtCore.QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding-12, self.height() -11)]
        self.flag = False
        self.LM = True
        self.resizing = False

        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.currentIndex = None
        self.currentListMusicIndex = None
        self.user = ""
        self.isConfigEdited = False
        self.listShowing = False
        self.musiclistShowing = True
        self.localShowing = True

        self.playing = False
        self.MyList = ListOperation.loadList()
        self.musicStorage = "."
        self.MyMusic = []
        self.ConfigInfo = {}
        self.customInfo = {}
        self.initConfigs()

        self.eTimeLabel.move(self.eTimeLabel.x()+40, self.eTimeLabel.y())
        self.adD = addToListDialog.ListDialog(self.MyList)
        self.adD.hide()
        self.config = configDialog.configWidget(self)
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
        self.sure_3 = sureDialog.sureDialog(self)
        self.sure_3.hide()
        self.sure_2 = sureDialog.sureDialog(self)
        self.sure_2.hide()
        self.sure = sureDialog.sureDialog(self)
        self.sure.hide()
        self.scroll.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listMusicWidget.setVerticalScrollBar(self.scroll)
        self.pl = playListDialog.PlayListWidget(self)
        self.pl.resize(550,self.pl.height())
        self.pl.hide()
        self.pSlider = playListDialog.MyPSlider(Qt.Qt.Horizontal, self.LowerNav)
        self.pSlider.move(105, 43)
        self.pSlider.setWindowFlags(Qt.Qt.WindowStaysOnTopHint)
        self.vSlider = playListDialog.MySlider(Qt.Qt.Horizontal, self.LowerNav)
        self.vSlider.move(830, 34)

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
        self.listMusicWidget.setColumnWidth(0, 330)
        self.listMusicWidget.setColumnWidth(1, 260)
        self.listMusicWidget.setColumnWidth(2, 290)
        self.listMusicWidget.setColumnWidth(3, 110)

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
        self.picLabel.setStyleSheet('border: 1px groove #e4c6d0;')
        self.picLabel.setScaledContents(True)
        self.editListButton.hide()
        self.PlayAllButton.hide()
        # Initialize some information
        self.initMusicList()
        self.initInterfaceInfo()
        self.timesLabel.setText("播放次数：0")
        self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))

        self.config.config_edited[dict].connect(self.edit_restart)
        self.orderChangedSignal.connect(self.pl.changeOrder)
        self.StopSearchingSingal.connect(self.MusicWidget.stop_searching)
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
        self.pl.musicOutted.connect(self.music_out_of_play)
        self.MusicWidget.deleteSingal[MusicList.singleMusic].connect(self.pl.deleteMusic)
        self.MusicWidget.addToPlaySignal[MusicList.singleMusic].connect(self.pl.addToPlay)
        self.MusicWidget.addToListSignal[MusicList.singleMusic].connect(self.pl.addToList)
        self.MusicWidget.addToMusicListSignal[MusicList.singleMusic].connect(self.add_to_music_list)
        self.PlayAllButton.clicked.connect(self.playList)
        self.playOrderButton.clicked.connect(self.change_order)
        self.SoundButton.clicked.connect(self.volumeZero)
        self.PlaylistWidget.itemDoubleClicked.connect(self.playList)
        self.refreshButton.clicked.connect(self.MusicWidget.updateLocalMusic)
        self.toListButton.clicked.connect(self.list_hide)
        self.toListButton_2.clicked.connect(self.local_hide)
        self.picLabel.picChange.connect(self.change_head)
        self.searchDiskButton.clicked.connect(self.search_all)

    def searching_loading(self):
        self.sure_2.title.setText("搜索中")
        self.sure_2.label.setText("正在进行全盘搜索中，整个过程预计消耗数秒到一分钟。")
        self.sure_2.rejectButton.hide()
        self.sure_2.acceptButton.setText("后台")
        self.sure_2.show()
        self.sure_2.acceptButton.clicked.connect(self.sure_2.hide)

    def move_or_not(self,lis):
        self.sure.title.setText("完成")
        self.sure.label.setText(f"搜索完成, 共找到{len(lis)}首曲目\n是否要复制到默认音乐储存目录中?")
        self.sure.acceptButton.setText("确认")
        if self.sure.exec_():
            self.move_all(lis)
        self.sure_2.hide()

    def move_all(self,lis):
        """
        A new thread is needed here, do it tomorrow
        :param lis:
        :return:
        """
        self.MusicWidget.move_to_store([i.path for i in lis], self.customInfo['MusicStorage'])
        self.sure_3.title.setText("移动")
        self.sure_3.label.setText('正在移动中...')
        self.sure_3.rejectButton.hide()
        self.sure_3.acceptButton.hide()
        self.sure_3.exec_()

    def move_update(self, i, string):
        if i == 1:
            self.sure_3.accept()
            self.MusicWidget.updateLocalMusic()
        else:
            self.sure_3.label.setText(string)

    def search_all(self):
        self.MusicWidget.search_all(self.customInfo["searchAllDisc"])

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
            self.playListSignal.emit(self.MyList[self.currentIndex].musicContent, self.MyList[self.currentIndex].name)
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
        self.pl.move(650, self.height() - self.LowerNav.height() - self.pl.height())
        if self.listShowing:
            pass
        else:
            self.showListButton.hide()

            self.pl.show()
            self.listShowing = True
            self.pl.setFocus()
            self.showListButton.setCheckable(False)

    def editConfig(self):
        # self.config.setGeometry(self.x()+220,self.y()+120,716,516)
        self.config.configinit(self.customInfo)
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
        self.delListButton.hide()
        self.PlaylistWidget.resize(200, 30*len(self.MyList))
        self.MusicWidget.resize(200, 30*len(self.MyMusic))
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

        self.widget_2.move(0, self.PlaylistWidget.y()+len(self.MyList)*28)
        self.MusicWidget.move(0, self.toListButton_2.height()+self.PlaylistWidget.y()+len(self.MyList)*30)
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
        self.PlaylistWidget.resize(200, 28*len(self.MyList))
        self.widget_2.move(0, self.PlaylistWidget.y() + len(self.MyList) * 28)
        self.MusicWidget.move(0, self.toListButton_2.height() + self.PlaylistWidget.y() + len(self.MyList) * 28)
        self.PlaylistWidget.clear()
        for i in range(len(self.MyList)):
            if len(self.MyList[i].name) >= 9:
                self.PlaylistWidget.addItem(self.MyList[i].name[0:8]+"..")
            else:
                self.PlaylistWidget.addItem(self.MyList[i].name)
            p = self.PlaylistWidget.item(i)
            p.setToolTip(self.MyList[i].name)
        self.PlaylistWidget.show()
        self.musiclistShowing = True

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
            self.delListButton.hide()
        else:
            self.birthLabel.setText(self.MyList[self.currentIndex].birth + " 创建")
            self.amountLabel.setText(str(len(self.MyList[self.currentIndex].musicContent)))
            self.ListNameLabel.setText(self.MyList[self.currentIndex].name)
            self.descriptionEidt.setText(self.MyList[self.currentIndex].description)
            self.timesLabel.setText("播放次数：%d"%self.MyList[self.currentIndex].times)
            self.editListButton.show()
            self.updateListContent()
            self.PlayAllButton.show()
            self.delListButton.show()
            if self.MyList[self.currentIndex].picPath is not None:
                if os.path.isfile(self.MyList[self.currentIndex].picPath):
                    self.picLabel.setPixmap(QtGui.QPixmap(self.MyList[self.currentIndex].picPath))
                else:
                    self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
            else:
                self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))

    def createNewList(self):
        n = NewListDialog.listDialog(self)
        # n.setGeometry(self.x() + 325, self.y() + 160, 420, 384)
        if n.exec_():
            self.currentIndex = len(self.MyList) - 1
            self.updateList()
            self.PlaylistWidget.setCurrentRow(self.PlaylistWidget.count() - 1)
            self.updateInterface()

    def deleteList(self):
        """delete the list from storeage and update the list items
            We also delete its head and raise a warning first"""
        # print(self.currentIndex)
        if self.currentIndex is None:
            pass
        else:
            self.sure.title.setText("删除")
            self.sure.label.setText("确认要删除歌单《%s》吗？"%(self.MyList[self.currentIndex].name))
            if self.sure.exec_():
                try:
                    os.remove(self.MyList[self.currentIndex].picPath)
                except:
                    pass
                ListOperation.deleteList(self.currentIndex, self.MyList)
                self.ListNameLabel.setText("")
                self.descriptionEidt.setText("")
                self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
                self.updateList()
                self.listMusicWidget.clearContents()
                self.currentIndex = None

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
        e.start(1400)
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

    def list_hide(self):
        if self.musiclistShowing:
            self.musiclistShowing = False
            self.PlaylistWidget.hide()
            self.widget_2.move(0, self.PlaylistWidget.y())
            self.MusicWidget.move(0, self.toListButton_2.height() + self.PlaylistWidget.y())
        else:
            self.PlaylistWidget.show()
            self.musiclistShowing = True
            self.widget_2.move(0, self.PlaylistWidget.y() + len(self.MyList) * 28)
            self.MusicWidget.move(0, self.toListButton_2.height() + self.PlaylistWidget.y() + len(self.MyList) * 28)

    def local_hide(self):
        if self.localShowing:
            self.localShowing = False
            self.MusicWidget.hide()
        else:
            self.localShowing = True
            self.MusicWidget.show()

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

    def music_out_of_play(self):
        self.titleLabel.setText("")
        self.pSlider.setValue(0)
        self.eTimeLabel.setText("00:00")
        self.cTimeLabel.setText("00:00")

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

    def edit_restart(self,dic):
        self.newConfig = dict(self.ConfigInfo)
        self.newConfig["config"] = dic
        self.isConfigEdited = True
        self.hide()
        sure = sureDialog.sureDialog()
        sure.title.setText("重启设置")
        sure.label.setText("需要手动重启才能使设置生效哦！")
        sure.acceptButton.setText("立刻关闭")
        sure.rejectButton.setText("稍后")
        if sure.exec_():
            self.show()
            self.myclose()
        else:
            self.show()

    def resizeEvent(self, event):
        changed = self.height() - 812
        self.LowerNav.move(0, 720 + changed)
        self.Leftnav.resize(200,660 + changed)
        self.MusicWidget.resize(200,300+ changed)
        self.line.resize(2,660 + changed)
        self.line_15.resize(2,800+changed)
        self.frame.resize(1212,812+changed)
        self.listMusicWidget.resize(997, 400 + changed)
        self._bottom_rect = [QtCore.QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding-12, self.height() -11)]

    def mouseDoubleClickEvent(self, event):
        """双击后恢复原状"""
        if 0 < event.y() < self.TopNav.height():
            self.resize(1212,812)

    def closeEvent(self, event):
        """Save configs and list information when you quit"""
        if self.isConfigEdited:
            Configs.saveConfig(self.newConfig)
        ListOperation.pureSave(self.MyList)
