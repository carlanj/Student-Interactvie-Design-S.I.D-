from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic 


class MyGUI(QMainWindow):
        def __init__(self):
                super(MyGUI, self).__init__()
                uic.loadUi("ui/home2.ui", self)
                self.show()

def main():
        app = QApplication([])
        window = MyGUI()
        app.exec_()


if __name__ =='__main__':
        main()