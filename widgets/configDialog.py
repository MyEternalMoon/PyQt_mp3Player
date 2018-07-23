from ui.config import Ui_Form
from PyQt5 import QtWidgets,Qt

class configWidget(QtWidgets.QWidget,Ui_Form):
    def __init__(self,parent = None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        #self.setAttribute(Qt.Qt.WA_TranslucentBackground)