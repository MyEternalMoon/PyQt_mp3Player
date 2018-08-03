from ui import checkDialog
from PyQt5 import QtWidgets,QtGui,Qt

class sureDialog(QtWidgets.QDialog,checkDialog.Ui_Dialog):
    def __init__(self,index,parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setGeometry(370, (self.parent.height()-180)/2, 360, 180)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.acceptButton.clicked.connect(self.accept)
        self.rejectButton.clicked.connect(self.reject)
        self.label.setText("确认要删除歌单《%s》吗？"%index)

