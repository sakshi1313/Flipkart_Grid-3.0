#include <Arduino.h>
#include <WiFiClient.h>
#include <WiFi.h>
#include <Servo.h>

const char* ssid     = "AMAN AARYA";
const char* password = "Aarya201@";
const int duration = 200;
//#define led_p1 d23;
//#define led_n1 d22;
//#define led_p2 d14;
//#define led_n2 d32;
#define motor1in1 d6;
#define motor1in2 d7;
#define motor2in3 d3;
#define motor2in4 d4;
#define enable1 d5;
#define enable2 d2;
#define servoPin d1;
int pos = 0;
int m1high=255,m2high=255;
int m1mid=180,m2mid=180;
int m1low=120,m2low=120;
Servo myservo;  // create servo object to control a servo
// 16 servo objects can be created on the ESP32
 
WiFiServer server(80);

void setup()
{
  Serial.begin(115200);
  pinMode(motor1in1, OUTPUT);
  pinMode(motor1in2, OUTPUT);
  pinMode(motor2in3, OUTPUT);
  pinMode(motor2in4, OUTPUT);
  pinMode(enable1,OUTPUT);
  pinMode(enable2,OUTPUT);
  pinMode(led_p1, OUTPUT);
  pinMode(led_n1, OUTPUT);
  pinMode(led_p2, OUTPUT);
  pinMode(led_n2, OUTPUT);
  delay(10);
  myservo.attach(servoPin, 500, 2400); // attaches the servo on pin 18 to the servo object
  // using default min/max of 1000us and 2000us
  // different servos may require different min/max settings
  // for an accurate 0 to 180 sweep

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();

}

int value = 0;

void loop() {
  digitalWrite(led_n1, LOW);
  digitalWrite(led_p1, HIGH);
  digitalWrite(led_n2, LOW);
  digitalWrite(led_p2, HIGH);
  WiFiClient client = server.available();   // listen for incoming clients

  if (client) {                             // if you get a client,
    //Serial.println("New Client.");           // print a message out the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {            // loop while the client's connected
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        if (c == '\n') {                    // if the byte is a newline character

          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            // the content of the HTTP response follows the header:
            client.print("<a href=\"/Forward1\">Forward1</a>.<br>");
            client.print("<a href=\"/Forward2\">Forward2</a>.<br>");
            client.print("<a href=\"/sleft\">sleft</a>.<br>");
            client.print("<a href=\"/sright\">sright</a>.<br>");
            client.print("<a href=\"/Left\">Left</a>.<br>");
            client.print("<a href=\"/Right\">Right</a>.<br>");
            client.print("<a href=\"/Stop\">Stop</a>.<br>");
            client.print("<a href=\"/Flip\">Flip</a>.<br>");
           


            // The HTTP response ends with another blank line:
            client.println();
            // break out of the while loop:
            break;
          } else {    // if you got a newline, then clear currentLine:
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }

        // forward
        if (currentLine.endsWith("GET /Forward1")) {
          //FOR Left Motor Forward
          analogWrite(enable1,m1high);
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, HIGH);
          //FOR Right Motor Forward
          analogWrite(enable2,m2high);
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, HIGH);
          delay(duration);
          digitalWrite(motor1in1,LOW);
          digitalWrite(motor1in2,LOW);
          digitalWrite(motor2in3,LOW);
          digitalWrite(motor2in4,LOW);
        }

        // forward
        if (currentLine.endsWith("GET /Forward2")) {
          //FOR Left Motor Forward
          analogWrite(enable1,m1low);
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, HIGH);
          //FOR Right Motor Forward
          analogWrite(enable2,m2low);
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, HIGH);
          delay(6*duration);
          //FOR STOP
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, LOW);
          //FOR STOP
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, LOW);

//          digitalWrite(enable1,HIGH);
//          digitalWrite(motor1in1,LOW);
//          digitalWrite(motor1in2, HIGH);
//          //FOR Right Motor Backward
//          digitalWrite(enable2,HIGH);
//          digitalWrite(motor2in3, HIGH);
//          digitalWrite(motor2in4, LOW);
//          delay(0.25*duration/3);
//          //FOR STOP
//          digitalWrite(enable1,HIGH);
//          digitalWrite(motor1in1, LOW);
//          digitalWrite(motor1in2, LOW);
//          //FOR STOP
//          digitalWrite(enable2,HIGH);
//          digitalWrite(motor2in3, LOW);
//          digitalWrite(motor2in4, LOW);
        }
        if (currentLine.endsWith("GET /Left")) {
          
          analogWrite(enable1,m1high);
          digitalWrite(motor1in1, HIGH);
          digitalWrite(motor1in2, LOW);
         
          analogWrite(enable2,m2high);
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, HIGH);
          delay(0.75*duration);
          //FOR STOP
          
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, LOW);
          //FOR STOP
          
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, LOW);
        }
        
        if (currentLine.endsWith("GET /Right")) {
          
          analogWrite(enable1,m1high);
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, HIGH);
          
          analogWrite(enable2,m2high);
          digitalWrite(motor2in3, HIGH);
          digitalWrite(motor2in4, LOW);
          delay(duration);
          //FOR STOP
          
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, LOW);
          //FOR STOP
          
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, LOW);
        }
        
        if (currentLine.endsWith("GET /sright")) {
          //FOR Left Motor Backward
          analogWrite(enable1,m1high);
          digitalWrite(motor1in1,LOW);
          digitalWrite(motor1in2, HIGH);
          //FOR Right Motor Backward
          analogWrite(enable2,m2high);
          digitalWrite(motor2in3, HIGH);
          digitalWrite(motor2in4, LOW);
          delay(0.25*duration/3);
          //FOR STOP
          
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, LOW);
          //FOR STOP
          
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, LOW);
        }
        if (currentLine.endsWith("GET /sleft")) {
          //FOR Left Motor Backward
          analogWrite(enable1,m1high);
          digitalWrite(motor1in1,HIGH);
          digitalWrite(motor1in2, LOW);
          //FOR Right Motor Backward
          analogWrite(enable2,m2high);
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, HIGH);
          delay(0.25*duration/3);
          //FOR STOP
          
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, LOW);
          //FOR STOP
          
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, LOW);
        }
        if (currentLine.endsWith("GET /Stop")) {
          //FOR STOP
          analogWrite(enable1,0);
          digitalWrite(motor1in1, LOW);
          digitalWrite(motor1in2, LOW);
          //FOR STOP
          analogWrite(enable2,0);
          digitalWrite(motor2in3, LOW);
          digitalWrite(motor2in4, LOW);
        }
        if (currentLine.endsWith("GET /Flip")) {
          for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);    // tell servo to go to position in variable 'pos'
    delay(5);             // waits 15ms for the servo to reach the position
  }
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);    // tell servo to go to position in variable 'pos'
    delay(5);             // waits 15ms for the servo to reach the position
  }
        }
      }
    }
    // close the connection:
    client.stop();
    //Serial.println("Client Disconnected.");
  }
}
