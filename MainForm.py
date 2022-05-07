from MyMainForm import Ui_MainWindow
from PyQt5 import QtWidgets

class MyMainForm(QtWidgets.QMainWindow):

 def __init__(self):
    super().__init__()
    self.__ui = Ui_MainWindow()
    self.__ui.setupUi(self)
    self.showMaximized()
    self.__ui.action_16.triggered.connect(self.Start)

 def Start(self):
    self.__ui.lineEdit.setText("")


