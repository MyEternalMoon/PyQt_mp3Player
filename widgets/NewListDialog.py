from PyQt5 import QtWidgets,QtCore,QtGui,Qt
from ui.newDialog import Ui_Dialog
from functions import ListOperation, MusicList
from PIL import Image
import random

class listDialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,parent):
        self.parent = parent
        super(QtWidgets.QDialog,self).__init__(parent)
        self.setupUi(self)
        self.setGeometry(325, 160, 420, 384)
        self.picPath = None
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.rejectButton.clicked.connect(self.reject)
        self.acceptButton.clicked.connect(self.do)
        self.fileDialogButton.clicked.connect(self.chooseHead)
        self.nameLineEdit.setFocus()
        self.im = None
        self.picLabel.setPixmap(QtGui.QPixmap("./Head/unKnown.png"))
        self.picLabel.setScaledContents(True)

    def chooseHead(self):
        f = QtWidgets.QFileDialog.getOpenFileName(self,"选择头像","C:\\","Picture files(*.jpg;*.png)")
        if f[0] != "":
            self.im = Image.open(f[0])
            n = "./Head/%dhead.png"%random.randint(10000000000,99999999999)
            self.picPath = n
            self.fileDialogButton.setText(f[0])
            self.fileDialogButton.setToolTip(f[0])
            self.picLabel.setPixmap(QtGui.QPixmap(f[0]))

    def do(self):
        if len(self.nameLineEdit.text()) == 0:
            self.reject()
        else:
            if self.im is not None:
                self.im.save(self.picPath, "png")
            self.newList = MusicList.musicList(self.nameLineEdit.text(),self.parent.user,"",self.picPath)
            ListOperation.saveList(self.newList, self.parent.MyList)
            self.accept()

    def mouseMoveEvent(self, event):
        if self.flag == True:
            self.move(Qt.QPoint(self.pos() + event.pos() - self.currentPos))
            self.setCursor(Qt.QCursor(Qt.Qt.SizeAllCursor))

    def mouseReleaseEvent(self,event):
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))
        self.flag = False

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if event.buttons() == QtCore.Qt.LeftButton and 0 < y < 60:
            self.currentPos = event.pos()
            self.setCursor(Qt.QCursor(Qt.Qt.SizeAllCursor))
            self.flag = True