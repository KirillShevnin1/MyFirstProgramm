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
        self.__ui.action_18.triggered.connect(self.Exam)
        self.__ui.action_16.triggered.connect(self.Start)
        self.__ui.action_20.triggered.connect(self.signs_of_pripen)
        self.__ui.lineEditEnterText.textChanged.connect(self.onEnterText)
        self.dict=['']
        self.allSymbols = 0
        self.allTrueSymbols = 0
        self.timerSec = QtCore.QTimer()
        self.timerSec.timeout.connect(self.onTimer)
        self.__ui.lineEditOutputText.setReadOnly(True)
        self.__ui.lineEditEnterText.setReadOnly(True)

    def Start(self):
        self.__ui.lineEditOutputText.setText('')
        self.__ui.lineEditEnterText.setText('')
        self.onEnterText('')
        self.allSymbols = 0
        self.allTrueSymbols = 0
        self.secValue = 5
        self.timerSec.start(1000)
        self.__ui.lineEditEnterText.setReadOnly(False)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            self.__ui.lineEditEnterText.setText('Enter')
            event.accept()

    def onEnterText(self, newText):
        if newText != '':
            self.allSymbols += 1
            a = newText[len(newText) - 1]
            if len(self.__ui.lineEditOutputText.text()) != 0:
                b = self.__ui.lineEditOutputText.text()[len(newText) - 1]
                if a != b:
                    newText = newText.removesuffix(a)
                    self.__ui.lineEditEnterText.setText(newText)
                else:
                    self.allTrueSymbols += 1
        # self.__ui.lineEditOutputText.setText(newText)
        if self.__ui.lineEditEnterText.text() == self.__ui.lineEditOutputText.text():
            # print('y')
            if (len(self.dict) > 0):
                idx = random.randrange(0, len(self.dict))
                self.__ui.lineEditEnterText.setText('')
                self.__ui.lineEditOutputText.setText(self.dict[idx])
                del self.dict[idx]

    def sh_w(self):
        self.dict=["год","дон","облако","солнце","компьютер", "золото", "медведь", "гараж", "закон", "город", "банан",
                   "туман", "жабры", "жаба","йога","ивняк","йогурт","кабак","лабаз","лава","лаваш","арбат",
                   "линзы","халат","цапля","чада","шаг","юг","ювелир","юбка","явка","аббат","абажур","абзац","багет",
                   "багор","багги","база","бадья"]
        #while self.dict:


    def lon_w(self):
        self.dict=["клавиатура","кышка","облако","солнце","рапира","расправа","радар","рапорт","разрыв","разбор",
                   "размер","разгром","растирание","ротатор","радиатор","разработка","рубероид","разоружение",
                   "разнообразие","равноправие","разодрать","раздробить"]

    def onTimer(self):
        self.__ui.lineEdit_2.setText(str(self.secValue))
        self.secValue -= 1
        if self.secValue == -1:
            self.timerSec.stop()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText("Натыкано правильных знаков: " + str(self.allTrueSymbols) + "\n" +
                           f"Натыкано не правильных знаков: {self.allSymbols - self.allTrueSymbols}\n")
            msgBox.setWindowTitle("Время вышло")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            returnValue = msgBox.exec()
            if returnValue == QtWidgets.QMessageBox.Yes:
                self.reset()
            else:
                self.__ui.lineEditEnterText.setText("")
                self.__ui.lineEditOutputText.setText("")


    def reset(self):
        self.Start()
        #self.timerSec.start(1000)

    def Exam(self):
        self.dict = ["год","дон","облако","солнце","компьютер", "золото", "медведь", "гараж", "закон", "город", "банан", "туман",
                     "клавиатура","мышка","облако","солнце","рапира","расправа","радар","рапорт","разрыв","разбор","размер","разгром","растирание",
                     "ротатор", "радиатор", "разработка", "рубероид", "разоружение", "разнообразие", "равноправие",
                     "разодрать", "раздробить"]

    def signs_of_pripen(self):
        self.dict = [",,,",",,,...","..",".,","..,,", "я,", "ты,", "он,", "она.", "А.С. Пушкин и др,.", "и","пр.,","Сон,","бал,","Файл,","зуб и т. п.,", "и т.","в.","т.",
                     ",,;,;",";,;,;","а,","б;","в,","Г;",",;,;,",";,,;","да,","Ага;","моря;"]







