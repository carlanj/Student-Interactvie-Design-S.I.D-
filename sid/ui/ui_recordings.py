# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordings1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import numpy as np
import imageio
import pyscreenshot as ImageGrab

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

    def add_row(self):
        rowCount = self.tableWidget.rowCount()  # get current row count
        self.tableWidget.insertRow(rowCount)  # insert new row at end
        newItem = QTableWidgetItem("New Item")
        self.tableWidget.setItem(rowCount, 0, newItem)

    def recorder(self):
        filename = "screen_capture.mp4"
        fps = 30.0

        with imageio.get_writer(filename, fps=fps) as writer:
            while True:
                try:
                    # Take a screenshot
                    im = ImageGrab.grab()

                    # Convert to numpy array
                    im = np.array(im)

                    # Add to the video writer
                    writer.append_data(im)

                except KeyboardInterrupt:
                    # Stop recording on keyboard interrupt
                    break



    def setupUi(self, Recordings_2):
        if not Recordings_2.objectName():
            Recordings_2.setObjectName(u"Recordings_2")
        Recordings_2.resize(1824, 917)
        self.frame = QFrame(Recordings_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 40, 1471, 1050))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius: 50px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 61, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    ptrashing: 5px;"
"font-size:35px;\n"
"font-weight:800;")
        backImage = QPixmap("images/arrow.png")
        backImage = backImage.scaled(QSize(32,32))
        backPng = QIcon(backImage)
        self.pushButton.setIcon(backPng)


        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1390, 10, 61, 51))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    ptrashing: 5px;"
"font-size:35px;\n"
"font-weight:800;")
        trashImage = QPixmap("images/trash.png")
        trashImage = trashImage.scaled(QSize(32,32))
        trashPng = QIcon(trashImage)
        self.pushButton_2.setIcon(trashPng)


        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, -10, 381, 100))
        self.label.setStyleSheet("font-size: 60px; color: blue;")
       
        


        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-30, 90, 1491, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)

            self.tableWidget.setColumnWidth(0,210)
            self.tableWidget.setColumnWidth(1,1010)
            self.tableWidget.setColumnWidth(2,290)

        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)



        
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 100, 1471, 1010))
        self.tableWidget.setMinimumSize(QSize(1471, 0))
        self.label_9 = QLabel(Recordings_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 3821, 2211))
        self.label_9.setStyleSheet(u"background-image: url(:/images/blueHex.png);")
        self.label_9.raise_()
        self.frame.raise_()

        self.retranslateUi(Recordings_2)

        QMetaObject.connectSlotsByName(Recordings_2)
    # setupUi

    def retranslateUi(self, Recordings_2):
        Recordings_2.setWindowTitle(QCoreApplication.translate("Recordings_2", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Recordings_2", u"Recordings", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Recordings_2", u"Video Length", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Recordings_2", u"Lecture TItle", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Recordings_2", u"Date Recorded", None));
        
       
        self.label_9.setText("")
    # retranslateUi

