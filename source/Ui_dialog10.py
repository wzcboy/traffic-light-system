# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\cc\Desktop\AI_system\lab\lab3\mysql文件\dialog10.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog10(object):
    def setupUi(self, Dialog10):
        Dialog10.setObjectName("Dialog10")
        Dialog10.resize(319, 360)
        self.comboBox = QtWidgets.QComboBox(Dialog10)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 61, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label = QtWidgets.QLabel(Dialog10)
        self.label.setGeometry(QtCore.QRect(50, 80, 63, 13))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Dialog10)
        self.pushButton.setGeometry(QtCore.QRect(100, 280, 90, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog10)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 280, 90, 41))
        self.pushButton_2.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(Dialog10)
        self.lineEdit.setGeometry(QtCore.QRect(130, 140, 121, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Dialog10)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 63, 13))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog10)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 200, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(Dialog10)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 63, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog10)
        QtCore.QMetaObject.connectSlotsByName(Dialog10)

    def retranslateUi(self, Dialog10):
        _translate = QtCore.QCoreApplication.translate
        Dialog10.setWindowTitle(_translate("Dialog10", "推理系统"))
        self.comboBox.setItemText(0, _translate("Dialog10", "东西"))
        self.comboBox.setItemText(1, _translate("Dialog10", "南北"))
        self.label.setText(_translate("Dialog10", "车辆方向："))
        self.pushButton.setText(_translate("Dialog10", "推理"))
        self.pushButton_2.setText(_translate("Dialog10", "解释器表"))
        self.label_2.setText(_translate("Dialog10", "车流量："))
        self.label_3.setText(_translate("Dialog10", "绿灯时长："))
