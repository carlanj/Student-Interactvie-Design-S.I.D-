# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminders1.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)
from ui import rc_imagesQ

class Ui_Recordings_2(object):
    def setupUi(self, Recordings_2):
        if not Recordings_2.objectName():
            Recordings_2.setObjectName(u"Recordings_2")
        Recordings_2.resize(1824, 917)
        self.frame = QFrame(Recordings_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 40, 1471, 711))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 51, 41))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1390, 10, 61, 41))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(710, 10, 131, 20))
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-30, 90, 1491, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setColumnWidth(0,1475)
        

        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 100, 1471, 611))
        self.tableWidget.setMinimumSize(QSize(1471, 0))
        self.label_9 = QLabel(Recordings_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 1821, 911))
        self.label_9.setStyleSheet(u"background-image: url(:/images/blueHex.png);")
        self.label_9.raise_()
        self.frame.raise_()

        self.retranslateUi(Recordings_2)

        QMetaObject.connectSlotsByName(Recordings_2)
    # setupUi

    def retranslateUi(self, Recordings_2):
        Recordings_2.setWindowTitle(QCoreApplication.translate("Recordings_2", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Recordings_2", u"<--", None))
        self.pushButton_2.setText(QCoreApplication.translate("Recordings_2", u"ADD", None))
        self.label.setText(QCoreApplication.translate("Recordings_2", u"Reminders", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Recordings_2", u"TO-DO", None));

      

        self.label_9.setText("")
    # retranslateUi

