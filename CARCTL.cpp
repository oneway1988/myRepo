#include "CARCTL.h"

CARCTL::CARCTL(int L1_0, int L1_1, int L2_0, int L2_1, int R1_0, int R1_1, int R2_0, int R2_1)
 {
    motorL1_0 = L1_0;
    motorL1_1 = L1_1;
    motorL2_0 = L2_0;
    motorL2_1 = L2_1;
    motorR1_0 = R1_0;
    motorR1_1 = R1_1;
    motorR2_0 = R2_0;
    motorR2_1 = R2_1;
    pinMode(motorL1_0, OUTPUT);
    pinMode(motorL1_1, OUTPUT);
    pinMode(motorL2_0, OUTPUT);
    pinMode(motorL2_1, OUTPUT);
    pinMode(motorR1_0, OUTPUT);
    pinMode(motorR1_1, OUTPUT);
    pinMode(motorR2_0, OUTPUT);
    pinMode(motorR2_1, OUTPUT);
    digitalWrite(motorL1_0,LOW);
    digitalWrite(motorL1_1,LOW);
    digitalWrite(motorL2_0,LOW);
    digitalWrite(motorL2_1,LOW);
    digitalWrite(motorR1_0,LOW);
    digitalWrite(motorR1_1,LOW);
    digitalWrite(motorR2_0,LOW);
    digitalWrite(motorR2_1,LOW);
    state = STATE_STOP;
    spd = SPEED_STOP;
    spdChgFlag = false;
 }
 
CARCTL::~CARCTL()
 {
    disattach();
 }

void CARCTL::stopping()
{
    if (state != STATE_STOP) {
      digitalWrite(motorL1_0,LOW);
      digitalWrite(motorL1_1,LOW);
      digitalWrite(motorL2_0,LOW);
      digitalWrite(motorL2_1,LOW);
      digitalWrite(motorR1_0,LOW);
      digitalWrite(motorR1_1,LOW);
      digitalWrite(motorR2_0,LOW);
      digitalWrite(motorR2_1,LOW);
      state = STATE_STOP;
    }
}
  
void CARCTL::forward()
{
  if (state != STATE_FORWARD || spdChgFlag == true) {
    analogWrite(motorL1_0,0);
    analogWrite(motorL1_1,spd);
    analogWrite(motorL2_0,0);
    analogWrite(motorL2_1,spd);
    analogWrite(motorR1_0,0);
    analogWrite(motorR1_1,spd);
    analogWrite(motorR2_0,0);
    analogWrite(motorR2_1,spd);
    state = STATE_FORWARD;
    spdChgFlag == false;
  }
}
void CARCTL::backward()
{
  if (state != STATE_BACKWARD || spdChgFlag == true) {
    analogWrite(motorL1_0,spd);
    analogWrite(motorL1_1,0);
    analogWrite(motorL2_0,spd);
    analogWrite(motorL2_1,0);
    analogWrite(motorR1_0,spd);
    analogWrite(motorR1_1,0);
    analogWrite(motorR2_0,spd);
    analogWrite(motorR2_1,0);
    state = STATE_BACKWARD;
    spdChgFlag == false;
  }
}
void CARCTL::turnleft()
{
  if (state != STATE_TURNLEFT) {
    analogWrite(motorL1_0,0);
    analogWrite(motorL1_1,0);
    analogWrite(motorL2_0,0);
    analogWrite(motorL2_1,0);
    analogWrite(motorR1_0,0);
    analogWrite(motorR1_1,spd);
    analogWrite(motorR2_0,0);
    analogWrite(motorR2_1,spd);
    state = STATE_TURNLEFT;
  }
}
void CARCTL::turnright()
{
  if (state != STATE_TURNRIGHT) {
    analogWrite(motorL1_0,0);
    analogWrite(motorL1_1,spd);
    analogWrite(motorL2_0,0);
    analogWrite(motorL2_1,spd);
    analogWrite(motorR1_0,0);
    analogWrite(motorR1_1,0);
    analogWrite(motorR2_0,0);
    analogWrite(motorR2_1,0);
    state = STATE_TURNRIGHT;
  }
}
void CARCTL::leftaround()
{
  if (state != STATE_LEFTAROUND) {
    analogWrite(motorL1_0,spd);
    analogWrite(motorL1_1,0);
    analogWrite(motorL2_0,spd);
    analogWrite(motorL2_1,0);
    analogWrite(motorR1_0,0);
    analogWrite(motorR1_1,spd);
    analogWrite(motorR2_0,0);
    analogWrite(motorR2_1,spd);
    state = STATE_LEFTAROUND;
  }
}
void CARCTL::speedup()
{
  switch (spd) {
    case SPEED_STOP:
      spd = SPEED_LOW;
      spdChgFlag = true;
      break;
    case SPEED_LOW:
      spd = SPEED_MEDIUM;
      spdChgFlag = true;
      break;
    case SPEED_MEDIUM:
      spd = SPEED_HIGH;
      spdChgFlag = true;
      break;
    default:
      spdChgFlag = false;
      break;
  }
}

void CARCTL::speeddown()
{
  switch (spd) {
    case SPEED_LOW:
      spd = SPEED_STOP;
      spdChgFlag = true;
      break;
    case SPEED_MEDIUM:
      spd = SPEED_LOW;
      spdChgFlag = true;
      break;
    case SPEED_HIGH:
      spd = SPEED_MEDIUM;
      spdChgFlag = true;
      break;
    default:
      spdChgFlag = false;
      break;
  }
}

void CARCTL::speedcontrol()
{
  
}
char CARCTL::getstate()
{
  
}
char CARCTL::getspeed()
{
  
}
 void CARCTL::disattach()
{
    digitalWrite(motorL1_0,LOW);
    digitalWrite(motorL1_1,LOW);
    digitalWrite(motorL2_0,LOW);
    digitalWrite(motorL2_1,LOW);
    digitalWrite(motorR1_0,LOW);
    digitalWrite(motorR1_1,LOW);
    digitalWrite(motorR2_0,LOW);
    digitalWrite(motorR2_1,LOW);
    pinMode(motorL1_0, INPUT);
    pinMode(motorL1_1, INPUT);
    pinMode(motorL2_0, INPUT);
    pinMode(motorL2_1, INPUT);
    pinMode(motorR1_0, INPUT);
    pinMode(motorR1_1, INPUT);
    pinMode(motorR2_0, INPUT);
    pinMode(motorR2_1, INPUT);
}
