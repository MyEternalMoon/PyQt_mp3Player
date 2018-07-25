from widgets.child.firstDialog import firstDialog
from PyQt5 import QtWidgets,Qt
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    o = firstDialog()
    o.show()
    sys.exit(app.exec_())