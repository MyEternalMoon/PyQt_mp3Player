import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from widgets.MainWindow import PlayerMainWinodw
from functions.Configs import *
from functions import ListOperation




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    this = PlayerMainWinodw()
    this.show()

    sys.exit(app.exec_())