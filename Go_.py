import sys
from eyed3 import mp3
from PyQt5 import QtWidgets,QtCore, Qt
from widgets.MainWindow import PlayerMainWindow
import time


def main():
    app = QtWidgets.QApplication(sys.argv)
    this = PlayerMainWindow()
    this.show()
    sys.exit(app.exec_())


# class Loading(QtWidgets.QWidget, Ui_Form):
#     def __init__(self, parent=None):
#         super(Loading, self).__init__()
#         self.trueparent = parent
#         self.setupUi(self)
#         self.timer = QtCore.QTimer()
#         self.timer.timeout.connect(self.processing)
#         self.timer.setInterval(100)
#         self.timer.start()
#         self.setWindowFlags(Qt.Qt.FramelessWindowHint)
#         self.setAttribute(Qt.Qt.WA_TranslucentBackground)
#         self.v = 0
#
#     def processing(self):
#         self.v += 100
#         self.progressBar.setValue(self.v / 25)
#         if self.v == 1500:
#             self.show_main()
#
#     def show_main(self):
#         self.hide()


if __name__ == "__main__":
    main()
