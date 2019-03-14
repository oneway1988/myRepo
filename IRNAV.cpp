#include "IRNAV.h"

IRNAV::IRNAV(int IR_Pin)
{
  IRsensor_Pin = IR_Pin;
  IRsensor_Value_Realtime = 1023;  
  Last_Result = NOBLOCK;
  IRsensor_Value_Max = 1023;
}

IRNAV::~IRNAV()
{
  
}

int IRNAV::ValueRead(int N, int T)
{
  int ValueTem = 0;
  int n = N;
  int Tms = T;
  for (int i = 1; i <= n; i++) {
    ValueTem = ValueTem+analogRead(IRsensor_Pin);
    delay(Tms);
  }
  return (ValueTem/n);
}

int IRNAV::GetMaxValue()
{
  return IRsensor_Value_Max;
}

void IRNAV::InitMaxValue()
{
    IRsensor_Value_Max = ValueRead(MAXVALUE_Num,MAXVALUE_Delay);
}

int IRNAV::GetRTValue()
{
  return ValueRead(RTVALUE_Num,RTVALUE_Delay);
}

int IRNAV::GetBlockIdx(){
  return max(0,(IRsensor_Value_Max - ValueRead(RTVALUE_Num,RTVALUE_Delay)));
}

int IRNAV::Result()
{
  IRsensor_Value_Realtime = ValueRead(RTVALUE_Num,RTVALUE_Delay);
  if (Last_Result == NOBLOCK) {
    if (IRsensor_Value_Realtime < (IRsensor_Value_Max - THRD_CLOSE)) {
      Last_Result = CLOSEBLOCK;
      return CLOSEBLOCK;
    }else if (IRsensor_Value_Realtime < (IRsensor_Value_Max - THRD_NEAR)) {
      Last_Result = NEARBLOCK;
      return NEARBLOCK;    
    }else{
      Last_Result = NOBLOCK;
      return NOBLOCK;          
    }
  }
  
  if (Last_Result == NEARBLOCK) {
    if (IRsensor_Value_Realtime < (IRsensor_Value_Max - THRD_CLOSE)) {
      Last_Result = CLOSEBLOCK;
      return CLOSEBLOCK;
    }else if (IRsensor_Value_Realtime >= (IRsensor_Value_Max - THRD_NEAR + THRD_HYSIS_NEAR2NO)) {
      delay(HYSIS_NEAR2NO);
      IRsensor_Value_Realtime = ValueRead(RTVALUE_Num,RTVALUE_Delay);
      if (IRsensor_Value_Realtime >= (IRsensor_Value_Max - THRD_NEAR + THRD_HYSIS_NEAR2NO)) {
        Last_Result = NOBLOCK;
        return NOBLOCK;    
      }else if (IRsensor_Value_Realtime < (IRsensor_Value_Max - THRD_CLOSE)){
        Last_Result = CLOSEBLOCK;
        return CLOSEBLOCK;
      }else{
        Last_Result = NEARBLOCK;
        return NEARBLOCK;           
      }
    }else{
      Last_Result = NEARBLOCK;
      return NEARBLOCK;          
    }
  }
  
  if (Last_Result == CLOSEBLOCK) {
    if (IRsensor_Value_Realtime >= (IRsensor_Value_Max - THRD_CLOSE + THRD_HYSIS_CLOSE2NO)) {
      delay(HYSIS_CLOSE2NEAR);
      IRsensor_Value_Realtime = ValueRead(RTVALUE_Num,RTVALUE_Delay);
      if (IRsensor_Value_Realtime >= (IRsensor_Value_Max - THRD_CLOSE + THRD_HYSIS_CLOSE2NO)){
        Last_Result = NEARBLOCK;
        return NEARBLOCK;  
      }else{
        Last_Result = CLOSEBLOCK;
        return CLOSEBLOCK;
      }   
    }else{
      Last_Result = CLOSEBLOCK;
      return CLOSEBLOCK;
    }
  }
}
