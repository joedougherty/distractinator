/*
Mapping of M4 Receiver pins to transmitter buttons
--------------------------------------------------
D0: "D" button
D1: "C" button
D2: "B" button
D3: "A" button
*/

const int buttonPinA = 12; // D12
const int buttonPinB = 6;  // D6
const int buttonPinC = 9;  // D9
const int buttonPinD = 10; // D10

int buttonStateA = 0;
int lastButtonStateA = 0;

int buttonStateB = 0;
int lastButtonStateB = 0;

int buttonStateC = 0;
int lastButtonStateC = 0;

int buttonStateD = 0;
int lastButtonStateD = 0;

void setup() {
  pinMode(buttonPinA, INPUT);
  pinMode(buttonPinB, INPUT);
  pinMode(buttonPinC, INPUT);
  pinMode(buttonPinD, INPUT);
  
  Serial.begin(9600); 
}

void loop() {
  buttonStateA = digitalRead(buttonPinA);
  buttonStateB = digitalRead(buttonPinB);
  buttonStateC = digitalRead(buttonPinC);
  buttonStateD = digitalRead(buttonPinD);

  // A Button  
  if (buttonStateA != lastButtonStateA) {
    if (buttonStateA == HIGH) {      
      Serial.println("a_recvd");
    } else {
      Serial.println("a_off");
    }
  }
  
  lastButtonStateA = buttonStateA;
  
  // B Button
  if (buttonStateB != lastButtonStateB) {
    if (buttonStateB == HIGH) {      
      Serial.println("b_recvd");
    } else {
      Serial.println("b_off");
    }
  }
  
  lastButtonStateB = buttonStateB;
  
  // C Button
  if (buttonStateC != lastButtonStateC) {
    if (buttonStateC == HIGH) {      
      Serial.println("c_recvd");
    } else {
      Serial.println("c_off");
    }
  }
  
  lastButtonStateC = buttonStateC;
  
  // D Button
  if (buttonStateD != lastButtonStateD) {
    if (buttonStateD == HIGH) {      
      Serial.println("d_recvd");
    } else {
      Serial.println("d_off");
    }
  }
  
  lastButtonStateD = buttonStateD;
}

