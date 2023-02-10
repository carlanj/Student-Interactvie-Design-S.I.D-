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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1832, 919)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Home = QFrame(self.centralwidget)
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(250, 70, 1401, 691))
        self.Home.setFrameShape(QFrame.StyledPanel)
        self.Home.setFrameShadow(QFrame.Plain)
        self.Home.setLineWidth(26)
        self.recButt = QPushButton(self.Home)
        self.recButt.setObjectName(u"recButt")
        self.recButt.setGeometry(QRect(210, 160, 191, 61))
        self.remButt = QPushButton(self.Home)
        self.remButt.setObjectName(u"remButt")
        self.remButt.setGeometry(QRect(950, 160, 191, 61))
        self.filesButt = QPushButton(self.Home)
        self.filesButt.setObjectName(u"filesButt")
        self.filesButt.setGeometry(QRect(940, 500, 191, 61))
        self.schedButt = QPushButton(self.Home)
        self.schedButt.setObjectName(u"schedButt")
        self.schedButt.setGeometry(QRect(200, 520, 191, 61))
        self.hMidLine = QFrame(self.Home)
        self.hMidLine.setObjectName(u"hMidLine")
        self.hMidLine.setGeometry(QRect(670, -20, 20, 721))
        self.hMidLine.setLineWidth(10)
        self.hMidLine.setFrameShape(QFrame.VLine)
        self.hMidLine.setFrameShadow(QFrame.Sunken)
        self.vMidLine = QFrame(self.Home)
        self.vMidLine.setObjectName(u"vMidLine")
        self.vMidLine.setGeometry(QRect(0, 340, 1441, 20))
        self.vMidLine.setLineWidth(10)
        self.vMidLine.setMidLineWidth(0)
        self.vMidLine.setFrameShape(QFrame.HLine)
        self.vMidLine.setFrameShadow(QFrame.Sunken)
        self.appButt = QPushButton(self.Home)
        self.appButt.setObjectName(u"appButt")
        self.appButt.setGeometry(QRect(640, 310, 71, 71))
        self.micButt = QPushButton(self.Home)
        self.micButt.setObjectName(u"micButt")
        self.micButt.setGeometry(QRect(660, 330, 31, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1832, 26))
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

