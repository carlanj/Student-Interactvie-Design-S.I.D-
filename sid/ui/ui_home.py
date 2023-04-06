# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from ui import rc_imagesQ, rc_mic, ui_files, ui_recordings, ui_reminders1, ui_home, ui_schedule, ui_scheduleTest
import test
class Ui_MainWindow(object):


    def hider(self):
        self.hide()

    def goHome(self):
        self.show()

    def escQuit(self):
        QApplication.quit()
        

    



    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1832, 919)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")



        
        self.recButt = QPushButton(MainWindow)
        self.recButt.setObjectName(u"recButt")
        self.recButt.setGeometry(QRect(310, 130, 216, 86))
        self.recButt.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:35px;\n"
"font-weight:800;")
        self.recButt.clicked.connect(self.openRecWindow)
        self.recButt.clicked.connect(self.hider)



        self.remButt = QPushButton(MainWindow)
        self.remButt.setObjectName(u"remButt")
        self.remButt.setGeometry(QRect(1430, 130, 216, 86))
        self.remButt.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    padding: 5px;"
"font-size:35px;\n"
"font-weight:800;")
        self.remButt.clicked.connect(self.openRemWindow)
        self.remButt.clicked.connect(self.hider)


        self.filesButt = QPushButton(MainWindow)
        self.filesButt.setObjectName(u"filesButt")
        self.filesButt.setGeometry(QRect(1430, 750, 216, 86))
        self.filesButt.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    padding: 5px;"
"font-size:35px;\n"
"font-weight:800;")
        self.filesButt.clicked.connect(self.openFilesWindow)
        self.filesButt.clicked.connect(self.hider)


        self.schedButt = QPushButton(MainWindow)
        self.schedButt.setObjectName(u"schedButt")
        self.schedButt.setGeometry(QRect(310, 750, 216, 86))
        self.schedButt.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    padding: 5px;"
"font-size:35px;\n"
"font-weight:800;")
        self.schedButt.clicked.connect(self.openSchedWindow)
        self.schedButt.clicked.connect(self.hider)


        self.hMidLine = QFrame(MainWindow)
        self.hMidLine.setObjectName(u"hMidLine")
        self.hMidLine.setGeometry(QRect(970, 0, 20, 1211))
        self.hMidLine.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(0, 0, 0);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")
        self.hMidLine.setLineWidth(10)
        self.hMidLine.setFrameShape(QFrame.VLine)
        self.hMidLine.setFrameShadow(QFrame.Sunken)
        self.hMidLine.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")


        self.vMidLine = QFrame(MainWindow)
        self.vMidLine.setObjectName(u"vMidLine")
        self.vMidLine.setGeometry(QRect(0, 500, 1961, 20))
        self.vMidLine.setAutoFillBackground(False)
        self.vMidLine.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")
        self.vMidLine.setLineWidth(10)
        self.vMidLine.setMidLineWidth(0)
        self.vMidLine.setFrameShape(QFrame.HLine)
        self.vMidLine.setFrameShadow(QFrame.Sunken)

        self.appButt = QPushButton(MainWindow)
        self.appButt.setObjectName(u"appButt")
        self.appButt.setGeometry(QRect(855, 380, 251, 261))
        self.appButt.setStyleSheet(u" color: #333;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid white;\n"
"    padding: 5px;\n"
"")

        self.micButt = QPushButton(MainWindow)
        self.micButt.setObjectName(u"micButt")
        self.micButt.setGeometry(QRect(915, 440, 130, 140))

        self.micButt.setStyleSheet(u"background-image: url(:/newPrefix/sid/images/mic.png);")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 3821, 2211))
        self.label.setStyleSheet(u"background-image: url(:/images/blueHex.png);")
        self.label.raise_()

        
        MainWindow.setCentralWidget(self.centralwidget)
      
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1832, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

        self.window_list=[]

    def openRecWindow(self):
        self.window = QMainWindow()
        self.ui = ui_recordings.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window_list.append(self.window) 
        self.window.show()
        self.ui.pushButton.clicked.connect(self.close_last_window)
        self.ui.pushButton.clicked.connect(self.goHome)
        self.window.setWindowState(Qt.WindowFullScreen)

    def openRemWindow(self):
        self.window = QMainWindow()
        self.ui = ui_reminders1.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window_list.append(self.window) 
        self.window.show()
        self.ui.pushButton.clicked.connect(self.close_last_window)
        self.ui.pushButton.clicked.connect(self.goHome)
        self.window.setWindowState(Qt.WindowFullScreen)


    def openFilesWindow(self):
        self.window = QMainWindow()
        self.ui = ui_files.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window_list.append(self.window) 
        self.window.show()
        self.ui.pushButton.clicked.connect(self.close_last_window)
        self.ui.pushButton.clicked.connect(self.goHome)
        self.window.setWindowState(Qt.WindowFullScreen)


    def openSchedWindow(self):
        self.window = QMainWindow()
        self.ui = ui_schedule.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window_list.append(self.window) 
        self.window.show()
        self.ui.pushButton.clicked.connect(self.close_last_window)
        self.ui.pushButton.clicked.connect(self.goHome)
        self.window.setWindowState(Qt.WindowFullScreen)




    
    def close_last_window(self):
        last_window=self.window_list[-1]
        self.window_list.remove(last_window)
        last_window.close()






    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.recButt.setText(QCoreApplication.translate("MainWindow", u"Recordings", None))
        self.remButt.setText(QCoreApplication.translate("MainWindow", u"Reminders", None))
        self.filesButt.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.schedButt.setText(QCoreApplication.translate("MainWindow", u"Schedule ", None))
        self.appButt.setText(QCoreApplication.translate("MainWindow", u"APPS", None))
        self.micButt.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label.setText("")
    # retranslateUi

