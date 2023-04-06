# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule1.ui'
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
        self.frame.setGeometry(QRect(250, 40, 1471, 1011))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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
"    padding: 5px;"
"font-size:35px;\n"
"font-weight:800;")
        backImage = QPixmap("C:/Student-Interactvie-Design-S.I.D-/sid/images/arrow.png")
        backImage = backImage.scaled(QSize(32,32))
        backPng = QIcon(backImage)
        self.pushButton.setIcon(backPng)


        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1390, 10, 61, 41))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(680, 10, 131, 20))
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-30, 90, 1491, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)

            self.tableWidget.setColumnWidth(0,210)
            self.tableWidget.setColumnWidth(1,210)
            self.tableWidget.setColumnWidth(2,210)
            self.tableWidget.setColumnWidth(3,210)
            self.tableWidget.setColumnWidth(4,210)
            self.tableWidget.setColumnWidth(5,210)
            self.tableWidget.setColumnWidth(6,210)

        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)





        
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)


            self.tableWidget.setRowHeight(0,75)
            self.tableWidget.setRowHeight(1,75)
            self.tableWidget.setRowHeight(2,75)
            self.tableWidget.setRowHeight(3,75)
            self.tableWidget.setRowHeight(4,75)
            self.tableWidget.setRowHeight(5,75)
            self.tableWidget.setRowHeight(6,75)
            self.tableWidget.setRowHeight(7,75)
            self.tableWidget.setRowHeight(8,75)
            self.tableWidget.setRowHeight(9,75)
            self.tableWidget.setRowHeight(10,75)
            self.tableWidget.setRowHeight(11,75)


        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem18)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 100, 1471, 1111))
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

        self.pushButton_2.setText(QCoreApplication.translate("Recordings_2", u"ADD", None))
        self.label.setText(QCoreApplication.translate("Recordings_2", u"Schedule & Calendar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Recordings_2", u"Monday", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Recordings_2", u"Tuesday", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Recordings_2", u"Wednesday", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Recordings_2", u"Thursday", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Recordings_2", u"Friday", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Recordings_2", u"Saturday", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Recordings_2", u"Sunday", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Recordings_2", u"8AM", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Recordings_2", u"9AM", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Recordings_2", u"10AM", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Recordings_2", u"11AM", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Recordings_2", u"12n", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Recordings_2", u"1PM", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Recordings_2", u"2PM", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Recordings_2", u"3PM", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Recordings_2", u"4PM", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Recordings_2", u"5PM", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Recordings_2", u"6PM", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Recordings_2", u"7PM", None));
        self.label_9.setText("")
    # retranslateUi

