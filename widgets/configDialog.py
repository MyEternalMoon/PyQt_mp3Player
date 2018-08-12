from ui.config import Ui_Form
# from widgets.child.firstDialog import firstDialog
from PyQt5 import QtWidgets,Qt,QtCore
import copy,os


class configWidget(QtWidgets.QDialog,Ui_Form):

    first_set = QtCore.pyqtSignal()
    config_edited = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(configWidget, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.flag = None
        self.currentIndex = 0
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.rejectButton.clicked.connect(self.reject)
        self.customConfig = {}
        self.pushButton.clicked.connect(self.button_one_slot)
        self.pushButton_2.clicked.connect(self.button_two_slot)
        self.pushButton_3.clicked.connect(self.button_three_slot)
        self.optionWidget.clicked.connect(self.updateOptions)
        self.options = {0:
                            {0:
                                 ["默认音乐储存:", "选择位置"],
                             1:
                                 ["默认头像储存:",  "选择位置"],
                             2:
                                 ["网络服务:",  "更改"]},
                        1:
                            {0:
                                 ["关闭后仍记录播放列表:", "更改"],
                             1:
                                 ["循环播放列表:", "更改"],
                             2:
                                 ["全盘搜索范围:",  "增加"]},
                        2:
                            {0:
                                 ["", ""],
                             1:
                                 ["",  ""],
                             2:
                                 ["",  ""]},
                        3:
                            {0:
                                 ["",  ""],
                             1:
                                 ["",  ""],
                             2:
                                 ["",  ""]}
                        }
        self.optionHint = ['基本设置','用户设置','个性化','自定义']

    def updateOptions(self):
        self.currentIndex = self.optionWidget.currentRow()
        self.optionLabel.setText(self.optionHint[self.currentIndex])
        for j in range(len(self.groupBox.children())):
            self.groupBox.children()[j].setText(self.options[self.currentIndex][j][0])
            self.groupBox_3.children()[j].setText(self.options[self.currentIndex][2-j][1])
            self.groupBox_2.children()[j].setText('')
        if self.currentIndex == 0:
            self.groupBox_2.children()[0].setText(self.customConfig['MusicStorage'])
            self.groupBox_2.children()[1].setText(self.customConfig['HeadStorage'])
            self.groupBox_2.children()[2].setText('是' if self.customConfig['Internet'] == '1' else '否')
        elif self.currentIndex == 1:
            self.groupBox_2.children()[0].setText('是' if self.customConfig['MemoryPlayList'] == '1' else '否')
            self.groupBox_2.children()[1].setText("是" if self.customConfig['circle'] == '1' else '否')
            self.groupBox_2.children()[2].setText(', '.join(self.customConfig['searchAllDisc']))

    def button_one_slot(self):
        if self.currentIndex == 0:
            mess = QtWidgets.QFileDialog.getExistingDirectory(self, "选择音乐文件夹", os.getcwd())
            if len(mess) != 0:
                self.customConfig['MusicStorage'] = mess
                self.groupBox_2.children()[0].setText(mess)
        elif self.currentIndex == 1:
            self.customConfig['MemoryPlayList'] = '0' if self.customConfig['MemoryPlayList'] == '1' else '1'
            self.groupBox_2.children()[1].setText('否' if self.customConfig['MemoryPlayList'] == '0' else '是')

    def button_two_slot(self):
        if self.currentIndex == 0:
            mess = QtWidgets.QFileDialog.getExistingDirectory(self, "选择头像文件夹", "D:")
            if len(mess) != 0:
                self.customConfig['HeadStorage'] = mess
                self.groupBox_2.children()[1].setText(mess)
        elif self.currentIndex == 1:
            self.customConfig['circle'] = '0' if self.customConfig['circle'] == '1' else '1'
            self.groupBox_2.children()[1].setText('否' if self.customConfig['circle'] == '0' else '是')

    def button_three_slot(self):
        if self.currentIndex == 0:
            self.customConfig['Internet'] = '0' if self.customConfig['Internet'] == '1' else '1'
            self.groupBox_2.children()[2].setText('否' if self.customConfig['Internet'] == '0' else '是')
        elif self.currentIndex == 1:
            mess = QtWidgets.QFileDialog.getExistingDirectory(self, "选择音乐文件夹", os.getcwd())
            if len(mess) != 0:
                self.customConfig['searchAllDisc'].append(mess)
                self.groupBox_2.children()[2].setText(', '.join(self.customConfig['searchAllDisc']))

    def configinit(self, config):
        self.optionWidget.setCurrentRow(0)
        self.customConfig = copy.copy(config)
        self.updateOptions()

    def myaccept(self):
        self.accpet()

    def mouseMoveEvent(self, event):
        if self.flag:
            self.move(Qt.QPoint(self.pos() + event.pos() - self.currentPos))
            self.setCursor(Qt.QCursor(Qt.Qt.ClosedHandCursor))

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))
        self.flag = False

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if event.buttons() == QtCore.Qt.LeftButton and 0 < y < 40:
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))
            self.flag = True
