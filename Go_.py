from widgets.MainWindow import PlayerMainWinodw
from functions.Configs import *
from functions import ListOperation
from widgets.musicWidget import MusicWidget
import sys
from PyQt5 import QtCore, QtWidgets, QtGui

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    this = PlayerMainWinodw()
    initconfig()
    this.show()

    sys.exit(app.exec_())