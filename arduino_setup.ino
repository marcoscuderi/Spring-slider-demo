
// This is the sketch that should be uploaded to the arduino uno board
// it used a Potentiometer to measure the displacement of the slider -- reading analog voltage
// the scheme for the circuit and ports is shown in figure
// here is a useful tutorial on how to set up and read a potentiometer with arduino
// http://www.toptechboy.com/arduino/lesson-10-analog-reads-on-the-arduino/

int potPin = A0;                        // assign variable to pin that will read

float recRate = 10;                     //[Hz] recording rate number of reads per second
float delayRecRate = (1/recRate)*1000;  //[ms] milliseconds

int readValue;                          // variable to read value that will be assigned later
float Voltage;                          // declare real voltage variable
int recNum;                             // this variable represents the numer of readings

unsigned long StartTime = millis();     // initialize reading for absolute time 

void setup() {
pinMode(potPin, INPUT);         // declare input
Serial.begin(115200);           // start serial port


}

void loop() {

recNum+=1;                                              // set a rec number to derive time
unsigned long CurrentTime = millis();
unsigned long ElapsedTime = CurrentTime - StartTime;    // Calculate elapsed time
readValue = analogRead(potPin);                         // read pin and put in variable (assign the variable to the pin that reads values)
Voltage = (5.0/1023.0)*readValue;                       // calculate the real voltage (see calibration file)

Serial.print(recNum);        // print the value
Serial.print(",");
Serial.print(ElapsedTime);
Serial.print(",");
Serial.print(Voltage,7);
Serial.print(",");
Serial.println(recRate);
delay(delayRecRate);         // delay printing readings

}
