from PySide6 import QtWidgets  
from PySide6.QtWidgets import QApplication
import threading
import speech_recognition as sr
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PyQt6.QtGui import QScreen,QGuiApplication
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton

from ui import ui_home
from ui.ui_home import Ui_MainWindow
from playsound import playsound
import pyttsx3
class Home(ui_home.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Home,self).__init__()
        self.setupUi(self)
        self.window_list=[]
        self.setWindowState(Qt.WindowFullScreen)

        escButt = QShortcut(QKeySequence(Qt.Key_Escape), self)
        escButt.activated.connect(self.escQuit)

 



       





    def escQuit(self):
        QApplication.quit()

    



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = Home()
    qt_app.show()
    app.exec() 
