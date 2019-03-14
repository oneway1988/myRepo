
#ifndef _CARCTL_H__
#define _CARCTL_H__
 
 //导入arduino核心头文件
#include "Arduino.h"

#define STATE_STOP        2
#define STATE_FORWARD     3
#define STATE_BACKWARD    4
#define STATE_TURNLEFT    5
#define STATE_TURNRIGHT   6
#define STATE_LEFTAROUND  7

#define SPEED_HIGH    255
#define SPEED_MEDIUM  190
#define SPEED_LOW     110
#define SPEED_STOP    0

class CARCTL
{
    public:
      CARCTL(int L1_0, int L1_1, int L2_0, int L2_1, int R1_0, int R1_1, int R2_0, int R2_1); //构造函数
      ~CARCTL();                     //析构函数
      int getPin();         //获取控制的引脚
      void stopping();      //停止  
      void forward();       //前进
      void backward();      //后退
      void turnleft();      //左转
      void turnright();     //右转
      void leftaround();    //左转圈
      void speedup();       //加速
      void speeddown();     //减速
      void speedcontrol(); //速度控制
      char getstate();      //获取状态
      char getspeed();      //获取速度
      void disattach();     //释放引脚，使得引脚可以控制其他的东西

    private:
      int motorL1_0;        //左前马达负
      int motorL1_1;         //左前马达正
      int motorL2_0;        //左后马达负
      int motorL2_1;         //左后马达正
      int motorR1_0;        //右前马达负
      int motorR1_1;         //右前马达正
      int motorR2_0;        //右后马达负
      int motorR2_1;      //右后马达正
      int spd;            //速度，范围0~255
      int state;          //状态 STATE_STOP STATE_FORWARD STATE_BACKWARD STATE_TURNLEFT STATE_TURNRIGHT"
      bool spdChgFlag;    //速度改变指示
};

#endif
