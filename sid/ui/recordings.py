# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordings.ui'
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
from PySide6.QtWidgets import (QApplication, QColumnView, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Recordings_2(object):
    def setupUi(self, Recordings_2):
        if not Recordings_2.objectName():
            Recordings_2.setObjectName(u"Recordings_2")
        Recordings_2.resize(1105, 723)
        Recordings_2.setStyleSheet("background-image: url(images/blueHex.png)")


        self.Recordings = QFrame(Recordings_2)
        self.Recordings.setObjectName(u"Recordings")
        self.Recordings.setGeometry(QRect(40, 30, 1031, 661))
        self.Recordings.setAutoFillBackground(False)
        self.Recordings.setFrameShape(QFrame.StyledPanel)
        self.Recordings.setFrameShadow(QFrame.Raised)
        self.columnView = QColumnView(self.Recordings)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setGeometry(QRect(0, 0, 1031, 661))
        self.line = QFrame(self.Recordings)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(90, -140, 20, 811))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.Recordings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-100, 90, 1171, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.Recordings)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(940, 0, 20, 811))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.Recordings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 10, 71, 16))
        self.label_2 = QLabel(self.Recordings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 80, 71, 16))
        self.label_3 = QLabel(self.Recordings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 81, 20))
        self.label_4 = QLabel(self.Recordings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(980, 70, 31, 21))
        self.pushButton = QPushButton(self.Recordings)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 51, 41))
        self.pushButton_2 = QPushButton(self.Recordings)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(960, 10, 61, 41))

        self.retranslateUi(Recordings_2)

        QMetaObject.connectSlotsByName(Recordings_2)
    # setupUi

    def retranslateUi(self, Recordings_2):
        Recordings_2.setWindowTitle(QCoreApplication.translate("Recordings_2", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Recordings_2", u"RECORDINGS", None))
        self.label_2.setText(QCoreApplication.translate("Recordings_2", u"VIDEO TITLE", None))
        self.label_3.setText(QCoreApplication.translate("Recordings_2", u"VIDEO LENGTH", None))
        self.label_4.setText(QCoreApplication.translate("Recordings_2", u"DATE", None))
        self.pushButton.setText(QCoreApplication.translate("Recordings_2", u"<--", None))
        self.pushButton_2.setText(QCoreApplication.translate("Recordings_2", u"TRASH", None))
    # retranslateUi

