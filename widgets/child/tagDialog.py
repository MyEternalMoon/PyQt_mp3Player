from PyQt5 import QtWidgets,Qt,QtCore
from ui.changeTag import Ui_Form
import eyed3


class tagDialog(QtWidgets.QDialog,Ui_Form):

    def __init__(self,music,parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.setupUi(self)
        self.music = music
        self.parent = parent
        self.setGeometry(370, (self.parent.height()-220)/2, 360, 220)
        self.pushButton.clicked.connect(self.myaccept)
        self.pushButton_2.clicked.connect(self.reject)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.flag = False
        self.title.setText(self.music.name)
        self.aritist.setText(self.music.artist)
        self.album.setText(self.music.album)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)

    def myaccept(self):
        title = self.title.text()
        artist = self.aritist.text()
        album = self.album.text()
        try:
            a = eyed3.mp3.Mp3AudioFile(self.music.path)
            if title != "":
                a.tag.title = title
            if artist != "":
                a.tag.artist = artist
            if album != "":
                a.tag.album = album
            a.tag.save()
        except:
            pass
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
        if event.buttons() == QtCore.Qt.LeftButton and 0 < y < 30:
            self.currentPos = event.pos()
            self.setCursor(Qt.QCursor(Qt.Qt.SizeAllCursor))
            self.flag = True