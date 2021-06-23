'''
使用pandas库的DataFrame进行mysql数据的获取
'''
import pymysql
import pandas as pd
from sqlalchemy import create_engine
import datetime
import test

# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
# con = create_engine('mysql+pymysql://root:wzc2000sxmx.@localhost:3306/intelligent_system')
con = create_engine('mysql+pymysql://root:123456@localhost:3306/ailab')


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


def queryCK(ID=None, premise=None, conclusion=None, time=None, person=None):
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
    if ID==None:
        flags[0] = 0
    if premise==None:
        flags[1] = 0
    if conclusion==None:
        flags[2] = 0
    if time==None:
        flags[3] = 0
    if person==None:
        flags[4] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '00000':
        sql_query = 'select * from 可信度知识表;'
    elif strFlag == '00001':
        sql_query = 'select * from 可信度知识表 where 更新人=' + person + ';'
    elif strFlag == '00010':
        sql_query = 'select * from 可信度知识表 where 更新时间=' + time + ';'
    elif strFlag == '00011':
        sql_query = 'select * from 可信度知识表 where 更新人=' + person + ' and 更新时间=' + time + ';'
    elif strFlag == '00100':
        sql_query = 'select * from 可信度知识表 where 结论=' + conclusion + ';'
    elif strFlag == '00101':
        sql_query = 'select * from 可信度知识表 where 结论=' + conclusion + ' and 更新人=' + person + ';'
    elif strFlag == '00110':
        sql_query = 'select * from 可信度知识表 where 结论=' + conclusion + ' and 更新时间=' + time + ';'
    elif strFlag == '00111':
        sql_query = 'select * from 可信度知识表 where 结论=' + conclusion + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '01000':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ';'
    elif strFlag == '01001':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ' and 更新人=' + person + ';'
    elif strFlag == '01010':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ' and 更新时间=' + time + ';'
    elif strFlag == '01011':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '01100':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ' and 结论=' + conclusion + ';'
    elif strFlag == '01101':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ' and 结论=' + conclusion + ' and 更新人=' + person + ';'
    elif strFlag == '01110':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ' and 结论=' + conclusion + ' and 更新时间=' + time + ';'
    elif strFlag == '01111':
        sql_query = 'select * from 可信度知识表 where 前提=' + premise + ' and 结论=' + conclusion + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '10000':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ';'
    elif strFlag == '10001':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and  更新人=' + person + ';'
    elif strFlag == '10010':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 更新时间=' + time + ';'
    elif strFlag == '10011':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '10100':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=' + conclusion + ';'
    elif strFlag == '10101':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=' + conclusion + ' and 更新人=' + person + ';'
    elif strFlag == '10110':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=' + conclusion + ' and 更新时间=' + time + ';'
    elif strFlag == '10111':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 结论=' + conclusion + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '11000':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ';'
    elif strFlag == '11001':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ' and  更新人=' + person + ';'
    elif strFlag == '11010':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ' and 更新时间=' + time + ';'
    elif strFlag == '11011':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '11100':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ' and 结论=' + conclusion + ';'
    elif strFlag == '11101':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ' and 结论=' + conclusion + ' and 更新人=' + person + ';'
    elif strFlag == '11110':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ' and 结论=' + conclusion + ' and 更新时间=' + time + ';'
    elif strFlag == '11111':
        sql_query = 'select * from 可信度知识表 where ID=' + ID + ' and 前提=' + premise + ' and 结论=' + conclusion + ' and 更新时间=' + time + ' and 更新人=' + person + ';'

    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    print(df_read)


def insertCK(premise, conclusion, cf, lamb, time, person):
    # mysql语句
    sql_insert = "insert into 可信度知识表 values(null, \'" + premise + "\',\'" + conclusion + "\'," + str(cf) \
                 + "," + str(lamb) + ",\'" + time + "\',\'" + person + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条可信度知识")


def queryFK(ID=None, AName=None, BName=None, time=None, person=None):
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
    if ID==None:
        flags[0] = 0
    if AName==None:
        flags[1] = 0
    if BName==None:
        flags[2] = 0
    if time==None:
        flags[3] = 0
    if person==None:
        flags[4] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '00000':
        sql_query = 'select * from 模糊知识表;'
    elif strFlag == '00001':
        sql_query = 'select * from 模糊知识表 where 更新人=' + person + ';'
    elif strFlag == '00010':
        sql_query = 'select * from 模糊知识表 where 更新时间=' + time + ';'
    elif strFlag == '00011':
        sql_query = 'select * from 模糊知识表 where 更新人=' + person + ' and 更新时间=' + time + ';'
    elif strFlag == '00100':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=' + BName + ';'
    elif strFlag == '00101':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=' + BName + ' and 更新人=' + person + ';'
    elif strFlag == '00110':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=' + BName + ' and 更新时间=' + time + ';'
    elif strFlag == '00111':
        sql_query = 'select * from 模糊知识表 where B模糊集名称=' + BName + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '01000':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ';'
    elif strFlag == '01001':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ' and 更新人=' + person + ';'
    elif strFlag == '01010':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ' and 更新时间=' + time + ';'
    elif strFlag == '01011':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '01100':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ';'
    elif strFlag == '01101':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ' and 更新人=' + person + ';'
    elif strFlag == '01110':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ' and 更新时间=' + time + ';'
    elif strFlag == '01111':
        sql_query = 'select * from 模糊知识表 where A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '10000':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ';'
    elif strFlag == '10001':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and  更新人=' + person + ';'
    elif strFlag == '10010':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and 更新时间=' + time + ';'
    elif strFlag == '10011':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '10100':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=' + BName + ';'
    elif strFlag == '10101':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=' + BName + ' and 更新人=' + person + ';'
    elif strFlag == '10110':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=' + BName + ' and 更新时间=' + time + ';'
    elif strFlag == '10111':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and B模糊集名称=' + BName + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '11000':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ';'
    elif strFlag == '11001':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ' and  更新人=' + person + ';'
    elif strFlag == '11010':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ' and 更新时间=' + time + ';'
    elif strFlag == '11011':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ' and 更新时间=' + time + ' and 更新人=' + person + ';'
    elif strFlag == '11100':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ';'
    elif strFlag == '11101':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ' and 更新人=' + person + ';'
    elif strFlag == '11110':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ' and 更新时间=' + time + ';'
    elif strFlag == '11111':
        sql_query = 'select * from 模糊知识表 where ID=' + ID + ' and A模糊集名称=' + AName + ' and B模糊集名称=' + BName + ' and 更新时间=' + time + ' and 更新人=' + person + ';'

    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    print(df_read)


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
    print(strMatrix)
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
    sql_insert = "insert into 模糊集表 values(null, " + Name + "," + ",\'" + strMatrix + "\'"+str(did) + ");"
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
        sql_query = 'select * from 传感器数据表 where 采集时间=' + collectTime + ';'
    elif ID!=None and collectTime==None:
        sql_query = 'select * from 传感器数据表 where ID=' + str(ID) + ';'
    else:
        sql_query = 'select * from 传感器数据表 where ID=' + str(ID) + ' and 采集时间=' + collectTime + ';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    print(df_read)


def insertSensorData(collectTime, carFlow1=0, carFlow2=0):
    """
    插入传感器采集到的数据
    :param collectTime: 采集时间(2021-5-22 23:18:21)
    :param carFlow1: 东西方向的车流量，默认为0
    :param carFlow2: 南北方向的车流量，默认为0
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
        sql_query = 'select * from 上位机数据表 where 下传时间=' + outTime + ';'
    elif ID!=None and outTime==None:
        sql_query = 'select * from 上位机数据表 where ID=' + str(ID) + ';'
    else:
        sql_query = 'select * from 上位机数据表 where ID=' + str(ID) + ' and 下传时间=' + outTime + ';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    print(df_read)


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


if __name__ == '__main__':
    # insertSensorData('2021-5-22 4:50:21', 10, 0)
    # insertSensorData('2021-5-22 4:51:21', 0, 20)
    # insertSensorData('2021-5-22 4:55:21', 36, 0)
    # insertSensorData('2021-5-22 4:56:21', 0, 12)
    
    # insertPCData('2021-5-22 4:50:21', 10, 0)
    # insertPCData('2021-5-22 4:51:21', 0, 20)
    # insertPCData('2021-5-22 4:55:21', 36, 0)
    # insertPCData('2021-5-22 4:56:21', 0, 12)

    # allMatrix = test.calcAllMatrix()
    # insertMatrix(1, 11, allMatrix[0])
    # insertMatrix(2, 12, allMatrix[1])
    # insertMatrix(3, 13, allMatrix[2])
    # insertMatrix(4, 14, allMatrix[3])
    # insertMatrix(5, 15, allMatrix[4])
    
    # insertMatrix(6, 17, allMatrix[0])
    # insertMatrix(7, 18, allMatrix[1])
    # insertMatrix(8, 19, allMatrix[2])
    # insertMatrix(9, 20, allMatrix[3])
    # insertMatrix(10, 21, allMatrix[4])
    queryCK()
    queryFK()
    print()