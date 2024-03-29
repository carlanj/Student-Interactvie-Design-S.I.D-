# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'files1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QDir,QSortFilterProxyModel,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,QFileDialog,
    QTableWidgetItem, QWidget,QFileSystemModel,QTreeView)
from ui import rc_imagesQ
from PyQt6 import QtCore, QtGui, QtWidgets
import os 
import datetime
import time
import arrow
import random
class Ui_Recordings_2(object):

    def sorter(self):
        proxy_model = QSortFilterProxyModel()
        proxy_model.setSourceModel(self.file_model)
        self.tree_view.setModel(proxy_model)

        # sort the items in the tree view widget
        proxy_model.sort(0, order=Qt.AscendingOrder)

    def createFile(self):
        current_time = random.randint(0, 100)
        # Set the file path and name
        file_path = "sidSaved/ANew" + str(current_time) + ".txt"

        # Define the content of the file
        file_content = "This is the content of my new file!"

        # Create the file and write the content to it
        with open(file_path, "w") as file:
            file.write(file_content)



    def remover(self):
        # get the selected index from the tree view
        selected_index = self.tree.currentIndex()

        # delete the file or folder at the selected index
        file_system_model = self.tree.model()
        file_system_model.remove(selected_index)
    


    def setupUi(self, Recordings_2):
        if not Recordings_2.objectName():
            Recordings_2.setObjectName(u"Recordings_2")
        Recordings_2.resize(1824, 917)
        self.frame = QFrame(Recordings_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(130, 40, 1471, 1050))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);border-radius: 50px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        dir_path = "sidSaved"

        self.model = QFileSystemModel(self.frame)
        self.model.setRootPath(dir_path)

        self.tree =  QTreeView(self.frame)
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dir_path))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)
        self.tree.setGeometry(QRect(0, 100, 1471, 1111))

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
        backImage = QPixmap("images/arrow.png")
        backImage = backImage.scaled(QSize(32,32))
        backPng = QIcon(backImage)
        self.pushButton.setIcon(backPng)
        

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 10, 61, 51))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
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
        addImage = QPixmap("images/add.png")
        addImage = addImage.scaled(QSize(32,32))
        addPng = QIcon(addImage)
        self.pushButton_2.setIcon(addPng)
        self.pushButton_2.clicked.connect(self.createFile)




        self.trashButton = QPushButton(self.frame)
        self.trashButton.setObjectName(u"trashButton")
        self.trashButton.setGeometry(QRect(240, 10, 61, 51))
        self.trashButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
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
        trashImage = QPixmap("images/trash.png")
        trashImage = trashImage.scaled(QSize(32,32))
        trashPng = QIcon(trashImage)
        self.trashButton.setIcon(trashPng)
        self.trashButton.clicked.connect(self.remover)


     






        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(680, 10, 131, 20))
        self.label.setGeometry(QRect(670, -10, 381, 100))
        self.label.setStyleSheet("font-size: 60px; color: blue;")


        

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
        self.label.setText(QCoreApplication.translate("Recordings_2", u"Files", None))
      
        self.label_9.setText("")
    # retranslateUi
class Center(object):
    def centerWID(self):
            qr=self.frameGeometry()           
            cp=QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

