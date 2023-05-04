#include <cvzone.h>


SerialData serialData(1, 3); //(numOfValsRec,digitsPerValRec)
int valsRec[3]; // array of int with size numOfValsRec 

void setup() {
  pinMode(9, OUTPUT);
  serialData.begin();
}

void loop() {

  serialData.Get(valsRec);
  analogWrite(9, valsRec[0]);

}
