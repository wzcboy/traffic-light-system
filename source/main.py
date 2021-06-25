
from PyQt5 import QtWidgets, QtCore
from Ui_dialog1 import Ui_Dialog1
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
from Ui_dialog2 import Ui_dialog2
from Ui_mainWin import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QGridLayout
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import datetime
import numpy as np
import datetime
import time
import serial

# 硬件相关设置
serialPort = "/dev/cu.usbmodem14201"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)  # 连接串口
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
con = create_engine('mysql+pymysql://root:wzc2000sxmx.@localhost:3306/intelligent_system')
# con = create_engine('mysql+pymysql://root:123456@localhost:3306/ailab2')


def insertMatrix(aID, bID, matrix):
    """
    插入模糊矩阵到mysql
    :param aID: 模糊集A的ID，整数
    :param bID: 模糊集B的ID，整数
    :param matrix: 模糊矩阵，浮点数矩阵
    :return: none
    """
    strMatrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = round(matrix[i][j], 2)
            strMatrix += str(matrix[i][j])
            if j != len(matrix[0])-1:
                strMatrix += ";"
        if i != len(matrix)-1:
            strMatrix += "\\"
    print(strMatrix)
    # mysql语句
    sql_insert = "insert into 模糊矩阵表 values(null, " + str(aID) + "," + str(bID) + ",\'" + strMatrix + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条模糊矩阵的数据")


def queryCK(ID="", premise="", conclusion="", time="", person=""):
    """
    可信度知识库的查询函数
    :param ID: 整数
    :param premise: 前提
    :param conclusion: 结论
    :param time: 更新时间
    :param person: 更新人
    :return: none
    """
    flags = [1, 1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if premise=="":
        flags[1] = 0
    if conclusion=="":
        flags[2] = 0
    if time=="":
        flags[3] = 0
    if person=="":
        flags[4] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '00000':
        sql_query = 'select * from 可信度知识表;'
    elif strFlag == '00001':
        sql_query = 'select * from 可信度知识表 where 更新人=\'' + person + '\';'
    elif strFlag == '00010':
        sql_query = 'select * from 可信度知识表 where 更新时间=\'' + time + '\';'
    elif strFlag == '00011':
        sql_query = 'select * from 可信度知识表 where 更新人=\'' + person + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '00100':
        sql_query = 'select * from 可信度知识表 where 结论=\'' + conclusion + '\';'
    elif strFlag == '00101':
        sql_query = 'select * from 可信度知识表 where 结论=\'' + conclusion + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '00110':
        sql_query = 'select * from 可信度知识表 where 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '00111':
        sql_query = 'select * from 可信度知识表 where 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01000':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\';'
    elif strFlag == '01001':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01010':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '01011':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01100':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\';'
    elif strFlag == '01101':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01110':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '01111':
        sql_query = 'select * from 可信度知识表 where 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '10000':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ';'
    elif strFlag == '10001':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and  更新人=\'' + person + '\';'
    elif strFlag == '10010':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 更新时间=\'' + time + '\';'
    elif strFlag == '10011':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '10100':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=\'' + conclusion + '\';'
    elif strFlag == '10101':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=\'' + conclusion + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '10110':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '10111':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '11000':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\';'
    elif strFlag == '11001':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\' and  更新人=\'' + person + '\';'
    elif strFlag == '11010':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '11011':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '11100':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\';'
    elif strFlag == '11101':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '11110':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '11111':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=\'' + premise + '\' and 结论=\'' + conclusion + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'

    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # df_read_str=str(df_read)
    # print(df_read)
    return df_read


def insertCK(premise, conclusion, cf, lamb, time, person):
    # mysql语句
    sql_insert = "insert into 可信度知识表 values(null, \'" + premise + "\',\'" + conclusion + "\'," + str(cf) \
                 + "," + str(lamb) + ",\'" + time + "\',\'" + person + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条可信度知识")


def queryFK(ID="", AName="", BName="", time="", person=""):
    """
    模糊知识库的查询函数
    :param ID: 整数
    :param AName: 模糊集A的名称
    :param BName: 模糊集的名称
    :param time: 更新时间
    :param person: 更新人
    :return: none
    """
    flags = [1, 1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if AName=="":
        flags[1] = 0
    if BName=="":
        flags[2] = 0
    if time=="":
        flags[3] = 0
    if person=="":
        flags[4] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '00000':
        sql_query = 'select * from 模糊知识表;'
    elif strFlag == '00001':
        sql_query = 'select * from 模糊知识表 where 更新人=\'' + person + '\';'
    elif strFlag == '00010':
        sql_query = 'select * from 模糊知识表 where 更新时间=\'' + time + '\';'
    elif strFlag == '00011':
        sql_query = 'select * from 模糊知识表 where 更新人=\'' + person + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '00100':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=\'' + BName + '\';'
    elif strFlag == '00101':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=\'' + BName + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '00110':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '00111':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01000':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\';'
    elif strFlag == '01001':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01010':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '01011':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01100':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\';'
    elif strFlag == '01101':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '01110':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '01111':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '10000':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ';'
    elif strFlag == '10001':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and  更新人=\'' + person + '\';'
    elif strFlag == '10010':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and 更新时间=\'' + time + '\';'
    elif strFlag == '10011':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '10100':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=\'' + BName + '\';'
    elif strFlag == '10101':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=\'' + BName + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '10110':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '10111':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '11000':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\';'
    elif strFlag == '11001':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\' and  更新人=\'' + person + '\';'
    elif strFlag == '11010':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '11011':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '11100':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\';'
    elif strFlag == '11101':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\' and 更新人=\'' + person + '\';'
    elif strFlag == '11110':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\';'
    elif strFlag == '11111':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=\'' + AName + '\' and B模糊集名称=\'' + BName + '\' and 更新时间=\'' + time + '\' and 更新人=\'' + person + '\';'

    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def insertFK(aID, aName, bID, bName, cf, lamb, matrixID, time, person):
    # mysql语句
    sql_insert = "insert into 模糊知识表 values(null, " + str(aID) + ",\'" + aName + "\'," + str(bID) \
                 + ",\'" + bName + "\'," + str(cf) + "," + str(lamb) + "," + str(matrixID) + ",\'" + time + "\',\'" + person + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条模糊知识")


def insertDomain(Name, matrix):
    """
    插入论域到mysql
    :param Name: 论域名称，字符串
    :param matrix: 论域，浮点数矩阵
    :return: none
    """
    strMatrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = round(matrix[i][j], 2)
            strMatrix += str(matrix[i][j])
            if j != len(matrix[0])-1:
                strMatrix += ";"
        if i != len(matrix)-1:
            strMatrix += "\\"
    # print(strMatrix)
    # mysql语句
    sql_insert = "insert into 论域表 values(null, " + Name + "," + ",\'" + strMatrix + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条论域")


def insertFKSet(Name, matrix, did):
    """
    插入模糊集到mysql
    :param Name: 模糊集名称，字符串
    :param matrix: 模糊集，浮点数矩阵
    :param did: 论域id，整数
    :return: none
    """
    # strMatrix = ""
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         matrix[i][j] = round(matrix[i][j], 2)
    #         strMatrix += str(matrix[i][j])
    #         if j != len(matrix[0])-1:
    #             strMatrix += ";"
    #     if i != len(matrix)-1:
    #         strMatrix += "\\"
    # print(strMatrix)
    # mysql语句
    sql_insert = "insert into 模糊集表 values(null, \'" + Name + "\',\'" + matrix + "\',"+str(did) + ");"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条模糊集的数据")


def querySensorData(ID=None, collectTime=None):
    """
    查询传感器采集到的数据
    :param ID: 整数ID
    :param collectTime: 字符串类型的采集时间(2021-5-22 23:18:21)
    :return:
    """
    if ID==None and collectTime==None:
        sql_query = 'select * from 传感器数据表;'
    elif ID==None and collectTime!=None:
        sql_query = 'select * from 传感器数据表 where 采集时间=\'' + collectTime + '\';'
    elif ID!=None and collectTime==None:
        sql_query = 'select * from 传感器数据表 where ID=' + str(ID) + ';'
    else:
        sql_query = 'select * from 传感器数据表 where ID=' + str(ID) + ' and 采集时间=\'' + collectTime + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def querySensorData_twoID(IDf="",IDe=""):
    """
    通过ID范围查询传感器采集到的数据
    :param IDf: 整数ID
    :param IDe: 整数ID
    :return:
    """
    if IDf=="" and IDe=="":
        sql_query = 'select * from 传感器数据表;'
    elif IDf=="" and IDe!="":
        sql_query = 'select * from 传感器数据表 where ID<=' + IDe + ';'
    elif IDf!="" and IDe=="":
        sql_query = 'select * from 传感器数据表 where ID>=' + IDf + ';'
    else:
        sql_query = 'select * from 传感器数据表 where ID>=' + IDf + ' and ID<=' + IDe + ';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def querySensorData_twoDate(Datef="",Datee=""):
    """
    通过时间范围查询传感器采集到的数据
    :param Datef: date
    :param Datee: date
    :return:
    """
    if Datef=="" and Datee=="":
        sql_query = 'select * from 传感器数据表;'
    elif Datef=="" and Datee!="":
        sql_query = 'select * from 传感器数据表 where 采集时间<=\'' + Datee + '\';'
    elif Datef!="" and Datee=="":
        sql_query = 'select * from 传感器数据表 where 采集时间>=\'' + Datef + '\';'
    else:
        sql_query = 'select * from 传感器数据表 where 采集时间>=\'' + Datef + '\' and 采集时间<=\'' + Datee + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def insertSensorData(collectTime, carFlow1=0, carFlow2=0):
    """
    插入传感器采集到的数据
    :param collectTime: string 采集时间(2021-5-22 23:18:21)
    :param carFlow1: int 东西方向的车流量，默认为0
    :param carFlow2: int 南北方向的车流量，默认为0
    :return: none
    """
    # mysql语句
    sql_insert = "insert into 传感器数据表 values(null, \'" + collectTime + "\'," + str(carFlow1) + "," + str(carFlow2) + ");"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条传感器采集的数据")


def queryPCData(ID=None, outTime=None):
    """
    查询上位机输出的数据
    :param ID: 整数ID
    :param outTime: 字符串类型的输出时间(2021-5-22 23:18:21)
    :return:
    """
    if ID==None and outTime==None:
        sql_query = 'select * from 上位机数据表;'
    elif ID==None and outTime!=None:
        sql_query = 'select * from 上位机数据表 where 下传时间=\'' + outTime + '\';'
    elif ID!=None and outTime==None:
        sql_query = 'select * from 上位机数据表 where ID=' + str(ID) + ';'
    else:
        sql_query = 'select * from 上位机数据表 where ID=' + str(ID) + ' and 下传时间=\'' + outTime + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def queryPCData_twoID(IDf="",IDe=""):
    """
    通过ID范围查询上位机输出的数据
    :param IDf: 整数ID
    :param IDe: 整数ID
    :return:
    """
    if IDf=="" and IDe=="":
        sql_query = 'select * from 上位机数据表;'
    elif IDf=="" and IDe!="":
        sql_query = 'select * from 上位机数据表 where ID<=' + IDe + ';'
    elif IDf!="" and IDe=="":
        sql_query = 'select * from 上位机数据表 where ID>=' + IDf + ';'
    else:
        sql_query = 'select * from 上位机数据表 where ID>=' + IDf + ' and ID<=' + IDe + ';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def queryPCData_twoDate(Datef="",Datee=""):
    """
    通过时间范围查询上位机输出的数据
    :param Datef: date
    :param Datee: date
    :return:
    """
    if Datef=="" and Datee=="":
        sql_query = 'select * from 上位机数据表;'
    elif Datef=="" and Datee!="":
        sql_query = 'select * from 上位机数据表 where 下传时间<=\'' + Datee + '\';'
    elif Datef!="" and Datee=="":
        sql_query = 'select * from 上位机数据表 where 下传时间>=\'' + Datef + '\';'
    else:
        sql_query = 'select * from 上位机数据表 where 下传时间>=\'' + Datef + '\' and 下传时间<=\'' + Datee + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def insertPCData(outTime, lightTime1=0, lightTime2=0):
    """
    插入上位机输出的数据
    :param outTime: 输出时间(2021-5-22 23:18:21)
    :param lightTime1: 东西方向的绿灯时长，默认为0
    :param lightTime2: 南北方向的绿灯时长，默认为0
    :return: none
    """
    # mysql语句
    sql_insert = "insert into 上位机数据表 values(null,\'" + outTime + "\'," + str(lightTime1) + "," + str(lightTime2) + ");"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条上位机输出的数据")


# 删除可信度知识
def deleteCK(id):
    """
    删除可信度知识库知识
    :param id：知识id号
    :return: string
    """
    # mysql语句
    sql_delete = "delete from 可信度知识表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条可信度知识 ID="+str(id)
    return msg


# 修改可信度知识
def updateCK(id, premise, conclusion, cf, lamb, time, person):
    flags = [1, 1, 1, 1, 1, 1, 1]
    if id=="":
        flags[0] = 0
    if premise=="":
        flags[1] = 0
    if conclusion=="":
        flags[2] = 0
    if cf=="":
        flags[3] = 0
    if lamb=="":
        flags[4] = 0
    if time=="":
        flags[5] = 0
    if person=="":
        flags[6] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(id)
    if flags[0]==1&flags[6]==1:
        sql_update='update 可信度知识表 set 更新人=\'' +person+ '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[5]==1:
        sql_update='update 可信度知识表 set 更新时间=\'' + str(time) + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[4]==1:
        sql_update='update 可信度知识表 set 知识可信度=' + str(lamb) + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[3]==1:
        sql_update='update 可信度知识表 set 前提可信度=' + str(cf) + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[2]==1:
        sql_update='update 可信度知识表 set 结论=\'' + conclusion + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 可信度知识表 set 前提=\'' + premise + '\' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条可信度知识")
    return msg


# 删除模糊知识
def deleteFK(id):
    """
    删除模糊知识库知识
    :param id：知识id号
    :return: string
    """
    # mysql语句
    sql_delete = "delete from 模糊知识表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条模糊知识 ID="+str(id)
    return msg


# 修改模糊知识
def updateFK(id,aID, aName, bID, bName, cf, lamb, matrixID, time, person):
    flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    if id=="":
        flags[0] = 0
    if aID=="":
        flags[1] = 0
    if aName=="":
        flags[2] = 0
    if bID=="":
        flags[3] = 0
    if bName=="":
        flags[4] = 0
    if cf=="":
        flags[5] = 0
    if lamb=="":
        flags[6] = 0
    if matrixID=="":
        flags[7] = 0
    if time=="":
        flags[8] = 0
    if person=="":
        flags[9] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(id)
    if flags[0]==1&flags[9]==1:
        sql_update='update 模糊知识表 set 更新人=\'' +person+ '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[8]==1:
        sql_update='update 模糊知识表 set 更新时间=\'' + str(time) + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[7]==1:
        sql_update='update 模糊知识表 set 模糊矩阵ID=' + str(matrixID) + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[6]==1:
        sql_update='update 模糊知识表 set λ=' + str(lamb) + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[5]==1:
        sql_update='update 模糊知识表 set CF=' + cf + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[4]==1:
        sql_update='update 模糊知识表 set B模糊集名称=\'' + bName + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[3]==1:
        sql_update='update 模糊知识表 set B模糊集ID=' + bID + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[2]==1:
        sql_update='update 模糊知识表 set A模糊集名称=\'' + aName + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 模糊知识表 set A模糊集ID=' + aID + ' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条模糊知识")
    return msg


# 查询模糊知识论域表
def queryFKDomain(ID="", Name=""):
    """
    模糊知识库的查询函数
    :param ID: 整数
    :param Name: 名称
    :return: DataFrame
    """
    flags = [1, 1]
    if ID == "":
        flags[0] = 0
    if Name == "":
        flags[1] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '00':
        sql_query = 'select * from 论域表;'
    elif strFlag == '01':
        sql_query = 'select * from 论域表 where 名称=\'' + Name + '\';'
    elif strFlag == '10':
        sql_query = 'select * from 论域表 where ID=' + ID + ';'
    elif strFlag == '11':
        sql_query = 'select * from 论域表 where ID=' + ID + ' and 名称=\'' + Name + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


# 新增模糊知识论域
def insertFKDomain(ID, Name, object):
    """
    插入模糊知识论域
    :param ID: 整数
    :param Name: string
    :param object: string
    :return: msg string
    """
    # mysql语句
    sql_insert = "insert into 论域表 values(" + str(ID) + ",\'" + str(Name) + "\',\'" + str(object) + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条模糊知识论域")


# 删除模糊知识论域
def deleteFKDomain(ID):
    """
    删除模糊知识论域
    :param ID: 整数
    """
    # mysql语句
    sql_delete = "delete from 论域表 where ID=" + ID + ";"
    # 执行语句
    con.execute(sql_delete)
    print("成功新增一条模糊知识论域")


# 修改论域
def updateFKDomain(ID, Name, object):
    flags = [1, 1, 1]
    if ID=="":
        flags[0] = 0
    if Name=="":
        flags[1] = 0
    if object=="":
        flags[2] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(ID)
    if flags[0]==1&flags[2]==1:
        sql_update='update 论域表 set object=\'' + object + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 论域表 set 名称=\'' + Name + '\' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条论域")
    return msg


# 查询模糊集表
def queryFKSet(ID="", Name="", DID=""):
    """
    模糊集的查询函数
    :param ID: 整数
    :param Name: 名称
    :param DID: 论域id
    :return: DataFrame
    """
    flags = [1, 1, 1]
    if ID == "":
        flags[0] = 0
    if Name == "":
        flags[1] = 0
    if DID == "":
        flags[2] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '000':
        sql_query = 'select * from 模糊集表;'
    elif strFlag == '001':
        sql_query = 'select * from 模糊集表 where 论域ID=' + DID + ';'
    elif strFlag == '010':
        sql_query = 'select * from 模糊集表 where 名称=\'' + Name + '\';'
    elif strFlag == '100':
        sql_query = 'select * from 模糊集表 where ID=' + ID + ';'
    elif strFlag == '011':
        sql_query = 'select * from 模糊集表 where 论域ID=' + DID + ' and 名称=\'' + Name + '\';'
    elif strFlag == '101':
        sql_query = 'select * from 模糊集表 where 论域ID=' + DID + ' and ID=' + ID + ';'
    elif strFlag == '110':
        sql_query = 'select * from 模糊集表 where ID=' + ID + ' and 名称=\'' + Name + '\';'
    elif strFlag == '111':
        sql_query = 'select * from 模糊集表 where ID=' + ID + ' and 名称=\'' + Name + '\' and 论域ID=' + DID + ';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


# 删除模糊集
def deleteFKSet(id):
    """
    删除模糊集
    :param id：id
    :return: string
    """
    # mysql语句
    sql_delete = "delete from 模糊集表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条模糊集 ID="+str(id)
    return msg


# 修改模糊集
def updateFKSet(ID, Name, object, DID):
    flags = [1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if Name=="":
        flags[1] = 0
    if object=="":
        flags[2] = 0
    if DID=="":
        flags[3] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(ID)
    if flags[0]==1&flags[3]==1:
        sql_update='update 模糊集表 set 论域ID=' + DID + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[2]==1:
        sql_update='update 模糊集表 set object=\'' + object + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 模糊集表 set 名称=\'' + Name + '\' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条模糊集")
    return msg


# 查询模糊矩阵表
def queryFKMat(ID="", pID="",cID=""):
    """
    模糊矩阵的查询函数
    :param ID: 整数
    :param pID: 整数
    :param cID: 整数
    :return: string
    """
    flags = [1, 1, 1]
    if ID=="":
        flags[0] = 0
    if pID=="":
        flags[1] = 0
    if cID=="":
        flags[2] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '000':
        sql_query = 'select * from 模糊矩阵表;'
    elif strFlag == '001':
        sql_query = 'select * from 模糊矩阵表 where 结论模糊集ID=' + cID + ';'
    elif strFlag == '010':
        sql_query = 'select * from 模糊矩阵表 where 前提模糊集ID=' + pID + ';'
    elif strFlag == '100':
        sql_query = 'select * from 模糊矩阵表 where ID=' + ID + ';'
    elif strFlag == '011':
        sql_query = 'select * from 模糊矩阵表 where 结论模糊集ID=' + cID + ' and 前提模糊集ID=' + pID + ';'
    elif strFlag == '101':
        sql_query = 'select * from 模糊矩阵表 where 结论模糊集ID=' + cID + ' and ID=' + ID + ';'
    elif strFlag == '110':
        sql_query = 'select * from 模糊矩阵表 where ID=' + ID + ' and 前提模糊集ID=' + pID + ';'
    elif strFlag == '111':
        sql_query = 'select * from 模糊矩阵表 where ID=' + ID + ' and 前提模糊集ID=' + pID + ' and 结论模糊集ID=' + cID + ';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


# 新增模糊矩阵
def insertFKMat(ID, pID, cID, object):
    """
    插入模糊矩阵
    :param ID: 整数
    :param pID: 整数
    :param cID: 整数
    :param object: string
    :return: msg string
    """
    # mysql语句
    sql_insert = "insert into 模糊矩阵表 values(" + str(ID) + "," + pID + "," + cID + ",\'" + str(object) + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条模糊知识论域")


# 删除模糊矩阵
def deleteFKMat(id):
    """
    删除模糊矩阵知识
    :param id：id
    :return: string
    """
    # mysql语句
    sql_delete = "delete from 模糊矩阵表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条模糊矩阵 ID="+str(id)
    return msg


# 修改模糊集
def updateFKMat(ID, pID, cID, object):
    flags = [1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if pID=="":
        flags[1] = 0
    if cID=="":
        flags[2] = 0
    if object=="":
        flags[3] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(ID)
    if flags[0]==1&flags[3]==1:
        sql_update='update 模糊矩阵表 set object=\'' + object + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[2]==1:
        sql_update='update 模糊矩阵表 set 结论模糊集ID=' + cID + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 模糊矩阵表 set 前提模糊集ID=' + pID + ' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条模糊矩阵")
    return msg


# 查询可信度属性表
def queryCA(ID="", SID="", attibute=""):
    flags = [1, 1, 1]
    if ID=="":
        flags[0] = 0
    if SID=="":
        flags[1] = 0
    if attibute=="":
        flags[2] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '000':
        sql_query = 'select * from 可信度属性表;'
    elif strFlag == '001':
        sql_query = 'select * from 可信度属性表 where 属性=\'' + attibute + '\';'
    elif strFlag == '010':
        sql_query = 'select * from 可信度属性表 where 传感器数据ID=' + SID + ';'
    elif strFlag == '100':
        sql_query = 'select * from 可信度属性表 where ID=' + ID + ';'
    elif strFlag == '011':
        sql_query = 'select * from 可信度属性表 where 属性=\'' + attibute + '\' and 传感器数据ID=' + SID + ';'
    elif strFlag == '101':
        sql_query = 'select * from 可信度属性表 where 属性=\'' + attibute + '\' and ID=' + ID + ';'
    elif strFlag == '110':
        sql_query = 'select * from 可信度属性表 where ID=' + ID + ' and 传感器数据ID=' + SID + ';'
    elif strFlag == '111':
        sql_query = 'select * from 可信度属性表 where ID=' + ID + ' and 传感器数据ID=' + SID + ' and 属性=\'' + attibute + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


# 新增可信度属性
def insertCA(ID, SID, atrribute, cf):
    # mysql语句
    sql_insert = "insert into 可信度属性表 values(null" + "," + str(SID) + ",\'" + atrribute + "\'," + str(cf) + ");"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条可信度属性")


# 删除可信度属性
def deleteCA(id):
    # mysql语句
    sql_delete = "delete from 可信度属性表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条可信度属性 ID="+str(id)
    return msg


# 修改可信度属性
def updateCA(ID, SID, atrribute, cf):
    flags = [1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if SID=="":
        flags[1] = 0
    if atrribute=="":
        flags[2] = 0
    if cf=="":
        flags[3] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(ID)
    if flags[0]==1&flags[3]==1:
        sql_update='update 可信度属性表 set CF=' + cf + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[2]==1:
        sql_update='update 可信度属性表 set 属性=\'' + atrribute + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 可信度属性表 set 传感器数据ID=' + SID + ' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条可信度属性")
    return msg


########################################################
# 查询可信度综合表
def queryCS(ID="", SID="",conclusion=""):
    flags = [1, 1, 1]
    if ID=="":
        flags[0] = 0
    if SID=="":
        flags[1] = 0
    if conclusion=="":
        flags[2] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '000':
        sql_query = 'select * from 可信度综合表;'
    elif strFlag == '001':
        sql_query = 'select * from 可信度综合表 where 结论=\'' + conclusion + '\';'
    elif strFlag == '010':
        sql_query = 'select * from 可信度综合表 where 传感器数据ID=' + SID + ';'
    elif strFlag == '100':
        sql_query = 'select * from 可信度综合表 where ID=' + ID + ';'
    elif strFlag == '011':
        sql_query = 'select * from 可信度综合表 where 结论=\'' + conclusion + '\' and 传感器数据ID=' + SID + ';'
    elif strFlag == '101':
        sql_query = 'select * from 可信度综合表 where 结论=\'' + conclusion + '\' and ID=' + ID + ';'
    elif strFlag == '110':
        sql_query = 'select * from 可信度综合表 where ID=' + ID + ' and 传感器数据ID=' + SID + ';'
    elif strFlag == '111':
        sql_query = 'select * from 可信度综合表 where ID=' + ID + ' and 传感器数据ID=' + SID + ' and 结论=\'' + conclusion + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


# 新增可信度综合表
def insertCS(ID, SID, conclusion, cf):
    # mysql语句
    sql_insert = "insert into 可信度综合表 values(null" + "," + str(SID) + ",\'" + conclusion + "\'," + str(cf) + ");"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条可信度综合")


# 删除可信度综合表
def deleteCS(id):
    # mysql语句
    sql_delete = "delete from 可信度综合表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条可信度综合 ID="+str(id)
    return msg


# 修改可信度综合表
def updateCS(ID, SID, conclusion, cf):
    flags = [1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if SID=="":
        flags[1] = 0
    if conclusion=="":
        flags[2] = 0
    if cf=="":
        flags[3] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(ID)
    if flags[0]==1&flags[3]==1:
        sql_update='update 可信度综合表 set 综合可信度=' + cf + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[2]==1:
        sql_update='update 可信度综合表 set 结论=\'' + conclusion + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 可信度综合表 set 传感器数据ID=' + SID + ' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条可信度综合")
    return msg


########################################################
# 查询可信度前提结论对应表
def queryGT(ID="", Name=""):
    flags = [1, 1]
    if ID=="":
        flags[0] = 0
    if Name=="":
        flags[1] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '00':
        sql_query = 'select * from 可信度前提结论对应表;'
    elif strFlag == '01':
        sql_query = 'select * from 可信度前提结论对应表 where 名称=\'' + Name + '\';'
    elif strFlag == '10':
        sql_query = 'select * from 可信度前提结论对应表 where ID=' + ID + ';'
    elif strFlag == '11':
        sql_query = 'select * from 可信度前提结论对应表 where ID=' + ID + ' and 名称=\'' + Name +'\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


# 新增可信度前提结论对应表
def insertGT(ID, Name, UpValue,DownValue):
    # mysql语句
    sql_insert = "insert into 可信度前提结论对应表 values(null" + ",\'" + str(Name) + "\'," + UpValue + "," + DownValue +");"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条可信度前提结论对应信息")


# 删除可信度前提结论对应表
def deleteGT(id):
    # mysql语句
    sql_delete = "delete from 可信度前提结论对应表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条可信度前提结论对应信息 ID="+str(id)
    return msg


# 修改可信度前提结论对应表
def updateGT(ID, Name, UpValue,DownValue):
    flags = [1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if Name=="":
        flags[1] = 0
    if UpValue=="":
        flags[2] = 0
    if DownValue=="":
        flags[3] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(ID)
    if flags[0]==1&flags[3]==1:
        sql_update='update 可信度前提结论对应表 set 下限值=' + DownValue + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[2]==1:
        sql_update='update 可信度前提结论对应表 set 上限值=' + UpValue + ' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 可信度前提结论对应表 set 名称=\'' + Name + '\' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条可信度前提结论对应信息")
    return msg


def queryResult():
    sql_query = 'select * from 结果数据表;'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


def insertResult(direct, carNum, lightTime):
    """
    插入结果数据表
    :param direct: int 方向
    :param carNum: int 车流量
    :param lightTime: int 绿灯时长
    :return: None
    """
    # mysql语句
    sql_insert = "insert into 结果数据表 values(null" + "," + str(direct) + "," + str(carNum) + "," + str(lightTime) + ");"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条结果数据")


def clearResult():
    """
    清空结果数据表
    :return: None
    """
    # mysql语句
    sql_delete = "delete from 结果数据表;"
    # 执行语句
    con.execute(sql_delete)
    print("已清空结果数据")


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
        return res
    else:
        print("事实不可用\n")


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
    str1=sets1.split(";")
    str2=sets2.split(";")
    # 去除 ""
    str1 = [x.strip() for x in str1 if x.strip()!='']
    str2 = [x.strip() for x in str2 if x.strip()!='']
    # inner 内积；outer 外积
    inner=0
    outer=10
    for i in range(len(str1)):
        temp1=min(float(str1[i]),float(str2[i]))
        if temp1 > inner:
            inner=temp1
        temp2=max(float(str1[i]),float(str2[i]))
        if temp2<outer:
            outer = temp2
    return (inner+(1-outer))/2


# sets为产生的模糊集，dire为车辆方向 0:东西 1：南北
# 返回最大匹配的模糊矩阵ID
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
        # print(name_set)
        if name_set != "":
            data2 = queryFK("", name_set, "", "", "")
            temp2 = data2.at[0, "λ"]
            temp_max_mat_id = data2.at[0, "模糊矩阵ID"]
            if close_d >= temp2:
                return temp_max_mat_id
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
        # print(name_set)
        if name_set != "":
            data2 = queryFK("", name_set, "", "", "")
            temp2 = data2.at[0, "λ"]
            temp_max_mat_id = data2.at[0, "模糊矩阵ID"]
            if close_d >= temp2:
                return temp_max_mat_id


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
    return min_num_id,max_num_id


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
# 输出绿灯时长
def compete_light_time(cin, alpha, dire):
    sets = fuzzification(cin, alpha)
    mat_id = close_degree(sets, dire)
    B_domain_index_min, B_domain_index_max = compete_end_id(sets, mat_id)

    # 查询B模糊集
    data = queryFKDomain("", "绿灯时长")
    temp = data.at[0, "object"]
    temp = temp.split(";")
    # 根据index获取对应绿灯时长
    res = (int(temp[B_domain_index_min]) + int(temp[B_domain_index_max]))/2
    return res


##############################################################
##############################################################
# 上位机下位机接口
def put_data_to_down(lightTime, direction):
    # ----------------组装数据包，传到下位机-----------------
    lenOfLightTime = len(str(lightTime)) + 2
    ser.write(str(lenOfLightTime).encode(encoding='gbk'))   # 数据包总长度
    ser.write(str(direction).encode(encoding='gbk'))   # 方向
    ser.write(str(lightTime).encode(encoding='gbk'))        # 要更新的绿灯时长


def analysis_data_form_down():
    """
    读取并解析下位机传来的数据包
    :return: 三个int类型：长度，方向，车流量
    """
    # 数据包总长度
    length = ser.read(1).decode()
    # 空的数据包则跳过
    if len(length) == 0:
        return 0, 0, 0
    # 车辆数的位数(字节数）
    LenOfCarNum = int(length) - 2
    if LenOfCarNum < 1:
        carNum = int(ser.read(1).decode())
    else:
        carNum = int(ser.read(LenOfCarNum).decode())
    directionFromLow = int(ser.read(1).decode())
    return length, directionFromLow, carNum
##############################################################


def inference(direction, carNum):
    """
    进行推理
    :param direction: int，方向
    :param carNum: int，车流量
    :return: 绿灯时长（float）和 推理结果（string）
    """
    alpha = 10
    if direction == 0:
        try:
            res = compete_light_time(carNum, alpha, 0)
            msg = "推理成功"
        except Exception:
            msg = "推理失败"
    else:
        # 南北采用可信度知识
        res = Cre_Inference_car_num(carNum)
        msg = "推理成功"
    return res, msg


def emit_start_signal():
    """
    给下位机发出开始信号
    :return: None
    """
    start = "1"
    ser.write(start.encode(encoding='gbk'))


# 推理线程类
class InferenceThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    signal = QtCore.pyqtSignal(int, int)

    def __init__(self):
        super(InferenceThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        print("这是推理线程")
        clearResult()
        emit_start_signal()
        cnt = 0
        while 1:
            # 解析下位机传上来的数据,返回下位机数据长度、车辆方向、车辆数
            if ser.in_waiting > 0:
                length, directionFromLow, carNum = analysis_data_form_down()

                # 将收集到的数据存入传感器数据库
                # if directionFromLow == 0:
                #     insertSensorData(getDateTime(), carNum, 0)
                # else:
                #     insertSensorData(getDateTime(), 0, carNum)

                lightTime, msg = inference(directionFromLow, carNum)
                lightTime = round(lightTime)

                # 发送信号给UI界面
                # 注意这里与_signal = pyqtSignal(str)中的类型相同
                self.signal.emit(carNum, lightTime)

                # 调试信息
                if directionFromLow == 0:
                    print("\n【info】东西方向车流量为：", carNum, "因此将绿灯时长调整为：", lightTime, "\n")
                else:
                    print("\n【info】南北方向车流量为：", carNum, "因此将绿灯时长调整为：", lightTime, "\n")

                # 将传感器获得和推理的结果数据存入数据库
                insertResult(directionFromLow, carNum, lightTime)

                # 传输数据包到下位机
                put_data_to_down(lightTime, directionFromLow)

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
        # 创建线程
        self.thread = InferenceThread()
        # 连接信号
        self.thread.signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # 开始线程
        self.thread.start()

    def call_backlog(self, carNum, lightTime):
        self.child.lineEdit.setText(str(carNum))
        self.child.lineEdit_2.setText(str(lightTime))


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 40)
        self.ax2 = self.ax.twinx()
        self.ax2.set_ylim(0, 75)


class drawThread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    signal = QtCore.pyqtSignal(list, list, list)

    def __init__(self):
        super(drawThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        print("这是绘制折线图线程")
        while True:
            df = queryResult()
            direct = list(df['方向'])
            carnum = list(df['车流量'])
            lighttime = list(df['绿灯时长'])
            self.signal.emit(direct, carnum, lighttime)  # 发送信号
            time.sleep(1)


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
        self.child.pushButton.clicked.connect(self.start_thread)

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
        self.inferencethread = InferenceThread()
        self.inferencethread.start()

        self.drawthread = drawThread()  # 多线程实例化
        self.drawthread.signal.connect(self.Init_Widgets)  # 线程启动槽函数
        self.drawthread.start()  # 启动线程

    def Init_Widgets(self, direct_list, carnum_list, lighttime_list):
        self.PrepareSamples(direct_list, carnum_list, lighttime_list)
        self.PrepareLineCanvas1()
        self.PrepareLineCanvas2()
        self.PrepareLineCanvas3()
        self.PrepareLineCanvas4()

    def set_ax(self, figCanvas):
        figCanvas.ax.set_xlim(0, 10)
        figCanvas.ax.set_ylim(0, 40)
        figCanvas.ax2.set_ylim(0, 75)

    def PrepareSamples(self, direct_list, carnum_list, lighttime_list):
        # 根据方向来选择放入对应的位置
        # 东西方向的数据放入carnum1, lighttime1
        # 南北方向的数据放入carnum2，lighttime2
        carnum1 = []
        carnum2 = []
        lighttime1 = []
        lighttime2 = []

        for i in range(len(direct_list)):
            if direct_list[i] == 0:
                carnum1.append(carnum_list[i])
                lighttime1.append(lighttime_list[i])
            else:
                carnum2.append(carnum_list[i])
                lighttime2.append(lighttime_list[i])
        # 只取10个数据
        self.carnum1 = carnum1[-10:]
        self.carnum2 = carnum2[-10:]
        self.lighttime1 = lighttime1[-10:]
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


# 仿真功能调用
def openExe():
    print("执行exe")



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

    btn10 = window.main_ui.pushButton_7
    btn10.clicked.connect(child10.show)

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

    window.show()
    sys.exit(app.exec_())

