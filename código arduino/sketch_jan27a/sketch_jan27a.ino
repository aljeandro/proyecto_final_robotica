#include <SoftwareSerial.h>
SoftwareSerial HC06(9, 10);

int IN3 = 5;
int IN4 = 4;
int ENB = 3;

int IN1 = 6;
int IN2 = 13;
int ENA = 11;

void setup() {
  HC06.begin(9600);
  Serial.begin(9600);
  
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {

  if (HC06.available() > 0)
    {
      char receive = HC06.read();
      
      if(receive == '1') //Detenerse
      {
        Serial.println("Detenerse");
        
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);

        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);

        analogWrite(ENB, 0);
        analogWrite(ENA, 0);
      }
      else if(receive == '2') // Movimiento recto
      {
        Serial.println("Movimiento recto");

        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);

        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);

        analogWrite(ENB, 150);
        analogWrite(ENA, 150);
      }
      else if(receive == '3') // Girar a la derecha
      {
        Serial.println("Girar a la derecha");
        
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);

        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
        
        analogWrite(ENB, 170);
        analogWrite(ENA, 170);
        
      }
      else if(receive == '4') // Girar a la izquierda
      {
        Serial.println("Girar a la izquierda");

        digitalWrite(IN2, LOW);
        digitalWrite(IN1, LOW);
        
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);

        analogWrite(ENB, 170);
        analogWrite(ENA, 170);
      }
    }

}
