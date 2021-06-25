# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataDisplayUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(900, 650)
        # self.centralwidget = QtWidgets.QWidget(Dialog2)
        # self.centralwidget.setGeometry(0, 0, 900, 690)
        # self.centralwidget.setObjectName("centralwidget")

        # self.gridLayout = QtWidgets.QGridLayout(Dialog2)
        # self.gridLayout.setObjectName("gridLayout")
        # self.gridLayout.setSpacing(10)

        self.LineDisplayGB1 = QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB1.setObjectName("LineDisplayGB1")
        self.LineDisplayGB1.setGeometry(10, 10, 420, 250)
        # self.gridLayout.addWidget(self.LineDisplayGB1, 0, 0, 2, 1)

        self.LineDisplayGB2= QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB2.setObjectName("LineDisplayGB2")
        self.LineDisplayGB2.setGeometry(440, 10, 420, 250)
        # self.gridLayout.addWidget(self.LineDisplayGB2, 0, 1, 2, 1)

        self.LineDisplayGB3 = QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB3.setObjectName("LineDisplayGB3")
        self.LineDisplayGB3.setGeometry(10, 270, 420, 250)
        # self.gridLayout.addWidget(self.LineDisplayGB3, 1, 0, 2, 1)

        self.LineDisplayGB4 = QtWidgets.QGroupBox(Dialog2)
        self.LineDisplayGB4.setObjectName("LineDisplayGB4")
        self.LineDisplayGB4.setGeometry(440, 270, 420, 250)
        # self.gridLayout.addWidget(self.LineDisplayGB4, 1, 1, 2, 1)

        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(780, 580, 100, 35)
        self.pushButton.setStyleSheet('''QPushButton{background:skyblue;border-radius:5px;}''')
        self.pushButton.setObjectName("pushButton")
        # self.gridLayout.addWidget(self.pushButton, 2, 0, 2, 1)

        self.legend1 = QtWidgets.QPushButton(Dialog2)
        self.legend1.setGeometry(300, 580, 60, 5)
        self.legend1.setStyleSheet('''QPushButton{background:skyblue;border-radius:5px;}''')
        self.legend1.setObjectName("legend1")

        self.lengendlabel1 = QtWidgets.QLabel(Dialog2)
        self.lengendlabel1.setGeometry(365, 580, 60, 20)
        self.lengendlabel1.setObjectName("lengendlabel1")

        self.legend2 = QtWidgets.QPushButton(Dialog2)
        self.legend2.setGeometry(440, 580, 60, 5)
        self.legend2.setStyleSheet('''QPushButton{background:orange;border-radius:5px;}''')
        self.legend2.setObjectName("legend2")

        self.lengendlabel2 = QtWidgets.QLabel(Dialog2)
        self.lengendlabel2.setGeometry(505, 580, 60, 20)
        self.lengendlabel2.setObjectName("lengendlabel2")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)


    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog2"))
        self.LineDisplayGB1.setTitle(_translate("Dialog2", "东 -> 西"))
        self.LineDisplayGB2.setTitle(_translate("Dialog2", "西 -> 东"))
        self.LineDisplayGB3.setTitle(_translate("Dialog2", "南 -> 北"))
        self.LineDisplayGB4.setTitle(_translate("Dialog2", "北 -> 南"))
        self.pushButton.setText(_translate("Dialog2", "开始检测"))
        self.lengendlabel1.setText(_translate("Dialog2", "车流量"))
        self.lengendlabel2.setText(_translate("Dialog2", "绿灯时长"))