from ui.addToList import Ui_Form
from PyQt5 import QtWidgets,Qt,QtCore


class ListDialog(QtWidgets.QDialog,Ui_Form):
    def __init__(self, List=[],parent = None):
        super(ListDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)

        self.List = List
        self.ListSelected = None
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.aButton.clicked.connect(self.Myaccept)
        self.rButton.clicked.connect(self.reject)


    def initInterface(self):
        self.listWidget.clear()
        for i in self.List:
            self.listWidget.addItem(i.name)

    def Myaccept(self):
        self.ListSelected = self.listWidget.currentRow()
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
        if event.buttons() == QtCore.Qt.LeftButton and 0 < y < 40:
            self.currentPos = event.pos()
            self.setCursor(Qt.QCursor(Qt.Qt.SizeAllCursor))
            self.flag = True