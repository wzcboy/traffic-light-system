# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\cc\Desktop\AI_system\lab\lab3\mysql文件\dialog4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog4(object):
    def setupUi(self, Dialog4):
        Dialog4.setObjectName("Dialog4")
        Dialog4.resize(332, 338)
        self.comboBox = QtWidgets.QComboBox(Dialog4)
        self.comboBox.setGeometry(QtCore.QRect(70, 80, 78, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog4)
        self.label.setGeometry(QtCore.QRect(30, 60, 63, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog4)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog4)
        self.label_3.setGeometry(QtCore.QRect(160, 160, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog4)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 63, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog4)
        self.lineEdit.setGeometry(QtCore.QRect(70, 240, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog4)
        self.pushButton.setGeometry(QtCore.QRect(120, 280, 82, 25))
        self.pushButton.setObjectName("pushButton")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog4)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 160, 121, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Dialog4)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(180, 160, 121, 22))
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.retranslateUi(Dialog4)
        QtCore.QMetaObject.connectSlotsByName(Dialog4)

    def retranslateUi(self, Dialog4):
        _translate = QtCore.QCoreApplication.translate
        Dialog4.setWindowTitle(_translate("Dialog4", "统计分析"))
        self.comboBox.setItemText(0, _translate("Dialog4", "车流量"))
        self.comboBox.setItemText(1, _translate("Dialog4", "绿灯时长"))
        self.label.setText(_translate("Dialog4", "统计元素："))
        self.label_2.setText(_translate("Dialog4", "统计范围(时间)："))
        self.label_3.setText(_translate("Dialog4", "--"))
        self.label_4.setText(_translate("Dialog4", "统计结果："))
        self.pushButton.setText(_translate("Dialog4", "开始"))
