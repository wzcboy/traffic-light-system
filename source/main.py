import numpy as np
import datetime
import time
import sys

from PyQt5 import QtWidgets, QtCore
from Ui_dialog1 import Ui_Dialog1
from Ui_dialog2 import Ui_dialog2
from Ui_dialog3 import Ui_Dialog3
from Ui_dialog4 import Ui_Dialog4
from Ui_dialog5 import Ui_Dialog5
from Ui_dialog6 import Ui_Dialog6
from Ui_dialog7 import Ui_Dialog7
from Ui_dialog8 import Ui_Dialog8
from Ui_dialog9 import Ui_Dialog9
from Ui_dialog10 import Ui_Dialog10
from Ui_dialog11 import Ui_Dialog11
from Ui_dialog12 import Ui_Dialog12
from Ui_dialog13 import Ui_Dialog13
from Ui_dialog14 import Ui_Dialog14
from Ui_dialog_baidu import Ui_Dialog_baidu
from Ui_dialogBaiduData import Ui_Dialog_baiduData
from Ui_mainWin import Ui_MainWindow

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QGridLayout
from connectMySQL import *
from connectBoard import *
import baidu_map

# macos中文显示
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']


def getDateTime():
    """
    获取当前系统时间
    :return: string类型 年-月-日 时:分:秒
    """
    now = datetime.datetime.now()
    now_format = now.strftime("%Y-%m-%d %H:%M:%S")
    return now_format


# 主界面
class parentWin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui=Ui_MainWindow()
        self.main_ui.setupUi(self)


# 系统设置
class childWin1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog1()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.Csetting)
        self.child.pushButton.clicked.connect(self.LightSetting)
    
    def Csetting(self):
        port=self.child.comboBox.currentText()
        data_weigth=str(self.child.lineEdit.text())
        return port,data_weigth

    def LightSetting(self):
        circleTime=str(self.child.lineEdit_2.text())
        yellowTime=str(self.child.lineEdit_3.text())
        greenTime=str(self.child.lineEdit_4.text())
        return circleTime,yellowTime,greenTime


# 数据维护
class childWin3(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog3()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select_sensor)
        self.child.pushButton_2.clicked.connect(self.select_pc)

    def select_new(self):
        # 传感器
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())
        data=querySensorData()
        linemun=data.shape[0]
        if linemun>6:
            linemun=linemun-6
        else :
            linemun=0
        for index,row in data.iterrows():
            if index<linemun:
                continue
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['采集时间'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['东西车流量'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['南北车流量'])))
        
        # 上位机
        rowT=self.child.tableWidget_4.rowCount()
        for i in range(rowT):
            self.child.tableWidget_4.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_4.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_4.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_4.setItem(int(i),3,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_4.setItem(int(i),4,QtWidgets.QTableWidgetItem())
        data=queryPCData()
        linemun=data.shape[0]
        if linemun>6:
            linemun=linemun-6
        else :
            linemun=0
        for index,row in data.iterrows():
            if index<linemun:
                continue
            self.child.tableWidget_4.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget_4.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['传感器ID'])))
            self.child.tableWidget_4.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['下传时间'])))
            self.child.tableWidget_4.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['东西绿灯时长'])))
            self.child.tableWidget_4.setItem(int(index),4,QtWidgets.QTableWidgetItem(str(row['南北绿灯时长'])))

    def select_sensor(self):
        rowT=self.child.tableWidget_2.rowCount()
        for i in range(rowT):
            self.child.tableWidget_2.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_2.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_2.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_2.setItem(int(i),3,QtWidgets.QTableWidgetItem())
        IDf=str(self.child.lineEdit.text())
        IDe=str(self.child.lineEdit_2.text())
        data=querySensorData_twoID(IDf,IDe)
        for index,row in data.iterrows():
            self.child.tableWidget_2.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget_2.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['采集时间'])))
            self.child.tableWidget_2.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['东西车流量'])))
            self.child.tableWidget_2.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['南北车流量'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")

    def select_pc(self):
        rowT=self.child.tableWidget_3.rowCount()
        for i in range(rowT):
            self.child.tableWidget_3.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_3.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_3.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_3.setItem(int(i),3,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_3.setItem(int(i),3,QtWidgets.QTableWidgetItem())
        IDf=str(self.child.lineEdit_3.text())
        IDe=str(self.child.lineEdit_4.text())
        data=queryPCData_twoID(IDf,IDe)
        for index,row in data.iterrows():
            self.child.tableWidget_3.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget_3.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['传感器ID'])))
            self.child.tableWidget_3.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['下传时间'])))
            self.child.tableWidget_3.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['东西绿灯时长'])))
            self.child.tableWidget_3.setItem(int(index),4,QtWidgets.QTableWidgetItem(str(row['南北绿灯时长'])))
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")


# 统计分析
class childWin4(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog4()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.count)

    def count(self):
        select=self.child.comboBox.currentText()
        Datef=self.child.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
        Datee=self.child.dateTimeEdit_2.dateTime().toString("yyyy-MM-dd hh:mm")
        if select=='车流量' :
            data=querySensorData_twoDate(str(Datef),str(Datee))
            sum=0
            for index,row in data.iterrows():
                sum=sum+int(row["东西车流量"])+int(row['南北车流量'])
            self.child.lineEdit.setText(str(sum))
        else:
            data=queryPCData_twoDate(str(Datef),str(Datee))
            sum=0
            for index,row in data.iterrows():
                sum=sum+int(row['东西绿灯时长'])+int(row['南北绿灯时长'])
            self.child.lineEdit.setText(str(sum))


# 知识维护：可信度知识表
class childWin5(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog5()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)
        self.child.pushButton_2.clicked.connect(self.insert)
        self.child.pushButton_3.clicked.connect(self.delete)
        self.child.pushButton_4.clicked.connect(self.update)
        self.child.pushButton_8.clicked.connect(self.gettime)

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),4,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),5,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),6,QtWidgets.QTableWidgetItem())
        ID=str(self.child.lineEdit.text())
        premise=str(self.child.lineEdit_2.text())
        conclusion=str(self.child.lineEdit_3.text())
        time=str(self.child.lineEdit_6.text())
        person=str(self.child.lineEdit_7.text())
        data=queryCK(ID,premise,conclusion,time,person)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['前提'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['结论'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['前提可信度'])))
            self.child.tableWidget.setItem(int(index),4,QtWidgets.QTableWidgetItem(str(row['知识可信度'])))
            self.child.tableWidget.setItem(int(index),5,QtWidgets.QTableWidgetItem(str(row['更新时间'])))
            self.child.tableWidget.setItem(int(index),6,QtWidgets.QTableWidgetItem(str(row['更新人'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")
        self.child.lineEdit_5.setText("")
        self.child.lineEdit_6.setText("")
        self.child.lineEdit_7.setText("")
        # return True

    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def insert(self):
        premise=str(self.child.lineEdit_2.text())
        conclusion=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        lamb=str(self.child.lineEdit_5.text())
        time=str(self.child.lineEdit_6.text())
        person=str(self.child.lineEdit_7.text())
        insertCK(premise,conclusion,cf,lamb,time,person)
        msg="成功新增一条知识！"
        self.showMessageBox(msg)
        self.select()

    def delete(self):
        id=str(self.child.lineEdit.text())
        msg=deleteCK(id)
        self.showMessageBox(msg)
        self.select()

    def update(self):
        id=str(self.child.lineEdit.text())
        premise=str(self.child.lineEdit_2.text())
        conclusion=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        lamb=str(self.child.lineEdit_5.text())
        time=str(self.child.lineEdit_6.text())
        person=str(self.child.lineEdit_7.text())
        msg=updateCK(id,premise,conclusion,cf,lamb,time,person)
        self.showMessageBox(msg)
        self.select()

    def gettime(self):
        datetime_temp=getDateTime()
        self.child.lineEdit_6.setText(str(datetime_temp))


#########################################################
# 知识维护：可信度属性表
class childWin11(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog11()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)
        self.child.pushButton_2.clicked.connect(self.insert)
        self.child.pushButton_3.clicked.connect(self.delete)
        self.child.pushButton_4.clicked.connect(self.update)

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())
        ID=str(self.child.lineEdit.text())
        SID=str(self.child.lineEdit_2.text())
        attribute=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        data=queryCA(ID,SID,attribute)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['传感器数据ID'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['属性'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['CF'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")
        # return True

    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def insert(self):
        ID=str(self.child.lineEdit.text())
        SID=str(self.child.lineEdit_2.text())
        attribute=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        insertCA(ID,SID,attribute,cf)
        msg="成功新增一条可信度属性！"
        self.showMessageBox(msg)
        self.select()

    def delete(self):
        id=str(self.child.lineEdit.text())
        msg=deleteCA(id)
        self.showMessageBox(msg)
        self.select()

    def update(self):
        ID=str(self.child.lineEdit.text())
        SID=str(self.child.lineEdit_2.text())
        attribute=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        msg=updateCA(ID,SID,attribute,cf)
        self.showMessageBox(msg)
        self.select()
    

###############################################################
# 知识维护：可信度综合表
class childWin12(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog12()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)
        self.child.pushButton_2.clicked.connect(self.insert)
        self.child.pushButton_3.clicked.connect(self.delete)
        self.child.pushButton_4.clicked.connect(self.update)

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())
        ID=str(self.child.lineEdit.text())
        SID=str(self.child.lineEdit_2.text())
        conclusion=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        data=queryCS(ID,SID,conclusion)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['传感器数据ID'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['结论'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['综合可信度'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")
        # return True

    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def insert(self):
        ID=str(self.child.lineEdit.text())
        SID=str(self.child.lineEdit_2.text())
        conclusion=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        insertCS(ID,SID,conclusion,cf)
        msg="成功新增一条可信度综合！"
        self.showMessageBox(msg)
        self.select()

    def delete(self):
        id=str(self.child.lineEdit.text())
        msg=deleteCS(id)
        self.showMessageBox(msg)
        self.select()

    def update(self):
        ID=str(self.child.lineEdit.text())
        SID=str(self.child.lineEdit_2.text())
        conclusion=str(self.child.lineEdit_3.text())
        cf=str(self.child.lineEdit_4.text())
        msg=updateCS(ID,SID,conclusion,cf)
        self.showMessageBox(msg)
        self.select()


#########################################################
# 知识维护：可信度前提结论对应表
class childWin13(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog13()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)
        self.child.pushButton_2.clicked.connect(self.insert)
        self.child.pushButton_3.clicked.connect(self.delete)
        self.child.pushButton_4.clicked.connect(self.update)

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())
        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        UpValue=str(self.child.lineEdit_3.text())
        DownValue=str(self.child.lineEdit_4.text())
        data=queryGT(ID,Name)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['名称'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['上限值'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['下限值'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")


    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def insert(self):
        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        UpValue=str(self.child.lineEdit_3.text())
        DownValue=str(self.child.lineEdit_4.text())
        insertGT(ID,Name,UpValue,DownValue)
        msg="成功新增一条可信度属性！"
        self.showMessageBox(msg)
        self.select()

    def delete(self):
        id=str(self.child.lineEdit.text())
        msg=deleteGT(id)
        self.showMessageBox(msg)
        self.select()

    def update(self):
        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        UpValue=str(self.child.lineEdit_3.text())
        DownValue=str(self.child.lineEdit_4.text())
        msg=updateGT(ID,Name,UpValue,DownValue)
        self.showMessageBox(msg)
        self.select()


# 知识维护：模糊知识
class childWin6(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog6()
        self.child.setupUi(self)
        self.child.pushButton_4.clicked.connect(self.select)
        self.child.pushButton_5.clicked.connect(self.insert)
        self.child.pushButton_6.clicked.connect(self.delete)
        self.child.pushButton_7.clicked.connect(self.update)
        self.child.pushButton_8.clicked.connect(self.gettime)

    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),4,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),5,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),6,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),7,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),8,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),9,QtWidgets.QTableWidgetItem())
        ID=str(self.child.lineEdit.text())
        aName=str(self.child.lineEdit_3.text())
        bName=str(self.child.lineEdit_5.text())
        time=str(self.child.lineEdit_9.text())
        person=str(self.child.lineEdit_10.text())
        data=queryFK(ID,aName,bName,time,person)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['A模糊集ID'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['A模糊集名称'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['B模糊集ID'])))
            self.child.tableWidget.setItem(int(index),4,QtWidgets.QTableWidgetItem(str(row['B模糊集名称'])))
            self.child.tableWidget.setItem(int(index),5,QtWidgets.QTableWidgetItem(str(row['CF'])))
            self.child.tableWidget.setItem(int(index),6,QtWidgets.QTableWidgetItem(str(row['λ'])))
            self.child.tableWidget.setItem(int(index),7,QtWidgets.QTableWidgetItem(str(row['模糊矩阵ID'])))
            self.child.tableWidget.setItem(int(index),8,QtWidgets.QTableWidgetItem(str(row['更新时间'])))
            self.child.tableWidget.setItem(int(index),9,QtWidgets.QTableWidgetItem(str(row['更新人'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")
        self.child.lineEdit_5.setText("")
        self.child.lineEdit_6.setText("")
        self.child.lineEdit_7.setText("")
        self.child.lineEdit_8.setText("")
        self.child.lineEdit_9.setText("")
        self.child.lineEdit_10.setText("")

    def insert(self):
        aID=str(self.child.lineEdit_2.text())
        aName=str(self.child.lineEdit_3.text())
        bID=str(self.child.lineEdit_4.text())
        bName=str(self.child.lineEdit_5.text())
        cf=str(self.child.lineEdit_6.text())
        lamb=str(self.child.lineEdit_7.text())
        matrixID=str(self.child.lineEdit_8.text())
        time=str(self.child.lineEdit_9.text())
        person=str(self.child.lineEdit_10.text())
        insertFK(aID,aName,bID,bName,cf,lamb,matrixID,time,person)
        msg="成功新增一条知识！"
        self.showMessageBox(msg)
        self.select()

    def delete(self):
        id=str(self.child.lineEdit.text())
        msg=deleteFK(id)
        self.showMessageBox(msg)
        self.select()

    def update(self):
        id=str(self.child.lineEdit.text())
        aID=str(self.child.lineEdit_2.text())
        aName=str(self.child.lineEdit_3.text())
        bID=str(self.child.lineEdit_4.text())
        bName=str(self.child.lineEdit_5.text())
        cf=str(self.child.lineEdit_6.text())
        lamb=str(self.child.lineEdit_7.text())
        matrixID=str(self.child.lineEdit_8.text())
        time=str(self.child.lineEdit_9.text())
        person=str(self.child.lineEdit_10.text())
        msg=updateFK(id,aID,aName,bID,bName,cf,lamb,matrixID,time,person)
        self.showMessageBox(msg)
        self.select()

    def gettime(self):
        datetime_temp=getDateTime()
        self.child.lineEdit_9.setText(str(datetime_temp))


# 知识维护：模糊论域
class childWin7(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog7()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)
        self.child.pushButton_2.clicked.connect(self.insert)
        self.child.pushButton_3.clicked.connect(self.delete)
        self.child.pushButton_4.clicked.connect(self.update)

    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        data=queryFKDomain(ID,Name)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['名称'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['object'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")


    def insert(self):
        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        object=str(self.child.lineEdit_3.text())
        insertFKDomain(ID,Name,object)
        msg="成功新增一条论域！"
        self.showMessageBox(msg)
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.select()

    def delete(self):
        ID=str(self.child.lineEdit.text())
        deleteFKDomain(ID)
        msg="成功删除一条论域！"
        self.showMessageBox(msg)
        self.child.lineEdit.setText("")
        self.select()

    def update(self):
        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        object=str(self.child.lineEdit_3.text())
        msg=updateFKDomain(ID,Name,object)
        self.showMessageBox(msg)
        self.select()
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")


# 知识维护：模糊集
class childWin8(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog8()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)
        self.child.pushButton_2.clicked.connect(self.insert)
        self.child.pushButton_3.clicked.connect(self.delete)
        self.child.pushButton_4.clicked.connect(self.update)

    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())

        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        DID=str(self.child.lineEdit_4.text())
        data=queryFKSet(ID,Name,DID)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['名称'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['object'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['论域ID'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")


    def insert(self):
        Name=str(self.child.lineEdit_2.text())
        object=str(self.child.lineEdit_3.text())
        DID=str(self.child.lineEdit_4.text())
        insertFKSet(Name,object,DID)
        msg="成功新增一条模糊集！"
        self.showMessageBox(msg)
        self.select()
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")


    def delete(self):
        ID=str(self.child.lineEdit.text())
        deleteFKSet(ID)
        msg="成功删除一条模糊集！"
        self.showMessageBox(msg)
        self.child.lineEdit.setText("")
        self.select()

    def update(self):
        ID=str(self.child.lineEdit.text())
        Name=str(self.child.lineEdit_2.text())
        object=str(self.child.lineEdit_3.text())
        DID=str(self.child.lineEdit_4.text())
        msg=updateFKSet(ID,Name,object,DID)
        self.showMessageBox(msg)
        self.select()


# 知识维护：模糊矩阵
class childWin9(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog9()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)
        self.child.pushButton_2.clicked.connect(self.insert)
        self.child.pushButton_3.clicked.connect(self.delete)
        self.child.pushButton_4.clicked.connect(self.update)

    def showMessageBox(self,msg):
        res = QMessageBox.about(self, "结果",str(msg))
        print("OK!")

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i),3,QtWidgets.QTableWidgetItem())

        ID=str(self.child.lineEdit.text())
        pID=str(self.child.lineEdit_2.text())
        cID=str(self.child.lineEdit_3.text())
        data=queryFKMat(ID,pID,cID)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['前提模糊集ID'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['结论模糊集ID'])))
            self.child.tableWidget.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['object'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")


    def insert(self):
        ID=str(self.child.lineEdit.text())
        pID=str(self.child.lineEdit_2.text())
        cID=str(self.child.lineEdit_3.text())
        object=str(self.child.lineEdit_4.text())
        insertFKMat(ID,pID,cID,object)
        msg="成功新增一条模糊矩阵！"
        self.showMessageBox(msg)
        self.select()
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")
        self.child.lineEdit_3.setText("")
        self.child.lineEdit_4.setText("")


    def delete(self):
        ID=str(self.child.lineEdit.text())
        deleteFKMat(ID)
        msg="成功删除一条模糊矩阵！"
        self.showMessageBox(msg)
        self.child.lineEdit.setText("")
        self.select()

    def update(self):
        ID=str(self.child.lineEdit.text())
        pID=str(self.child.lineEdit_2.text())
        cID=str(self.child.lineEdit_3.text())
        object=str(self.child.lineEdit_4.text())
        msg=updateFKMat(ID,pID,cID,object)
        self.showMessageBox(msg)
        self.select()


# 可信度车流量离散化
# 输入：车流量  输出：车流量小/较小/正常/较大/大
def Cre_inference_to_disperse(car_num):
    car_num = int(car_num)
    dataGT = queryGT("", "")
    for index, row in dataGT.iterrows():
        Name = str(row['名称'])
        UpValue = int(row['上限值'])
        DownValue = int(row['下限值'])
        if UpValue != DownValue:
            if (car_num <= UpValue) & (car_num > DownValue):
                return Name
    return ""


# 综合可信度判断
# 输入：综合可信度  输出：是否采纳 默认>0.6
def Com_Cre(CCnum):
    if CCnum > 0.6:
        flag = 1
    else:
        flag = 0
    return flag


# 可信度绿灯时间控制
# 输入：绿灯时间短/较短/正常/较长/长    输出：绿灯时长
def Cre_inference_to_greentime(str_green):
    dataGT = queryGT("", str_green)
    GTValue = dataGT.at[0, "上限值"]
    return GTValue


# 可信度推理
# 输入传感器数据表的ID
def Cre_Inference_ID(ID):
    # 获取数据表的车流量
    dataS = querySensorData(ID, None)
    car_num = dataS.at[0, "南北车流量"]

    # 车流量转换为离散
    car_res = Cre_inference_to_disperse(car_num)

    # 新增可信度属性
    insertCA("", ID, car_res, 0.9)

    # 获取可信度属性
    dataCA = queryCA("", ID, "")
    a_CA = dataCA.at[0, "属性"]
    cf_CA = dataCA.at[0, "CF"]

    # 获取对应可信度知识
    dataCK = queryCK("", str(a_CA), "", "", "")
    lamba = dataCK.at[0, "知识可信度"]
    cf_CK = dataCK.at[0, "前提可信度"]
    conclusion = dataCK.at[0, "结论"]

    # 判断事实是否可用
    if cf_CA >= lamba:
        cf_CS = cf_CA * cf_CK
        # 可用则加入综合表
        insertCS("", ID, conclusion, cf_CS)

        # 获取可信度综合表
        dataCS = queryCS("", ID, "")
        conclusionCS = dataCS.at[0, "结论"]
        cf_CS_emd = dataCS.at[0, "综合可信度"]

        flag = Com_Cre(cf_CS_emd)
        res = -1
        if flag == 1:
            res = Cre_inference_to_greentime(conclusionCS)
        else:
            print("结论不采用\n")
        return res
    else:
        print("事实不可用\n")


# 可信度推理，仅用于连接百度地图API
# 输入:路况,输出：可信度知识前提，结论
def Cre_Inference_Baidu(str1):
    # 车流量数据可信度
    car_num_CS = 0.9
    # print(str1)
    # 获取对应可信度知识
    dataCK = queryCK("", str1, "", "", "")
    lamba = dataCK.at[0, "知识可信度"]
    cf_CK = dataCK.at[0, "前提可信度"]
    conclusion = dataCK.at[0, "结论"]

    # 判断事实是否可用
    cf_CS = -1
    if car_num_CS >= lamba:
        cf_CS = car_num_CS * cf_CK

        # 判断是否采用结论
        flag = Com_Cre(cf_CS)
        res = -1
        if flag == 1:
            print(conclusion)
            res = Cre_inference_to_greentime(conclusion)
        else:
            print("结论不采用\n")
        print(str1)
        return res, str1, conclusion
    else:
        print("事实不可用\n")
        return -1, str1, conclusion


# 可信度推理，仅用于未连接传感器数据库时
# 输入:车流量
def Cre_Inference_car_num(car_num):
    # 车流量数据可信度
    car_num_CS = 0.9
    # 车流量转换为离散
    car_res = Cre_inference_to_disperse(car_num)

    # 获取对应可信度知识
    dataCK = queryCK("", car_res, "", "", "")
    lamba = dataCK.at[0, "知识可信度"]
    cf_CK = dataCK.at[0, "前提可信度"]
    conclusion = dataCK.at[0, "结论"]

    # 判断事实是否可用
    cf_CS = -1
    if car_num_CS >= lamba:
        cf_CS = car_num_CS * cf_CK

        # 判断是否采用结论
        flag = Com_Cre(cf_CS)
        res = -1
        if flag == 1:
            print(conclusion)
            res = Cre_inference_to_greentime(conclusion)
        else:
            print("结论不采用\n")
        print(car_res)
        return res, car_res, conclusion
    else:
        print("事实不可用\n")
        return 0, car_res, conclusion


# 模糊化，三角法，cin为输入数据，alpha
# 返回产生的模糊集
def fuzzification(cin, alpha):
    # 查询车流量论域
    data = queryFKDomain("", "车流量")
    str1 = data.at[0, "object"]
    cars_domain = str1.split(";")
    sets = ""
    for i in cars_domain:
        if abs(float(i)-float(cin)) <= float(alpha):
            res = 1-(abs(float(i)-float(cin))/float(alpha))
            # 保留三位小数
            res = round(res, 3)
            sets = sets+str(res)+";"
        else:
            sets = sets+"0"+";"
    return sets


# 贴近度计算，C(A,D)
# 输入两个模糊集，模糊集输入为str以；间隔，返回模糊集贴近度
def close_degree_C(sets1, sets2):
    str1 = sets1.split(";")
    str2 = sets2.split(";")
    # 去除 ""
    str1 = [x.strip() for x in str1 if x.strip() != '']
    str2 = [x.strip() for x in str2 if x.strip() != '']
    # inner 内积；outer 外积
    inner = 0
    outer = 10
    for i in range(len(str1)):
        temp1 = min(float(str1[i]), float(str2[i]))
        if temp1 > inner:
            inner = temp1
        temp2 = max(float(str1[i]), float(str2[i]))
        if temp2 < outer:
            outer = temp2
    return (inner+(1-outer))/2


# sets为产生的模糊集，dire为车辆方向 0:东西 1：南北
# 返回最大匹配A模糊集名称、B模糊集名称、模糊矩阵ID
def close_degree(sets, dire):
    close_d = 0
    name_set = ""
    if dire == 0:
        data = queryFKSet()
        for index, row in data.iterrows():
            ID = str(row["ID"])
            name = str(row["名称"])
            objects = str(row["object"])
            if name[0:5] == "东西车流量":
                temp = close_degree_C(sets, objects)
                if close_d < float(temp):
                    close_d = float(temp)
                    name_set = name
        print(name_set)
        if name_set != "":
            data2 = queryFK("", name_set, "", "", "")
            a_Set = data2.at[0, "A模糊集名称"]
            b_Set = data2.at[0, "B模糊集名称"]
            temp2 = data2.at[0, "λ"]
            temp_max_mat_id = data2.at[0, "模糊矩阵ID"]
            if close_d >= temp2:
                return a_Set, b_Set, temp_max_mat_id
    else:
        data = queryFKSet()
        for index, row in data.iterrows():
            ID = str(row["ID"])
            name = str(row["名称"])
            objects = str(row["object"])
            if name[0:5] == "南北车流量":
                temp = close_degree_C(sets, objects)
                if close_d < float(temp):
                    close_d = float(temp)
                    name_set = name
        print(name_set)
        if name_set != "":
            data2 = queryFK("", name_set, "", "", "")
            a_Set = data2.at[0, "A模糊集名称"]
            b_Set = data2.at[0, "B模糊集名称"]
            temp2 = data2.at[0, "λ"]
            temp_max_mat_id = data2.at[0, "模糊矩阵ID"]
            if close_d >= temp2:
                return a_Set, b_Set, temp_max_mat_id


# 寻找一维数组中最大、最小值的index
# 输入：一维数组  输出：index
def find_max_index(list_cin):
    len_list = len(list_cin)
    max_num = -1
    max_num_id = -1
    for i in range(len_list-1,-1,-1):
        if float(list_cin[i]) > float(max_num):
            max_num = list_cin[i]
            max_num_id = i
    min_num=-1
    min_num_id=-1
    for j in range(len_list-1):
        if float(list_cin[j]) > float(min_num):
            min_num = list_cin[j]
            min_num_id = j
    return min_num_id, max_num_id


# 计算B'，采用最大隶属度求得对应绿灯时长
# 输入车流量的产生模糊集，最大匹配的知识的对应矩阵ID
# 返回B对应论域的对应index，两个：最小，最大
def compete_end_id(sets, mat_id):
    # 处理产生模糊集，最后多出一个；，去除空元素
    str1 = sets.split(";")
    str1 = [x.strip() for x in str1 if x.strip() != '']

    # 查找模糊矩阵数据库的对应ID的矩阵
    data = queryFKMat(mat_id, "", "")
    temp = data.at[0, "object"]

    # 切片
    temp2_list = temp.split(";")
    line = len(temp2_list)

    # 构造二维矩阵
    list_two = []
    for i in range(line):
        list_two_temp=temp2_list[i].split(",")
        list_two.append(list_two_temp)

    # 转置
    list_twoT = np.array(list_two)
    list_twoT = list_twoT.T

    # 计算B',str_b为B’对应数组
    line2 = len(list_twoT)
    str_b = ""
    for i in range(line2):
        len_one_line = len(list_twoT[0])
        max_num = -1
        for j in range(len_one_line):
            temp3 = min(float(str1[j]), float(list_twoT[i][j]))
            max_num = max(temp3, max_num)
        str_b = str_b + str(max_num) + " "
    str_b = str_b.split(" ")
    str_b = [x.strip() for x in str_b if x.strip() != '']
    print(str_b)

    # 查找最大隶属度，返回对应B模糊集的index
    res1, res2 = find_max_index(str_b)
    return res1, res2


# 输入车流量、模糊化α、车流方向
# 输出绿灯时长，前提，结论
def compete_light_time(cin, arf, dire):
    sets = fuzzification(cin, arf)
    A_Set, B_Set, mat_id = close_degree(sets, dire)
    B_domain_index_min, B_domain_index_max = compete_end_id(sets, mat_id)

    # 查询B模糊集
    data = queryFKDomain("", "绿灯时长")
    temp = data.at[0, "object"]
    temp = temp.split(";")
    # 根据index获取对应绿灯时长
    res = (int(temp[B_domain_index_min]) + int(temp[B_domain_index_max])) / 2
    return res, A_Set, B_Set


def inference(direction, carNum):
    """
    进行推理
    :param direction: int，方向
    :param carNum: int，车流量
    :return: 绿灯时长（float）和 前提（string）和 结论（string）
    """
    alpha = 10
    if direction == 0:
        try:
            res, premise, conclusion = compete_light_time(carNum, alpha, 0)
            msg = "推理成功"
        except Exception:
            msg = "推理失败"
    else:
        # 南北采用可信度知识
        res, premise, conclusion = Cre_Inference_car_num(carNum)
        msg = "推理成功"
    print(msg)
    return res, premise, conclusion


def emit_start_signal():
    """
    给下位机发出开始信号
    :return: None
    """
    start = "1"
    ser.write(start.encode(encoding='gbk'))


def restart_board():
    ser.close()
    ser.open()


# 推理线程类
class InferenceThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    signal = QtCore.pyqtSignal(list, list, list)
    isStop = 0

    def __init__(self):
        super(InferenceThread, self).__init__()

    def __del__(self):
        self.wait()

    def queryAndEmit(self):
        df = queryResult()
        direct = list(df['方向'])
        carnum = list(df['车流量'])
        lighttime = list(df['绿灯时长'])
        self.signal.emit(direct, carnum, lighttime)

    # 终止线程
    def stopInference(self):
        self.isStop = 1

    def run(self):
        print("这是推理线程")
        # 初始化结果数据表
        initialResult()
        # 给下位机发送开始信号
        emit_start_signal()
        # 初始仿真亮灯
        self.queryAndEmit()
        cnt = 0
        while not self.isStop:
            # 解析下位机传上来的数据,返回下位机数据长度、车辆方向、车辆数
            if ser.in_waiting > 0:
                length, directionFromLow, carNum = analysis_data_form_down()

                lightTime = 0
                if directionFromLow == 0 or directionFromLow == 1:
                    lightTime, premise, conclusion = inference(directionFromLow, carNum)
                    lightTime = round(lightTime)

                # 调试信息
                if directionFromLow == 0:
                    print("\n【info】东西方向车流量为：", carNum, "因此将绿灯时长调整为：", int(lightTime/3), "\n")
                elif directionFromLow == 1:
                    print("\n【info】南北方向车流量为：", carNum, "因此将绿灯时长调整为：", lightTime, "\n")
                else:
                    print("\n【info】黄灯信号\n")

                # 将传感器获得和推理的结果数据存入数据库
                insertResult(directionFromLow, carNum, lightTime)

                # 发送槽信号
                self.queryAndEmit()

                # 传输数据包到下位机
                put_data_to_down(int(lightTime/3), directionFromLow)

            else:
                cnt += 1
                if cnt > 200000:
                    print("waiting data.......")
                    cnt = 0


# 推理功能
class childWin10(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog10()
        self.child.setupUi(self)
        self.child.setupUi(self)
        self.thread = None  # 初始化线程
        self.child.pushButton.clicked.connect(self.random_inference)

    def random_inference(self):
        self.child.lineEdit_2.setText("")
        direct = self.child.comboBox.currentText()
        car_num = str(self.child.lineEdit.text())
        try:
            if direct == "东西":
                lightTime, premise, conclusion = inference(0, car_num)
            elif direct == "南北":
                lightTime, premise, conclusion = inference(1, car_num)

            explain = "因为车流量为: " + str(car_num) + " ->即" + str(premise) + ",得出结论" + str(conclusion) + "->即绿灯时长为: " \
                      + str(lightTime) + " 是已有知识。"

            # 插入传感器数据表
            dataDateTime = getDateTime()
            insertSensorData(dataDateTime, car_num, 0)

            data = querySensorData(None, dataDateTime)
            temp_SensorID = data.at[0, "ID"]

            # 插入解释器数据表
            insertEX(0, temp_SensorID, explain)

            # 前端显示
            self.child.lineEdit_2.setText(str(lightTime))
            msg = "推理成功"
            self.showMessageBox(msg)

        except Exception:
            msg = "推理失败"
            self.showMessageBox(msg)
            self.child.lineEdit_2.setText("")


    def showMessageBox(self, msg):
        res = QMessageBox.about(self, "结果", str(msg))
        print("OK!")


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 40)
        self.ax2 = self.ax.twinx()
        self.ax2.set_ylim(0, 40)


class childWin2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_dialog2()
        self.child.setupUi(self)

        self.x1 = []
        self.x2 = []
        self.direct = []
        self.carnum1 = []
        self.carnum2 = []
        self.lighttime1 = []
        self.lighttime2 = []

        self.init()
        self.child.startButton.clicked.connect(self.start_thread)
        self.child.stopButton.clicked.connect(self.stop_thread)

    def init(self):
        self.LineFigure1 = Figure_Canvas()
        self.LineFigureLayout1 = QGridLayout(self.child.LineDisplayGB1)
        self.LineFigureLayout1.addWidget(self.LineFigure1)

        self.LineFigure2 = Figure_Canvas()
        self.LineFigureLayout2 = QGridLayout(self.child.LineDisplayGB2)
        self.LineFigureLayout2.addWidget(self.LineFigure2)

        self.LineFigure3 = Figure_Canvas()
        self.LineFigureLayout3 = QGridLayout(self.child.LineDisplayGB3)
        self.LineFigureLayout3.addWidget(self.LineFigure3)

        self.LineFigure4 = Figure_Canvas()
        self.LineFigureLayout4 = QGridLayout(self.child.LineDisplayGB4)
        self.LineFigureLayout4.addWidget(self.LineFigure4)

    def start_thread(self):
        # 将推理按钮重新设置为无效
        self.child.startButton.setEnabled(False)
        # 创建线程
        self.inferencethread = InferenceThread()
        self.inferencethread.signal.connect(self.Init_Widgets)  # 线程启动槽函数
        self.inferencethread.start()

    def stop_thread(self):
        self.inferencethread.stopInference()
        # 将推理按钮重新设置为有效
        self.child.startButton.setEnabled(True)
        print("【info】监测车流量终止")

    def Init_Widgets(self, direct_list, carnum_list, lighttime_list):
        self.PrepareSamples(direct_list, carnum_list, lighttime_list)
        self.controlLight()
        self.PrepareLineCanvas1()
        self.PrepareLineCanvas2()
        self.PrepareLineCanvas3()
        self.PrepareLineCanvas4()

    def set_ax(self, figCanvas):
        figCanvas.ax.set_xlim(0, 10)
        figCanvas.ax.set_ylim(0, 40)
        figCanvas.ax.set_xlabel("次数")
        figCanvas.ax.set_ylabel("车流量")

        figCanvas.ax2.set_ylim(0, 40)
        figCanvas.ax2.set_ylabel("绿灯时长")

    def controlLight(self):
        # 东西方向
        if self.displayDirect == 0:
            self.child.led1.gLight1.turn_off()
            self.child.led1.rLight1.turn_on()
            self.child.led1.yLight1.turn_off()

            self.child.led2.gLight1.turn_off()
            self.child.led2.rLight1.turn_on()
            self.child.led2.yLight1.turn_off()

            self.child.led3.gLight1.turn_on()
            self.child.led3.rLight1.turn_off()
            self.child.led3.yLight1.turn_off()

            self.child.led4.gLight1.turn_on()
            self.child.led4.rLight1.turn_off()
            self.child.led4.yLight1.turn_off()
        # 南北方向
        elif self.displayDirect == 1:
            self.child.led1.gLight1.turn_on()
            self.child.led1.rLight1.turn_off()
            self.child.led1.yLight1.turn_off()

            self.child.led2.gLight1.turn_on()
            self.child.led2.rLight1.turn_off()
            self.child.led2.yLight1.turn_off()

            self.child.led3.gLight1.turn_off()
            self.child.led3.rLight1.turn_on()
            self.child.led3.yLight1.turn_off()

            self.child.led4.gLight1.turn_off()
            self.child.led4.rLight1.turn_on()
            self.child.led4.yLight1.turn_off()
        # 东西黄灯显示
        elif self.displayDirect == 2:
            self.child.led1.gLight1.turn_off()
            self.child.led1.rLight1.turn_on()
            self.child.led1.yLight1.turn_off()

            self.child.led2.gLight1.turn_off()
            self.child.led2.rLight1.turn_on()
            self.child.led2.yLight1.turn_off()

            self.child.led3.gLight1.turn_off()
            self.child.led3.rLight1.turn_off()
            self.child.led3.yLight1.turn_on()

            self.child.led4.gLight1.turn_off()
            self.child.led4.rLight1.turn_off()
            self.child.led4.yLight1.turn_on()
            # 南北黄灯显示
        elif self.displayDirect == 3:
            self.child.led1.gLight1.turn_off()
            self.child.led1.rLight1.turn_off()
            self.child.led1.yLight1.turn_on()

            self.child.led2.gLight1.turn_off()
            self.child.led2.rLight1.turn_off()
            self.child.led2.yLight1.turn_on()

            self.child.led3.gLight1.turn_off()
            self.child.led3.rLight1.turn_on()
            self.child.led3.yLight1.turn_off()

            self.child.led4.gLight1.turn_off()
            self.child.led4.rLight1.turn_on()
            self.child.led4.yLight1.turn_off()


    def PrepareSamples(self, direct_list, carnum_list, lighttime_list):
        # 根据方向来选择放入对应的位置
        # 东西方向的数据放入carnum1, lighttime1
        # 南北方向的数据放入carnum2，lighttime2
        carnum1 = []
        carnum2 = []
        lighttime1 = []
        lighttime2 = []
        # 倒数第4个数据用来亮灯
        self.displayLightTime = lighttime_list[-4]
        self.displayDirect = direct_list[-4]

        for i in range(4, len(direct_list)):
            if direct_list[i] == 0:
                carnum1.append(carnum_list[i])
                lighttime1.append(lighttime_list[i])
            elif direct_list[i] == 1:
                carnum2.append(carnum_list[i])
                lighttime2.append(lighttime_list[i])
        # 只取10个数据
        self.carnum1 = carnum1[-10:]
        self.carnum2 = carnum2[-10:]
        lighttime1 = lighttime1[-10:]
        # 按比例缩减，避免仿真时间过长，最低时间为5s
        self.lighttime1 = [int(time/3) if int(time/3) >= 5 else 5 for time in lighttime1]
        self.lighttime2 = lighttime2[-10:]
        # print(self.carnum1)
        # print(self.carnum2)
        self.x1 = np.arange(len(self.carnum1)) + 1
        self.x2 = np.arange(len(self.carnum2)) + 1

    def PrepareLineCanvas1(self):
        line1 = Line2D(self.x1, self.carnum1, color='skyblue')
        line12 = Line2D(self.x1, self.lighttime1, color='orange')
        self.LineFigure1.ax.cla()
        self.LineFigure1.ax2.cla()
        self.set_ax(self.LineFigure1)
        self.LineFigure1.ax.add_line(line1)
        self.LineFigure1.ax2.add_line(line12)
        self.LineFigure1.fig.canvas.draw()
        self.LineFigure1.fig.canvas.flush_events()

    def PrepareLineCanvas2(self):
        line2 = Line2D(self.x1, self.carnum1, color='skyblue')
        line22 = Line2D(self.x1, self.lighttime1, color='orange')
        self.LineFigure2.ax.cla()
        self.LineFigure2.ax2.cla()
        self.set_ax(self.LineFigure2)
        self.LineFigure2.ax.add_line(line2)
        self.LineFigure2.ax2.add_line(line22)
        self.LineFigure2.fig.canvas.draw()
        self.LineFigure2.fig.canvas.flush_events()

    def PrepareLineCanvas3(self):
        line3 = Line2D(self.x2, self.carnum2, color='skyblue')
        line32 = Line2D(self.x2, self.lighttime2, color='orange')
        self.LineFigure3.ax.cla()
        self.LineFigure3.ax2.cla()
        self.set_ax(self.LineFigure3)
        self.LineFigure3.ax.add_line(line3)
        self.LineFigure3.ax2.add_line(line32)
        self.LineFigure3.fig.canvas.draw()
        self.LineFigure3.fig.canvas.flush_events()

    def PrepareLineCanvas4(self):
        line4 = Line2D(self.x2, self.carnum2, color='skyblue')
        line42 = Line2D(self.x2, self.lighttime2, color='orange')
        self.LineFigure4.ax.cla()
        self.LineFigure4.ax2.cla()
        self.set_ax(self.LineFigure4)
        self.LineFigure4.ax.add_line(line4)
        self.LineFigure4.ax2.add_line(line42)
        self.LineFigure4.fig.canvas.draw()
        self.LineFigure4.fig.canvas.flush_events()


# 解释器
class childWin14(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog14()
        self.child.setupUi(self)
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select)

    def select(self):
        rowT=self.child.tableWidget.rowCount()
        for i in range(rowT):
            self.child.tableWidget.setItem(int(i), 0, QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i), 1, QtWidgets.QTableWidgetItem())
            self.child.tableWidget.setItem(int(i), 2, QtWidgets.QTableWidgetItem())
        ID=""
        Sid = str(self.child.lineEdit.text())
        explain = ""
        data = queryEX(ID,Sid,explain)
        for index,row in data.iterrows():
            self.child.tableWidget.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['传感器数据ID'])))
            self.child.tableWidget.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['解释'])))


class BaiduInferenceThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    signal = QtCore.pyqtSignal(str, str, str)
    isStop = 0

    def __init__(self, road1, road2, city):
        super(BaiduInferenceThread, self).__init__()
        self.road1 = road1
        self.road2 = road2
        self.city = city

    def __del__(self):
        self.wait()

    def processAPIData(self, direct, traffic):
        """
        处理从百度API得来的模糊数据
        :param direct: int 方向，0代表东西方向，1代表南北方向
        :param traffic: string 模糊的路况，包括 未知路况 畅通 缓行 拥堵 严重拥堵
        :return: None
        """
        # 获取当前时间
        currentTime = getDateTime()

        # 将获取到的数据插入数据库
        insertBaiduData(currentTime, traffic, "无")

        # 获取当前传感器数据ID
        data = queryBaiduData(None, currentTime)
        tempSensorID = data.at[0, "ID"]

        # 进行推理
        res, premise, conclusion = Cre_Inference_Baidu(traffic)
        explain = "因为路况为: " + str(premise) + ",得出结论" + str(conclusion) + "->即绿灯时长为: " + str(res) + " 是已有知识。"

        # 将解释插入解释数据表
        insertEX(0, tempSensorID, explain)

        # 将结果插入上位机数据表
        currentTime = getDateTime()

        if direct == 0:
            insertPCData(tempSensorID, currentTime, res, 0)
            # 发送槽信号
            self.signal.emit("东西", traffic, str(res))
        elif direct == 1:
            insertPCData(tempSensorID, currentTime, 0, res)
            # 发送槽信号
            self.signal.emit("南北", traffic, str(res))

    # 终止线程
    def stopInference(self):
        self.isStop = 1

    def run(self):
        print("这是百度API推理线程")
        while not self.isStop:
            # 获取两条方向的路况（模糊数据）
            # 百度APi每一分钟更新一次路况
            traffic1, traffic2 = baidu_map.baidumap(self.road1, self.road2, self.city, self.city)

            # 先处理东西方向，即road1
            self.processAPIData(direct=0, traffic=traffic1)

            # 睡眠30s
            time.sleep(30)

            # 再处理南北方向，即road2
            self.processAPIData(direct=1, traffic=traffic2)

            # 再睡眠30s
            time.sleep(30)


class ChildWinbaidu(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog_baidu()
        self.child.setupUi(self)
        self.child.setupUi(self)
        self.baiduThread = None
        # 自动生成车辆数
        self.child.pushButton.clicked.connect(self.inference_form_baidu)
        self.child.stopButton.clicked.connect(self.stopInference)

    def call_backlog(self, direct, traffic, lighttime):
        # 设置方向信息
        self.child.lineEdit_3.setText(str(direct))
        # 设置路况信息
        self.child.lineEdit.setText(str(traffic))
        # 设置绿灯时长信息
        self.child.lineEdit_2.setText(str(lighttime))

    def inference_form_baidu(self):
        # 将推理按钮失效，避免重复点击
        self.child.label.setVisible(True)
        self.child.pushButton.setEnabled(False)
        # 获取输入信息
        road1 = str(self.child.lineEdit_4.text())
        road2 = str(self.child.lineEdit_6.text())
        city = str(self.child.lineEdit_5.text())

        # 创建线程
        self.baiduThread = BaiduInferenceThread(road1, road2, city)
        # 连接信号
        self.baiduThread.signal.connect(self.call_backlog)
        # 开始线程
        self.baiduThread.start()

    def stopInference(self):
        self.baiduThread.stopInference()
        # 将推理按钮重新设置为有效
        self.child.label.setVisible(False)
        self.child.pushButton.setEnabled(True)
        print("【info】百度API终止")

# 百度路况数据维护
class ChildWinBaiduData(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog_baiduData()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.select_BaiduData)

    def select_BaiduData(self):
        rowT=self.child.tableWidget_2.rowCount()
        for i in range(rowT):
            self.child.tableWidget_2.setItem(int(i),0,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_2.setItem(int(i),1,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_2.setItem(int(i),2,QtWidgets.QTableWidgetItem())
            self.child.tableWidget_2.setItem(int(i),3,QtWidgets.QTableWidgetItem())
        IDf = str(self.child.lineEdit.text())
        IDe = str(self.child.lineEdit_2.text())
        data = queryBaiduData_twoID(IDf, IDe)
        for index, row in data.iterrows():
            self.child.tableWidget_2.setItem(int(index),0,QtWidgets.QTableWidgetItem(str(row['ID'])))
            self.child.tableWidget_2.setItem(int(index),1,QtWidgets.QTableWidgetItem(str(row['采集时间'])))
            self.child.tableWidget_2.setItem(int(index),2,QtWidgets.QTableWidgetItem(str(row['东西路况'])))
            self.child.tableWidget_2.setItem(int(index),3,QtWidgets.QTableWidgetItem(str(row['南北路况'])))
        self.child.lineEdit.setText("")
        self.child.lineEdit_2.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWin()
    child1 = childWin1()
    child2 = childWin2()
    child3 = childWin3()
    child4 = childWin4()
    child5 = childWin5()
    child6 = childWin6()
    child7 = childWin7()
    child8 = childWin8()
    child9 = childWin9()
    child10 = childWin10()
    child11 = childWin11()
    child12 = childWin12()
    child13 = childWin13()
    child14 = childWin14()
    child_baidu = ChildWinbaidu()
    child_baiduData = ChildWinBaiduData()

    # 主界面
    btn1 = window.main_ui.pushButton
    btn1.clicked.connect(child1.show)

    btn2 = window.main_ui.pushButton_2
    btn2.clicked.connect(child2.show)

    btn3 = window.main_ui.pushButton_3
    btn3.clicked.connect(child3.show)
    btn3.clicked.connect(child3.select_new)

    btn4 = window.main_ui.pushButton_4
    btn4.clicked.connect(child4.show)

    btn5 = window.main_ui.pushButton_5
    btn5.clicked.connect(child5.show)

    btnbaidu10 = window.main_ui.pushButton_7
    btnbaidu10.clicked.connect(child_baidu.show)

    # 子功能界面
    btn6 = child5.child.pushButton_5
    btn6.clicked.connect(child6.show)
    btn61 = child5.child.pushButton_6
    btn61.clicked.connect(child11.show)
    btn62 = child5.child.pushButton_7
    btn62.clicked.connect(child12.show)
    btn63 = child5.child.pushButton_9
    btn63.clicked.connect(child13.show)
    btn7 = child6.child.pushButton
    btn7.clicked.connect(child7.show)
    btn8 = child6.child.pushButton_2
    btn8.clicked.connect(child8.show)
    btn9 = child6.child.pushButton_3
    btn9.clicked.connect(child9.show)

    # 百度API
    btn10baiduData = child_baidu.child.pushButton_2
    btn10baiduData.clicked.connect(child_baiduData.show)
    btn10baiduEX = child_baidu.child.pushButton_3
    btn10baiduEX.clicked.connect(child14.show)

    # 推理功能
    btn10 = window.main_ui.pushButton_8
    btn10.clicked.connect(child10.show)
    btn10explain = child10.child.pushButton_2
    btn10explain.clicked.connect(child14.show)

    window.show()
    sys.exit(app.exec_())

