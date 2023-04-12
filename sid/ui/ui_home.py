# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import pyttsx3 #Text to Speech
import datetime
import speech_recognition as sr
import smtplib
import cv2
import wikipedia
import webbrowser as wb
import pywhatkit
import requests
import clipboard
import os
import time 
import pyautogui
import random 
import psutil 
import cv2
import tkinter as Tk

import webbrowser as wb

from tkinter import Label
from tkinter import PhotoImage
from tkinter import Button
from PIL import Image
from PySide6.QtWidgets import QApplication, QWidget
#from secrets import senderemail, epwd, to
import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from playsound import playsound


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QScreen
import datetime
from PyQt5.QtGui import QScreen, QGuiApplication
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTime, QUrl
from PyQt5.QtMultimedia import QMediaRecorder, QCameraInfo, QCamera


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


        self.appFrame = QFrame(MainWindow)
        self.appFrame.setObjectName(u"appFrame")
        self.appFrame.setGeometry(QRect(755, 330, 251, 261))
        self.appFrame.setStyleSheet(u" color: #333;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid white;\n"
"    padding: 5px;\n"
"")

        self.recordButton = QPushButton(MainWindow)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setGeometry(QRect(835, 360, 86, 46))
        self.recordButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    padding: 5px;"
"font-size:25px;\n"
"font-weight:800;")
        self.recordButton.raise_()


        self.micButton = QPushButton(MainWindow)
        self.micButton.setObjectName(u"micButton")
        self.micButton.setGeometry(QRect(835, 440, 86, 46))
        self.micButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    padding: 5px;"
"font-size:25px;\n"
"font-weight:800;")
        self.micButton.raise_()
        micImage = QPixmap(r"sid/images/mic.png")
        micImage = micImage.scaled(QSize(32,32))
        micPng = QIcon(micImage)
        self.micButton.setIcon(micPng)
        self.micButton.clicked.connect(self.start_listening)



        self.appsButton = QPushButton(MainWindow)
        self.appsButton.setObjectName(u"appsButton")
        self.appsButton.setGeometry(QRect(835, 520, 86, 46))
        self.appsButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"    border-radius: 120px;\n"
"    border-style: outset;\n"
"   border: 2px solid blue;\n"
"    padding: 5px;"
"font-size:25px;\n"
"font-weight:800;")
        self.appsButton.raise_()
        self.appsButton.clicked.connect(self.appShower)


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
"font-size:25px;\n"
"font-weight:800;")
        self.recButt.clicked.connect(self.openRecWindow)
        self.recButt.clicked.connect(self.hider)



        self.remButt = QPushButton(MainWindow)
        self.remButt.setObjectName(u"remButt")
        self.remButt.setGeometry(QRect(1230, 130, 216, 86))
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
        self.filesButt.setGeometry(QRect(1230, 700, 216, 86))
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
        self.schedButt.setGeometry(QRect(310, 700, 216, 86))
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


        self.vMidLine = QFrame(MainWindow)
        self.vMidLine.setObjectName(u"leftMidLine")
        self.vMidLine.setGeometry(QRect(870, 0, 20, 330))
        self.vMidLine.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(0, 0, 0);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")
        self.vMidLine.setLineWidth(10)
        self.vMidLine.setFrameShape(QFrame.VLine)
        self.vMidLine.setFrameShadow(QFrame.Sunken)
        self.vMidLine.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")


        self.vMidLine2 = QFrame(MainWindow)
        self.vMidLine2.setObjectName(u"vMidLine2")
        self.vMidLine2.setGeometry(QRect(870, 600, 20, 675))
        self.vMidLine2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(0, 0, 0);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")
        self.vMidLine2.setLineWidth(10)
        self.vMidLine2.setFrameShape(QFrame.VLine)
        self.vMidLine2.setFrameShadow(QFrame.Sunken)
        self.vMidLine2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")



        self.leftMidLine = QFrame(MainWindow)
        self.leftMidLine.setObjectName(u"leftMidLine")
        self.leftMidLine.setGeometry(QRect(10, 450, 750, 20))
        self.leftMidLine.setAutoFillBackground(False)
        self.leftMidLine.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")
        self.leftMidLine.setLineWidth(10)
        self.leftMidLine.setMidLineWidth(0)
        self.leftMidLine.setFrameShape(QFrame.HLine)
        self.leftMidLine.setFrameShadow(QFrame.Sunken)





        self.rightMidLine = QFrame(MainWindow)
        self.rightMidLine.setObjectName(u"rightMidLine")
        self.rightMidLine.setGeometry(QRect(1000, 450, 850, 20))
        self.rightMidLine.setAutoFillBackground(False)
        self.rightMidLine.setStyleSheet(u"background-color: rgb(255\, 255, 255);\n"
" border: 2px solid blue;\n"
"    border-radius: 60px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"   border: 2px solid blue;\n"
"    padding: 5px;")
        self.rightMidLine.setLineWidth(10)
        self.rightMidLine.setMidLineWidth(0)
        self.rightMidLine.setFrameShape(QFrame.HLine)
        self.rightMidLine.setFrameShadow(QFrame.Sunken)

    

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

        self.name = ""



    def start_listening(self):
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
                print("Listening...")
                
                engine = pyttsx3.init()

                engine.say("Hello, How may I help You")
                engine.runAndWait()

                self.stop_listening = self.recognizer.listen_in_background(
                    self.microphone, self.on_recognize)

    def on_recognize(self, recognizer, audio):
        engine = pyttsx3.init()

        try:
            recognized_text = recognizer.recognize_google(audio)
            recognized_text = recognized_text.split()
            print(f"Recognized text: {recognized_text}")

            if "hello" in recognized_text:
                engine.say("Hello Sir")
                engine.runAndWait()

            elif "time" in recognized_text:
                Time = datetime.datetime.now().strftime("%I:%M") #Hour/Minute
                engine.say("The Time is Currently: " +str(Time))
                engine.runAndWait()

            elif "date" in recognized_text:
                months = {1:"january", 2:"february", 3:"march", 4:"april", 5:"may", 6:"june", 7:"july", 8:"august", 9:"september", 10:"october", 11:"november", 12:"december"}
                year = int(datetime.datetime.now().year)            
                month = int(datetime.datetime.now().month)
                date = int(datetime.datetime.now().day)

                engine.say("Today's date is: " + months[month] + str(date) + str(year))
                engine.runAndWait()


            elif "screenshot" in recognized_text:
                self.hider()
                name_img = time.time()
                name_img = f'sid/sidSaved/{name_img}.png'
                img = pyautogui.screenshot(name_img)
                img.show()

            elif "search" in recognized_text:
                self.hider()
                search = recognized_text
                del search[0]
                search = " ".join(search)
                wb.open('https://www.google.com/search?q=' + search)
                engine.say("Searching")
                engine.runAndWait()


            elif "return" in recognized_text:
                self.goHome()
                
                
              
        except sr.UnknownValueError:

            print("Google Speech Recognition could not understand audio")
            print("Listening...")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")



    
    def activate(self):
        self.showNormal()  # make sure the window is not minimized
        self.activateWindow()
        self.raise_()
        self.setFocus(Qt.OtherFocusReason)


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
    def speaker(self,message):
        print(message)

        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()

        time.sleep(1)


    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.recButt.setText(QCoreApplication.translate("MainWindow", u"Recordings", None))
        self.remButt.setText(QCoreApplication.translate("MainWindow", u"Reminders", None))
        self.filesButt.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.schedButt.setText(QCoreApplication.translate("MainWindow", u"Schedule ", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"REC", None))
        self.appsButton.setText(QCoreApplication.translate("MainWindow", u"APPS", None))


    # retranslateUi

    