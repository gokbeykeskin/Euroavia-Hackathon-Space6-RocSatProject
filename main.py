# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys #
from PyQt5 import QtWidgets #
from PyQt5 import QtCore #
from PyQt5.QtWidgets import * #
from PyQt5.QtGui import * #
from PyQt5 import * #
from PyQt5.QtCore import * #    
import data #
import map  #
from satSim import start_sattelite_sim  #

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.time = 0
        data.parse_data('Flight_data_1.csv') #
        self.curr_mass = float(data.mass[0])
        self.curr_velov = float(data.vertV[0])
        self.curr_veloh = float(data.lateralV[0])
        self.curr_alt = float(data.altitude[0])
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 730)
        MainWindow.setAutoFillBackground(False)
        
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(0, 0, 0);")    
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(200, 620, 491, 22))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: red;\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: pink;\n"
"}\n"
"")
        self.horizontalSlider.setProperty("value", self.time)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged[int].connect(self.updateUi) #
        self.horizontalSlider.setMaximum(len(data.time) - 1) #
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 260, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 440, 171, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(770, 380, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(770, 260, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(770, 440, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 620, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 711, 41))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.r1 = QtWidgets.QLabel(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(400, 200, 31, 31))
        self.r1.setText("")
        self.r1.setPixmap(QtGui.QPixmap("resources/red_1_30x30.png"))
        self.r1.setObjectName("r1")
        self.g1 = QtWidgets.QLabel(self.centralwidget)
        self.g1.setGeometry(QtCore.QRect(400, 200, 31, 31))
        self.g1.setText("")
        self.g1.setPixmap(QtGui.QPixmap("resources/green_30x30.png"))
        self.g1.setObjectName("g1")
        self.g1_2 = QtWidgets.QLabel(self.centralwidget)
        self.g1_2.setGeometry(QtCore.QRect(550, 200, 31, 31))
        self.g1_2.setText("")
        self.g1_2.setPixmap(QtGui.QPixmap("resources/green_30x30.png"))
        self.g1_2.setObjectName("g1_2")
        self.r2 = QtWidgets.QLabel(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(550, 200, 31, 31))
        self.r2.setText("")
        self.r2.setPixmap(QtGui.QPixmap("resources/red_1_30x30.png"))
        self.r2.setObjectName("r2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(390, 130, 51, 51))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("resources/uydu_1_45x45.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(540, 140, 51, 41))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("resources/parachute_45x45.png"))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(260, 430, 61, 51))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("resources/T_000.0_s_2_1_75x50.png"))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(500, 430, 61, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("resources/T_000.0_s_3_1_75x50.png"))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(340, 450, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(580, 450, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(260, 510, 61, 51))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("resources/T_000.0_s_4_75x50.png"))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(340, 530, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(500, 510, 61, 51))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("resources/T_000.0_s_5_75x50.png"))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(580, 530, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(920, 630, 31, 41))
        self.label_21.setStyleSheet("QLabel::indicator:indeterminate:hover{\n"
"    \n"
"}")
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("resources/T_000.0_s_6_1_60x45.png"))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_21.setStyleSheet("color: white;")
        self.label_21.setToolTip("TMP: Temperature\nAPR: Air Pressure\nDRF: Drug Force\nTHR: Thrust Force\nVEL: Velocity\nALT: Altitude\nVEV: Vertical Velocity\nVEA: Vertical Acceleration")#
        self.label_21.setToolTipDuration(500000)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(20, 30, 111, 101))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("resources/logo.png"))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 610, 41, 41))
        self.pushButton_3.setStyleSheet("background-color:white;\n"
"border: 1px grey solid;\n"
"border-radius: 20px;\n"
"")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 300, 191, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_2.clicked.connect(self.sattelite_thread) #
        

        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(163, 163, 163);\n"
"border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 300, 191, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton.setBaseSize(QtCore.QSize(40, 40))
        self.pushButton.clicked.connect(map.start2dMap) #
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(163, 163, 163);\n"
"border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 969, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_3.setObjectName("playButton")
        self.pushButton_3.clicked.connect(self.startTimer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TMP C"))
        self.label_4.setText(_translate("MainWindow", "APR mbar"))
        self.label_5.setText(_translate("MainWindow", "DRF N"))
        self.label_6.setText(_translate("MainWindow", "THR Placeholder N"))
        self.label_7.setText(_translate("MainWindow", "ALT Placeholder m"))
        self.label_8.setText(_translate("MainWindow", "VEV Placeholder m/s"))
        self.label_3.setText(_translate("MainWindow", "VEL Placeholder m/s"))
        self.label_9.setText(_translate("MainWindow", "VEA Placeholder m/s^2"))
        self.label_10.setText(_translate("MainWindow", "T +0000s"))
        self.label.setText(_translate("MainWindow", "ROCKET LAUNCH"))
        self.label_15.setText(_translate("MainWindow", "Placeholder m/s"))
        self.label_16.setText(_translate("MainWindow", "Placeholder m/s"))
        self.label_18.setText(_translate("MainWindow", "Placeholder g"))
        self.label_20.setText(_translate("MainWindow", "Placeholder m/s"))
        self.pushButton_3.setText(_translate("MainWindow", "Next"))
        self.pushButton_2.setText(_translate("MainWindow", "3D Visualization"))
        self.pushButton.setText(_translate("MainWindow", "Realtime Coordinate"))

    def updateUi(self): #
        self.curr_velov = float(data.vertV[int(self.horizontalSlider.value())])
        self.curr_veloh = float(data.lateralV[int(self.horizontalSlider.value())])
        self.curr_alt = float(data.altitude[int(self.horizontalSlider.value())])
        self.curr_mass = float(data.mass[int(self.horizontalSlider.value())])
        _translate = QtCore.QCoreApplication.translate #
        self.label_2.setText(_translate("MainWindow", 'TMP ' + data.airTemp[int(self.horizontalSlider.value())] + 'C')) #
        self.label_4.setText(_translate("MainWindow", 'APR ' + data.airPres[int(self.horizontalSlider.value())] + ' mbar')) #
        self.label_5.setText(_translate("MainWindow", 'DFR ' + data.dragForce[int(self.horizontalSlider.value())] + ' N')) #
        self.label_6.setText(_translate("MainWindow", 'THR ' + data.thrust[int(self.horizontalSlider.value())] + ' N')) #
        self.label_7.setText(_translate("MainWindow", 'ALT ' + data.altitude[int(self.horizontalSlider.value())] + ' m')) #
        self.label_8.setText(_translate("MainWindow", 'VEV ' + data.vertV[int(self.horizontalSlider.value())] + ' m/s')) #
        self.label_3.setText(_translate("MainWindow", 'VEL ' + data.totalV[int(self.horizontalSlider.value())] + ' m/s')) #
        self.label_9.setText(_translate("MainWindow", 'VEA ' + data.vertA[int(self.horizontalSlider.value())] + ' m/s^2')) #
        self.label_10.setText(_translate("MainWindow", "T +" + data.time[int(self.horizontalSlider.value())] + "s")) #
        self.label_16.setText(_translate("MainWindow", data.longitude[int(self.horizontalSlider.value())] + " ??")) #
        self.label_18.setText(_translate("MainWindow", data.mass[int(self.horizontalSlider.value())] + " g")) #
        self.label_20.setText(_translate("MainWindow", data.windV[int(self.horizontalSlider.value())] + " m/s"))
        self.label_15.setText(_translate("MainWindow", data.latitude[int(self.horizontalSlider.value())] + " ??")) #

    def sattelite_sim(self):
        start_sattelite_sim(self.curr_velov, self.curr_veloh, self.curr_alt, self.curr_mass)

    def sattelite_thread(self):
        self.thread = QThread()
        self.thread.started.connect(self.sattelite_sim)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def startTimer(self):
        self.nextTime()


    def nextTime(self):
        self.buttonStat = False
        if(self.horizontalSlider.value() != len(data.time)-1):
                self.horizontalSlider.setProperty("value", self.horizontalSlider.value() + 1)

                

if __name__ == "__main__": #
    app = QtWidgets.QApplication(sys.argv) #
    MainWindow = QtWidgets.QMainWindow() #
    ui = Ui_MainWindow() #
    ui.setupUi(MainWindow) #
    MainWindow.show() #
    
    sys.exit(app.exec_()) #
