# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataDisplayUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#

from PyQt5 import QtCore, QtGui, QtWidgets
from myLed import MyLed

class Ui_dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(900, 900)

        self.LineDisplayGB1 = QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB1.setObjectName("LineDisplayGB1")
        self.LineDisplayGB1.setGeometry(10, 350, 440, 250)

        self.LineDisplayGB2= QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB2.setObjectName("LineDisplayGB2")
        self.LineDisplayGB2.setGeometry(440, 350, 440, 250)

        self.LineDisplayGB3 = QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB3.setObjectName("LineDisplayGB3")
        self.LineDisplayGB3.setGeometry(10, 610, 440, 250)

        self.LineDisplayGB4 = QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB4.setObjectName("LineDisplayGB4")
        self.LineDisplayGB4.setGeometry(440, 610, 440, 250)

        self.startButton = QtWidgets.QPushButton(Dialog2)
        self.startButton.setGeometry(780, 100, 100, 35)
        self.startButton.setStyleSheet('''QPushButton{background:skyblue;border-radius:5px;}''')
        self.startButton.setObjectName("startButton")

        self.stopButton = QtWidgets.QPushButton(Dialog2)
        self.stopButton.setGeometry(780, 140, 100, 35)
        self.stopButton.setStyleSheet('''QPushButton{background:skyblue;border-radius:5px;}''')
        self.stopButton.setObjectName("stopButton")

        self.legend1 = QtWidgets.QPushButton(Dialog2)
        self.legend1.setGeometry(300, 870, 60, 5)
        self.legend1.setStyleSheet('''QPushButton{background:skyblue;border-radius:5px;}''')
        self.legend1.setObjectName("legend1")

        self.lengendlabel1 = QtWidgets.QLabel(Dialog2)
        self.lengendlabel1.setGeometry(365, 870, 60, 20)
        self.lengendlabel1.setObjectName("lengendlabel1")

        self.legend2 = QtWidgets.QPushButton(Dialog2)
        self.legend2.setGeometry(440, 870, 60, 5)
        self.legend2.setStyleSheet('''QPushButton{background:orange;border-radius:5px;}''')
        self.legend2.setObjectName("legend2")

        self.lengendlabel2 = QtWidgets.QLabel(Dialog2)
        self.lengendlabel2.setGeometry(505, 870, 60, 20)
        self.lengendlabel2.setObjectName("lengendlabel2")

        # 上部红绿灯
        self.led1 = MyLed(Dialog2, isVertical=0)
        self.led1.setGeometry(350, 50, 150, 50)
        # 下部红绿灯
        self.led2 = MyLed(Dialog2, isVertical=0)
        self.led2.setGeometry(370, 220, 150, 50)
        # 左部红绿灯
        self.led3 = MyLed(Dialog2, isVertical=1)
        self.led3.setGeometry(330, 90, 50, 150)
        # 右部红绿灯
        self.led4 = MyLed(Dialog2, isVertical=1)
        self.led4.setGeometry(490, 70, 50, 150)

        self.crossroads = QtWidgets.QLabel(Dialog2)
        self.crossroads.setObjectName("crossroads")
        self.crossroads.setGeometry(230, 0, 440, 320)
        self.crossroads.setPixmap(QtGui.QPixmap('/Users/mac/PycharmProjects/TrafficLightSystem/十字路口1.png'))
        self.crossroads.lower()

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog2"))
        self.LineDisplayGB1.setTitle(_translate("Dialog2", "东 -> 西"))
        self.LineDisplayGB2.setTitle(_translate("Dialog2", "西 -> 东"))
        self.LineDisplayGB3.setTitle(_translate("Dialog2", "南 -> 北"))
        self.LineDisplayGB4.setTitle(_translate("Dialog2", "北 -> 南"))
        self.startButton.setText(_translate("Dialog2", "开始检测"))
        self.stopButton.setText(_translate("Dialog2", "停止检测"))
        self.lengendlabel1.setText(_translate("Dialog2", "车流量"))
        self.lengendlabel2.setText(_translate("Dialog2", "绿灯时长"))