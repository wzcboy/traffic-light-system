// INCLUDE CHRONO LIBRARY : http://github.com/SofaPirate/Chrono
#include <Chrono.h> 

// Set the led's pin
int LedOfYellow = 10;       //定义黄灯的LED接口
int LedOfEastWest = 11;     //定义东西方向的LED 接口
int LedOfSouthNorth = 12;   //定义南北方向的LED 接口
int buttonpin = 3;          //定义避障传感器接口

// for count car
int oldVal = LOW;           //定义避障传感器接口的数字变量val
int newVal = LOW;           //比oldval快一个loop

int direct = 0;            //传感器检测的方向，0代表东西，1代表南北，2代表东西黄灯，3代表南北黄灯
int flag = 0;               //车辆计数

const unsigned long timeInterval = 10000;   //检测车流量间隔10s

int len;                    // 上位机传下来的数据包长度
char dataBuffer[10];        // 上位机传下来的总数据内容：方向和绿灯时长
char timeFromUp[5];         // 上位机传下来的绿灯时长
int directFromUp;           // 上位机传下来的方向:0东西，1南北

unsigned long EastWestTime = 5000;    // 东西方向的绿灯时长
unsigned long SouthNorthTime = 5000;  // 南北方向的绿灯时长
unsigned long YellowTime = 3000;      // 黄灯时长

int state = 0;   // 0代表初始还没开始，1代表检测东西方向的车流量，2代表东西黄灯，3代表检测南北方向的车流量，4代表南北黄灯

// Instantiate two Chronos
Chrono chronoA; 
Chrono chronoB; 
Chrono chronoC;
 
void setup()
{
    pinMode(LedOfYellow, OUTPUT);         //定义LedOfYellow为输出接口
    pinMode(LedOfEastWest, OUTPUT);       //定义LedOfEastWest为输出接口
    pinMode(LedOfSouthNorth, OUTPUT);     //定义LedOfSouthNorth为输出接口
    pinMode(buttonpin, INPUT);            //定义避障传感器为输出接口
    Serial.begin(9600);                   //连接上位机，波特率为9600
}

//当新旧值不同时，说明通过一辆汽车，进行计数
void count(){
    // 接收传感器信号然后发送给上位机
    newVal = digitalRead(buttonpin);
    
    if (oldVal == LOW and newVal == HIGH){   
        flag ++;
    }
    
    // 更新接受传感器的旧数值
    oldVal = newVal;  
}

// 判断num的位数
int numLen(int num){
  if(num < 10){
    return 1;
  }
  else if(num < 100){
    return 2;
  }
  else if(num <1000){
    return 3;
  }
  else{
    return 1;
  }
}

//下位机对传感器数据的处理，包括编码、传输数据到上位机
//获取当前车辆数的长度，组装数据包，重置计数、时间，改变计数方向
void put_data_to_up(){
  int lenOfFlag = numLen(flag);
  Serial.print(lenOfFlag+2);
  Serial.print(flag);
  Serial.print(direct);
}

void analysis_data_from_up(){
  // 数据包内容解析
  len = Serial.read() - '0';
  Serial.readBytes(dataBuffer, len-1);
  dataBuffer[len-1] = '\0';
  directFromUp = dataBuffer[0] - '0';
  strcpy(timeFromUp, dataBuffer+1);
  timeFromUp[len-2] = '\0';

  // 更新两个方向的绿灯时长
  if(len > 0){
      if(directFromUp == 0){
          EastWestTime = atoi(timeFromUp) * 1000UL;
          if(EastWestTime < 5000){
              EastWestTime = 5000;
          }
      } else if(directFromUp == 1){
          SouthNorthTime = atoi(timeFromUp) * 1000UL;
          if(SouthNorthTime < 5000){
              SouthNorthTime = 5000;
          }
       } 
  } 
}

void state0(){
  char sig = Serial.read();
  if(sig == '1'){
    state = 1;
    chronoA.restart();
  }
  else{
    state = 0;
  }
}

//状态0东西绿灯显示，同时检测东西车流量
void state1(){
  count();
  digitalWrite(LedOfEastWest, HIGH);
  if(chronoA.hasPassed(EastWestTime)) {
    put_data_to_up();
    if(Serial.available() > 0){
        analysis_data_from_up();    
    }
    // change
    chronoB.restart();  // restart the crono so that it triggers again later
    digitalWrite(LedOfEastWest, LOW);
    state = 2;
    flag = 0;
    direct = 2;
  }
}

//东西黄灯显示
void state2(){
  digitalWrite(LedOfYellow, HIGH);
  if(chronoB.hasPassed(YellowTime)) {
    put_data_to_up();
    if(Serial.available() > 0){
        analysis_data_from_up();    
    }
    // change
    chronoC.restart();  // restart the crono so that it triggers again later
    digitalWrite(LedOfYellow, LOW);
    state = 3;
    direct = 1;
  }
}

void state3(){
  count();
  digitalWrite(LedOfSouthNorth, HIGH);
  if(chronoC.hasPassed(SouthNorthTime)) {
    put_data_to_up();
    if(Serial.available() > 0){
        analysis_data_from_up();    
    }
    // change
    chronoB.restart();  // restart the crono so that it triggers again later
    digitalWrite(LedOfSouthNorth, LOW);
    state = 4;
    flag = 0;
    direct = 3;
  }
}

//东西黄灯显示
void state4(){
  digitalWrite(LedOfYellow, HIGH);
  if(chronoB.hasPassed(YellowTime)) {
    put_data_to_up();
    if(Serial.available() > 0){
        analysis_data_from_up();    
    }
    // change
    chronoA.restart();  // restart the crono so that it triggers again later
    digitalWrite(LedOfYellow, LOW);
    state = 1;
    direct = 0;
  }
}

void loop()
{
  if(state == 0){
    state0();
  }
  else if(state == 1){
    state1();
  }
  else if(state == 2){
    state2();
  }
  else if(state == 3){
    state3();
  }
  else if(state == 4){
    state4();
  }

}
