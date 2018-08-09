from ui.config import Ui_Form
# from widgets.child.firstDialog import firstDialog
from PyQt5 import QtWidgets,Qt,QtCore


class configWidget(QtWidgets.QDialog,Ui_Form):
    first_set = QtCore.pyqtSignal()
    config_edited = QtCore.pyqtSignal()
    def __init__(self, parent=None, First= True):
        super(configWidget, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.flag = None
        self.currentIndex = 0
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.rejectButton.clicked.connect(self.reject)
        # self.acceptButton.clicked.connect(self.myaccept)
        # if First:
        #     # self.fs = firstDialog(self.speWidget)
        #     self.fs.move(0,0)
        #     self.fs.show()
        #
        #     self.firstinit()
        # else:
        self.optionWidget.clicked.connect(self.updateOptions)
        self.options = {0:
                            {0:
                                 ["默认音乐储存", "", "选择位置"],
                             1:
                                 ["默认头像储存", "", "选择位置"],
                             2:
                                 ["", "", ""]},
                        1:
                            {0:
                                 ["关闭后仍记录播放列表", "是", "更改"],
                             1:
                                 ["循环播放列表", "是", "更改"],
                             2:
                                 ["", "", ""]},
                        2:
                            {0:
                                 ["", "", ""],
                             1:
                                 ["", "", ""],
                             2:
                                 ["", "", ""]},
                        3:
                            {0:
                                 ["", "", ""],
                             1:
                                 ["", "", ""],
                             2:
                                 ["", "", ""]}
                        }


        self.configinit()

    def updateOptions(self):
        self.currentIndex = self.optionWidget.currentRow()
        for j in range(len(self.groupBox.children())):
            self.groupBox.children()[j].setText(self.options[self.currentIndex][j][0])
            self.groupBox_2.children()[j].setText(self.options[self.currentIndex][j][1])

    def configinit(self):
        self.optionWidget.setCurrentRow(0)
        self.updateOptions()


    def myaccept(self):
        self.accpet()

    def mouseMoveEvent(self, event):
        if self.flag == True:
            self.move(Qt.QPoint(self.pos() + event.pos() - self.currentPos))
            self.setCursor(Qt.QCursor(Qt.Qt.ClosedHandCursor))

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))
        self.flag = False

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if event.buttons() == QtCore.Qt.LeftButton and 0 < y < 40:
            self.currentPos = event.pos()
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))
            self.flag = True
