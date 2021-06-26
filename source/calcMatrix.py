import numpy as np
import math
import matplotlib.pyplot as plt

# 论域U,V
U = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# 我们需要求解if A then F中 A和F的模糊关系
# UA的隶属函数
def ua_func(x):
    if x <= 3:
        return 1
    # y = math.exp(-((x-2)/2)**2)
    if x >3 and x <= 6:
        y = -0.33333333 * x + 2
    else:
        y = 0
    return y
# UB的隶属函数
def ub_func(x):
    # y = math.exp(-((x-4)/2)**2)
    if x >=3 and x <= 6:
        y = 0.33333333 * x -1
    elif x >6 and x <=9:
        y = -0.33333333*x + 3
    else:
        y = 0
    return y


# UC的隶属函数
def uc_func(x):
    if x >=7 and x <=10:
        y = 0.33333333*x -7/3
    elif x >10 and x <=13:
        y = -0.333333333*x  + 13/3
    else:
        y = 0

    return y

def ud_func(x):
    if x >=11 and x <=13:
        y = 0.5*x -5.5
    elif x >13 and x<=15:
        y = -0.5*x + 7.5
    else:
        y=0
    return y

def ue_func(x):
    if x >=13 and x <=15:
        y = 0.5*x -6.5
    elif x >15:
        y = 1
    else:
        y = 0
    return y

# def uf_func(x):
#     return x == 3
# UE的隶属函数
# def ue_func(x):
#     return x == 1
# # UD的隶属函数
# def ud_func(x):
#     return x == 0


# UF的隶属函数
def uf_func(x):
    if x >=0 and x <=4:
        y = 1
    elif x >4 and x<=8:
        y = -0.25 *x + 2
    else:
        y = 0
    return y

def ug_func(x):
    if x >=4 and x <=8:
        y = 0.25*x -1
    elif x >8 and x <=12:
        y = -0.25*x +3
    else:
        y = 0
    return y

def uh_func(x):
    if x >=8 and x <=12:
        y = 0.25*x -2
    elif x >12 and x <=16:
        y = -0.25*x +4
    else:
        y = 0
    return y

def ui_func(x):
    if x >=12 and x <=16:
        y = 0.25*x - 3
    elif x >16:
        y = -0.25*x + 5
    else:
        y = 0
    return y

def uj_func(x):
    if x >=16 and x <=20:
        y = 0.25*x -4
    elif x >20:
        y = 1
    else:
        y = 0
    return y

def calcAllMatrix():
    allMatrix = []
    matrixAF = np.zeros((len(U), len(V)))
    for i in range(len(U)):
        for j in range(len(V)):
            matrixAF[i][j] = max(min(ua_func(U[i]), uf_func(V[j])), 1 - ua_func(U[i]))
    print(matrixAF.T)
    print()

    matrixBG = np.zeros((len(U), len(V)))
    for i in range(len(U)):
        for j in range(len(V)):
            matrixBG[i][j] = max(min(ub_func(U[i]), ug_func(V[j])), 1 - ub_func(U[i]))
    print(matrixBG.T)
    print()

    matrixCH= np.zeros((len(U), len(V)))
    for i in range(len(U)):
        for j in range(len(V)):
            matrixCH[i][j] = max(min(uc_func(U[i]), uh_func(V[j])), 1 - uc_func(U[i]))
    print(matrixCH.T)
    print()

    matrixDI = np.zeros((len(U), len(V)))
    for i in range(len(U)):
        for j in range(len(V)):
            matrixDI[i][j] = max(min(ud_func(U[i]), ui_func(V[j])), 1 - uc_func(U[i]))
    print(matrixDI.T)
    print()

    matrixEJ = np.zeros((len(U), len(V)))
    for i in range(len(U)):
        for j in range(len(V)):
            matrixEJ[i][j] = max(min(ue_func(U[i]), uj_func(V[j])), 1 - uc_func(U[i]))
    print(matrixEJ.T)
    print()

    allMatrix.append(matrixAF)
    allMatrix.append(matrixBG)
    allMatrix.append(matrixCH)
    allMatrix.append(matrixDI)
    allMatrix.append(matrixEJ)
    return allMatrix