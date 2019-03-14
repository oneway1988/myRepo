#ifndef _IRNAV_H__
#define _IRNAV_H__
 
 //导入arduino核心头文件
#include "Arduino.h"

#define MAXVALUE_Num      10    // Sensor max value uses Average Value of 10 times
#define MAXVALUE_Delay    100   // 100ms
#define RTVALUE_Num       3    // Sensor realtime value uses Average Value of 3 times
#define RTVALUE_Delay     20   // 10ms

#define NOBLOCK     1
#define NEARBLOCK   2
#define CLOSEBLOCK  3

#define THRD_NEAR   10          //Threshold
#define THRD_CLOSE  100         
#define THRD_HYSIS_NEAR2NO    5           //
#define THRD_HYSIS_CLOSE2NO   30
#define HYSIS_NEAR2NO     50    //time hysteresis ms
#define HYSIS_CLOSE2NEAR  150

class IRNAV
{
  public:
    IRNAV(int IR_Pin);
    ~IRNAV();
    int ValueRead(int N, int T); //read N times and delay T ms each time, return average value of N times.
    void InitMaxValue();
    int GetMaxValue();
    int GetRTValue();
    int Result();
    int GetBlockIdx();

  private:
    int IRsensor_Pin;
    int IRsensor_Value_Max;
    int IRsensor_Value_Realtime;
    int Last_Result;
};

#endif
