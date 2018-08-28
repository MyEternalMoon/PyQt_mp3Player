from ui import checkDialog
from PyQt5 import QtWidgets,Qt

class sureDialog(QtWidgets.QDialog,checkDialog.Ui_Dialog):
    def __init__(self,parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.Window)
        self.setWindowModality(Qt.Qt.WindowModal)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.acceptButton.clicked.connect(self.accept)
        self.rejectButton.clicked.connect(self.reject)
