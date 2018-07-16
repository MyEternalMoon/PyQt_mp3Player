from PyQt5 import QtWidgets,QtGui
from ui.musicWidget import Ui_Form
from functions import getMp3

class MusicWidget(QtWidgets.QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.listWidget.addItem("功能建设中！")
        self.show()
