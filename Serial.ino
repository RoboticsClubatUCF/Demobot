#include <SoftwareSerial.h>

SoftwareSerial gpsSerial(11, 12); // RX, TX (TX not used)
const int sentenceSize = 80;
char sentence[sentenceSize];

// defines pins numbers
const int trigPin1 = 10;
const int echoPin1 = 9;
const int trigPin2 = 8;
const int echoPin2 = 7;
const int trigPin3 = 6;
const int echoPin3 = 5;
const int trigPin4 = 4;
const int echoPin4 = 3;
// defines variables
long duration1;
int distance1;
long duration2;
int distance2;
long duration3;
int distance3;
long duration4;
int distance4;

void setup()
{
  pinMode(trigPin1, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin1, INPUT); // Sets the echoPin as an 
  pinMode(trigPin2, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin2, INPUT); // Sets the echoPin as an Input
  pinMode(trigPin3, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin3, INPUT); // Sets the echoPin as an 
  pinMode(trigPin4, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin4, INPUT); // Sets the echoPin as an Input
  
  Serial.begin(9600);
  gpsSerial.begin(9600);
}

void loop()
{
  static int i = 0;
  if (gpsSerial.available())
  {
    char ch = gpsSerial.read();
    if (ch != '\n' && i < sentenceSize)
    {
      sentence[i] = ch;
      i++;
    }
    else
    {
     sentence[i] = '\0';
     i = 0;
     displayGPS();
    }
  }
}

void displayGPS()
{
  char field[20];
  getField(field, 0);
  if (strcmp(field, "$GPRMC") == 0)
  {
    // Clears the trigPin
    digitalWrite(trigPin1, LOW);
    delay(50);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin1, HIGH);
    delay(50);
    digitalWrite(trigPin1, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration1 = pulseIn(echoPin1, HIGH);
    // Calculating the distance
    distance1 = duration1*0.034/2;
    // Prints the distance on the Serial Monitor
    Serial.print("0000 ");
    Serial.println(distance1);

    // Clears the trigPin
    digitalWrite(trigPin2, LOW);
    delay(50);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin2, HIGH);
    delay(50);
    digitalWrite(trigPin2, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration2 = pulseIn(echoPin2, HIGH);
    // Calculating the distance
    distance2 = duration2*0.034/2;
    // Prints the distance on the Serial Monitor
    Serial.print("0001 ");
    Serial.println(distance2);

    // Clears the trigPin
    digitalWrite(trigPin3, LOW);
    delay(50);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin3, HIGH);
    delay(50);
    digitalWrite(trigPin3, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration3 = pulseIn(echoPin3, HIGH);
    // Calculating the distance
    distance3 = duration3*0.034/2;
    // Prints the distance on the Serial Monitor
    Serial.print("0010 ");
    Serial.println(distance3);

    // Clears the trigPin
    digitalWrite(trigPin4, LOW);
    delay(50);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin4, HIGH);
    delay(50);
    digitalWrite(trigPin4, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration4 = pulseIn(echoPin4, HIGH);
    // Calculating the distance
    distance4 = duration4*0.034/2;
    // Prints the distance on the Serial Monitor
    Serial.print("0011 ");
    Serial.println(distance4);
    
    Serial.print("0100 ");
    getField(field, 3);  // number
    Serial.println(field);
    
    Serial.print("0101 ");
    getField(field, 5);  // number
    Serial.println(field);
  }
}

void getField(char* buffer, int index)
{
  int sentencePos = 0;
  int fieldPos = 0;
  int commaCount = 0;
  while (sentencePos < sentenceSize)
  {
    if (sentence[sentencePos] == ',')
    {
      commaCount ++;
      sentencePos ++;
    }
    if (commaCount == index)
    {
      buffer[fieldPos] = sentence[sentencePos];
      fieldPos ++;
    }
    sentencePos ++;
  }
  buffer[fieldPos] = '\0';
} 
