from PySide6 import QtWidgets  

from ui import home, recordings, ui_home

class Home(home.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Home,self).__init__()
        self.setupUi(self)




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = Home()
    qt_app.show()
    app.exec()



