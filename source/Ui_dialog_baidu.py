# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\cc\Desktop\AI_system\lab\lab4\code\UI_design\dialog_baidu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_baidu(object):
    def setupUi(self, Dialog_baidu):
        Dialog_baidu.setObjectName("Dialog_baidu")
        Dialog_baidu.resize(334, 460)

        # 信息标签
        self.label = QtWidgets.QLabel(Dialog_baidu)
        self.label.setGeometry(QtCore.QRect(50, 120, 250, 13))
        self.label.setObjectName("label")
        # 先隐藏
        self.label.setVisible(False)

        self.pushButton = QtWidgets.QPushButton(Dialog_baidu)
        self.pushButton.setGeometry(QtCore.QRect(110, 350, 101, 41))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(Dialog_baidu)
        self.lineEdit.setGeometry(QtCore.QRect(130, 220, 121, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Dialog_baidu)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 63, 13))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_baidu)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 280, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(Dialog_baidu)
        self.label_3.setGeometry(QtCore.QRect(50, 290, 63, 13))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog_baidu)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 63, 13))
        self.label_4.setObjectName("label_4")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog_baidu)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 170, 121, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog_baidu)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 410, 82, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog_baidu)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 63, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog_baidu)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 20, 121, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Dialog_baidu)
        self.label_6.setGeometry(QtCore.QRect(70, 80, 63, 13))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog_baidu)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 80, 121, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Dialog_baidu)
        self.label_7.setGeometry(QtCore.QRect(50, 50, 63, 13))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog_baidu)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 50, 121, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog_baidu)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 410, 82, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.stopButton = QtWidgets.QPushButton(Dialog_baidu)
        self.stopButton.setGeometry(QtCore.QRect(200, 350, 101, 41))
        self.stopButton.setObjectName("stopButton")

        self.retranslateUi(Dialog_baidu)
        QtCore.QMetaObject.connectSlotsByName(Dialog_baidu)

    def retranslateUi(self, Dialog_baidu):
        _translate = QtCore.QCoreApplication.translate
        Dialog_baidu.setWindowTitle(_translate("Dialog_baidu", "推理系统+百度地图"))
        # self.comboBox.setItemText(0, _translate("Dialog_baidu", "东西"))
        # self.comboBox.setItemText(1, _translate("Dialog_baidu", "南北"))
        self.label.setText(_translate("Dialog_baidu", "正在接受百度API数据...(每1分钟更新一次)"))
        self.pushButton.setText(_translate("Dialog_baidu", "推理"))
        self.label_2.setText(_translate("Dialog_baidu", "路况："))
        self.label_3.setText(_translate("Dialog_baidu", "绿灯时长："))
        self.label_4.setText(_translate("Dialog_baidu", "方向："))
        self.pushButton_2.setText(_translate("Dialog_baidu", "数据表"))
        self.label_5.setText(_translate("Dialog_baidu", "东西道路："))
        self.label_6.setText(_translate("Dialog_baidu", "城市："))
        self.label_7.setText(_translate("Dialog_baidu", "南北道路："))
        self.pushButton_3.setText(_translate("Dialog_baidu", "解释器表"))
        self.stopButton.setText(_translate("Dialog_baidu", "结束推理"))
