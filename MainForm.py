from MyMainForm import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import random
class MyMainForm(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.showMaximized()
        self.__ui.action_14.triggered.connect(self.sh_w)
        self.__ui.action_15.triggered.connect(self.lon_w)
        self.__ui.action_16.triggered.connect(self.Start)
        self.__ui.lineEditEnterText.textChanged.connect(self.onEnterText)
        self.dict=['']
        self.timerSec = QtCore.QTimer()
        self.timerSec.timeout.connect(self.onTimer)
        self.reset()

    def Start(self):
        self.__ui.lineEditOutputText.setText('')
        self.__ui.lineEditEnterText.setText('')
        self.onEnterText('')

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.__ui.lineEditEnterText.setText('Enter')
            event.accept()

    def onEnterText(self, newText):
         #self.__ui.lineEditOutputText.setText(newText)
         if self.__ui.lineEditEnterText.text() == self.__ui.lineEditOutputText.text():
             print('y')
             idx = random.randrange(0, len(self.dict))
             self.__ui.lineEditOutputText.setText(self.dict[idx])
             del self.dict[idx]
             self.__ui.lineEditEnterText.setText('')

    def sh_w(self):
        self.dict=["Год","Дон","Облако","Солнце","Компьютер", "Золото", "Медведь", "Гараж", "Закон", "Город", "Банан", "Туман"]
        #while self.dict:


    def lon_w(self):
        self.dict=["Клавиатура","Мышка","Облако","Солнце","Компьютер"]

    def onTimer(self):
        self.__ui.lineEdit_2.setText(str(self.secValue))
        self.secValue-=1
        if self.secValue ==-1:
            self.timerSec.stop()

    def reset(self):
        self.secValue = 60
        self.timerSec.start(1000)







