char val;

void setup() {
  //initialize serial communications at a 9600 baud rate
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if(Serial.available()) {
    val = Serial.read();
    if(val == -1) {
      return;
    }
    int state;
    if(val == 'h') {
      Serial.write("high value");
      state = HIGH;
    } else if(val == 'l') {
      Serial.write("low value");
      state = LOW;
    } else {
      return;
    }
    digitalWrite(13, state);
  }
}
