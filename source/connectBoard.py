"""
@name: lab1.py
@Describe: 通过python的串口库与下位机单片机通信
"""

import serial

# 硬件相关设置
serialPort = "/dev/cu.usbmodem14201"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)  # 连接串口
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

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