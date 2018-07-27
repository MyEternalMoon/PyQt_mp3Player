from ui.addToList import Ui_Form
from PyQt5 import QtWidgets,Qt


class ListDialog(QtWidgets.QDialog,Ui_Form):
    def __init__(self,parent= None,List=[]):
        super(ListDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
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
