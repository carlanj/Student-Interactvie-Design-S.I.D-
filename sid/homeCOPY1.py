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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from ui import recordings#, reminders, files, schedule

class Ui_MainWindow(object):
    def openRecWindow(self):
        self.window = QMainWindow()
        self.ui = recordings.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window.show()


    def openRemWindow(self):
        self.window = QMainWindow()
        self.ui = reminders.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window.show()


    def openFilesWindow(self):
        self.window = QMainWindow()
        self.ui = files.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window.show()


    def openSchedWindow(self):
        self.window = QMainWindow()
        self.ui = schedule.Ui_Recordings_2()
        self.ui.setupUi(self.window)
        self.window.show()





    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(776, 623)
        MainWindow.setStyleSheet("background-image: url(D:\D - Work\sid\images\blueHex.png)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Home = QFrame(self.centralwidget)
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(40, 10, 701, 541))
        self.Home.setFrameShape(QFrame.StyledPanel)
        self.Home.setFrameShadow(QFrame.Plain)
        self.Home.setLineWidth(26)


        self.recButt = QPushButton(self.Home)
        self.recButt.setObjectName(u"recButt")
        self.recButt.setGeometry(QRect(80, 100, 191, 61))
        self.recButt.clicked.connect(self.openRecWindow)




        self.remButt = QPushButton(self.Home)
        self.remButt.setObjectName(u"remButt")
        self.remButt.setGeometry(QRect(440, 100, 191, 61))
        self.remButt.clicked.connect(self.openRemWindow)



        self.filesButt = QPushButton(self.Home)
        self.filesButt.setObjectName(u"filesButt")
        self.filesButt.setGeometry(QRect(440, 380, 191, 61))
        self.filesButt.clicked.connect(self.openFilesWindow)


        #-------------------Schedule Button ---------
        self.schedButt = QPushButton(self.Home)
        self.schedButt.setObjectName(u"schedButt")
        self.schedButt.setGeometry(QRect(70, 380, 191, 61))
        self.schedButt.clicked.connect(self.openSchedWindow)



        self.hMidLine = QFrame(self.Home)
        self.hMidLine.setObjectName(u"hMidLine")
        self.hMidLine.setGeometry(QRect(340, -10, 20, 561))
        self.hMidLine.setLineWidth(10)
        self.hMidLine.setFrameShape(QFrame.VLine)
        self.hMidLine.setFrameShadow(QFrame.Sunken)
        self.vMidLine = QFrame(self.Home)
        self.vMidLine.setObjectName(u"vMidLine")
        self.vMidLine.setGeometry(QRect(-13, 270, 721, 20))
        self.vMidLine.setLineWidth(10)
        self.vMidLine.setMidLineWidth(0)
        self.vMidLine.setFrameShape(QFrame.HLine)
        self.vMidLine.setFrameShadow(QFrame.Sunken)
        self.appButt = QPushButton(self.Home)
        self.appButt.setObjectName(u"appButt")
        self.appButt.setGeometry(QRect(310, 240, 71, 71))
        self.micButt = QPushButton(self.Home)
        self.micButt.setObjectName(u"micButt")
        self.micButt.setGeometry(QRect(330, 260, 31, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 776, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.recButt.setText(QCoreApplication.translate("MainWindow", u"Recording", None))
        self.remButt.setText(QCoreApplication.translate("MainWindow", u"Reminders", None))
        self.filesButt.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.schedButt.setText(QCoreApplication.translate("MainWindow", u"Schedule ", None))
        self.appButt.setText(QCoreApplication.translate("MainWindow", u"APPS", None))
        self.micButt.setText(QCoreApplication.translate("MainWindow", u"MIC", None))
    # retranslateUi

