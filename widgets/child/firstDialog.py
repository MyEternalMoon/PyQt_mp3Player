from PyQt5 import QtWidgets,Qt
from faker import Faker
from ui.firstWidget import Ui_Form
from functions import Configs

class firstDialog(QtWidgets.QDialog,Ui_Form):
    def __init__(self,parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.f = Faker (locale="zh-CN")
        self.parent= parent
        self.setupUi(self)
        self.store = "D:/DMplayer"
        self.music = self.store + "/music"
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.init_memory_info()

        self.randomButton.clicked.connect(self.get_random_name)
        self.pushButton1.clicked.connect(self.change_mainstorage)
        self.pushButton2.clicked.connect(self.oo)
        self.checkBox.clicked.connect(self.change_locale)

    def change_locale(self):
        if self.checkBox.isChecked():
            self.f = Faker(locale="en_US")
        else:
            self.f = Faker(locale="zh_CN")
        self.lineEdit.clear()

    def change_mainstorage(self):
        mess = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹", "D:")
        if mess[0] != "":
            self.store = mess[0]+"/DMPlayer"
            self.init_memory_info()

    def change_musicstorage(self):
        mess2 = QtWidgets.QFileDialog.getExistingDirectory(self,"选择文件夹","D:")
        if mess2[0] != "":
            self.musci = mess2[0]
            self.init_memory_info()

    def init_memory_info(self):
        self.label1.setText("我们将创建一个新文件夹:%s"%(self.store))
        self.label2.setText("也许需要设置本地音乐位置:%s"%(self.music))
        self.label3.setText("我们把图像文件储存在这里:%s"%(self.store+"/Head"))

    def get_random_name(self):
        self.lineEdit.setText(self.f.name().split(" ")[0])

    def package_info(self):
        '''将打包所有信息'''
        name = self.lineEdit.text()
        return [self.store,self.music,self.store+"/Head",name]

    def oo(self):
        print(Configs.first_create_config(self.package_info()))

