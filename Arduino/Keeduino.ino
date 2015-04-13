#include <SPI.h>
#include <SD.h>
//#include <Servo.h>

//Servo myservo;

int device = 1;
int smsensor = 0;
int tempsensor = 1;
int lightsensor = 2;
int smreading = 0;
int tempreading = 0;
int lightreading = 0;
char data[64];
int pos = 0;

void setup(){
  Serial.begin(9600);
  //myservo.attach(6);
  while(!Serial){
    ;
  }
}

void loop(){
  readMoisture();
  readTemp();
  readLight();
  //readData(tempreading, tempsensor);
  //readData(lightreading, lightsensor);
  //moveServo();
  sendData();
}

void readData(int value, int input){
  value = analogRead(input);
}

void readMoisture(){
  smreading = analogRead(smsensor);
}

void readTemp(){
  tempreading = analogRead(tempsensor);
}

void readLight(){
  lightreading = analogRead(lightsensor);
}

void sendData(){
  //sprintf(data, "%i\t%i\t%i", smreading, tempreading, lightreading);
  //Serial.println(data);
  Serial.print(smreading);
  Serial.print("\t");
  Serial.print(tempreading);
  Serial.print("\t");
  Serial.print(lightreading);
  Serial.println("");
}

//void moveServo(){
//  for(pos = 0; pos < 180; pos +=1){
//    myservo.write(pos);
//    delay(15);
//  }
//  for(pos = 180; pos>=1; pos-=1){
//    myservo.write(pos);
//    delay(15);
//  }
//}
