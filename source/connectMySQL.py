import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
con = create_engine('mysql+pymysql://root:wzc2000sxmx.@localhost:3306/intelligent_system')


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


def insertPCData(sensorDataId, outTime, lightTime1=0, lightTime2=0):
    """
    插入上位机输出的数据
    :param sensorDataId: 传感器数据ID
    :param outTime: 输出时间(2021-5-22 23:18:21)
    :param lightTime1: 东西方向的绿灯时长，默认为0
    :param lightTime2: 南北方向的绿灯时长，默认为0
    :return: none
    """
    # mysql语句
    sql_insert = "insert into 上位机数据表 values(null," + str(sensorDataId) + ",\'" + outTime + "\'," + str(lightTime1) + "," + str(lightTime2) + ");"
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


def initialResult():
    """
    初始化结果数据表，先清空再插入两条初始数据
    :return:
    """
    # mysql语句
    # 必须逐条执行
    sql_insert = ["delete from 结果数据表;", "insert into 结果数据表 values(null, 0, 0, 5);",
                  "insert into 结果数据表 values(null, 2, 0, 0);", "insert into 结果数据表 values(null, 1, 0, 5);",
                  "insert into 结果数据表 values(null, 3, 0, 0);"]

    for stat in sql_insert:
        con.execute(stat)
    print("成功初始化结果数据表")


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


def insertBaiduData(collectTime, carFlow1="未知路况", carFlow2="未知路况"):
    # 插入模糊数据至百度地图API数据库
    # mysql语句
    sql_insert = "insert into 百度地图数据表 values(null, \'" + collectTime + "\',\'" + str(carFlow1) + "\',\'" + str(carFlow2) + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条百度地图API采集的数据")


def queryBaiduData(ID=None, collectTime=None):
    if ID==None and collectTime==None:
        sql_query = 'select * from 百度地图数据表;'
    elif ID==None and collectTime!=None:
        sql_query = 'select * from 百度地图数据表 where 采集时间=\'' + collectTime + '\';'
    elif ID!=None and collectTime==None:
        sql_query = 'select * from 百度地图数据表 where ID=' + str(ID) + ';'
    else:
        sql_query = 'select * from 百度地图数据表 where ID=' + str(ID) + ' and 采集时间=\'' + collectTime + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    # print(df_read)
    return df_read


# 根据ID范围进行查询
def queryBaiduData_twoID(IDf="",IDe=""):
    if IDf=="" and IDe=="":
        sql_query = 'select * from 百度地图数据表;'
    elif IDf=="" and IDe!="":
        sql_query = 'select * from 百度地图数据表 where ID<=' + IDe + ';'
    elif IDf!="" and IDe=="":
        sql_query = 'select * from 百度地图数据表 where ID>=' + IDf + ';'
    else:
        sql_query = 'select * from 百度地图数据表 where ID>=' + IDf + ' and ID<=' + IDe + ';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    return df_read


# 查询解释器表
def queryEX(ID="", SID="",explain=""):
    flags = [1, 1, 1]
    if ID=="":
        flags[0] = 0
    if SID=="":
        flags[1] = 0
    if explain=="":
        flags[2] = 0

    # 转成字符串
    strFlag = ''.join(str(i) for i in flags)
    ID = str(ID)
    if strFlag == '000':
        sql_query = 'select * from 解释器表;'
    elif strFlag == '001':
        sql_query = 'select * from 解释器表 where 解释=\'' + explain + '\';'
    elif strFlag == '010':
        sql_query = 'select * from 解释器表 where 传感器数据ID=' + SID + ';'
    elif strFlag == '100':
        sql_query = 'select * from 解释器表 where ID=' + ID + ';'
    elif strFlag == '011':
        sql_query = 'select * from 解释器表 where 解释=\'' + explain + '\' and 传感器数据ID=' + SID + ';'
    elif strFlag == '101':
        sql_query = 'select * from 解释器表 where 解释=\'' + explain + '\' and ID=' + ID + ';'
    elif strFlag == '110':
        sql_query = 'select * from 解释器表 where ID=' + ID + ' and 传感器数据ID=' + SID + ';'
    elif strFlag == '111':
        sql_query = 'select * from 解释器表 where ID=' + ID + ' and 传感器数据ID=' + SID + ' and 解释=\'' + explain + '\';'
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, con)
    print(df_read)
    return df_read

# 新增解释器表
def insertEX(ID, SID, explain):
    # mysql语句
    sql_insert = "insert into 解释器表 values(null" + "," + str(SID) + ",\'" + explain + "\');"
    # 执行语句
    con.execute(sql_insert)
    print("成功新增一条解释器数据")

# 删除解释器表
def deleteEX(id):
    # mysql语句
    sql_delete = "delete from 解释器表 where ID=" + id +";"
    # 执行语句
    con.execute(sql_delete)
    msg = "成功删除一条解释器信息 ID="+str(id)
    return msg

# 修改解释器表
def updateEX(ID, SID, explain):
    flags = [1, 1, 1, 1]
    if ID=="":
        flags[0] = 0
    if SID=="":
        flags[1] = 0
    if explain=="":
        flags[2] = 0

    if flags[0]==0:
        msg="主键不能为空"
        return msg

    ID = str(ID)
    if flags[0]==1&flags[2]==1:
        sql_update='update 解释器表 set 解释=\'' + explain + '\' where ID=' + ID +';'
        con.execute(sql_update)
    if flags[0]==1&flags[1]==1:
        sql_update='update 解释器表 set 传感器数据ID=' + SID + ' where ID=' + ID +';'
        con.execute(sql_update)
    msg="更新成功，ID="+ID
    print("成功修改一条解释器表")
    return msg
