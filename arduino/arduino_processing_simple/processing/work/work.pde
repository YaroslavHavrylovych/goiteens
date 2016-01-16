import processing.serial.*;

Serial myPort;
String val;
OurButton ourButton = new OurButton(100, 100, 50, 50);

void setup() {
  size(500, 500);
  String portName = "/dev/ttyUSB0";//Serial.list()[0];
  myPort = new Serial(this, portName, 9600); 
  //draw
}

void draw() {
  if ( myPort.available() > 0) 
  {  // If data is available,
    val = myPort.readStringUntil('\n');         // read it and store it in val
    if(val != null) {
      println(val); //print it out in the console
    }
  } 
  //draw
  background(200, 200, 200);
  ourButton.draw();
}

void mouseClicked() {
  if(overRect(ourButton.mX, ourButton.mY, ourButton.mWidth, ourButton.mHeight)) {
    ourButton.setPressed(!ourButton.pressed);
  }
}

boolean overRect(int mX, int mY, int mWidth, int mHeight)  {
  println("x = " + mX + ", mY = " + mY);
  if (mouseX >= mX && mouseX <= mX+mWidth && 
      mouseY >= mY && mouseY <= mY+mHeight) {
    return true;
  } else {
    return false;
  }
}

class OurButton {
  int mX; 
  int mY; 
  int mWidth; 
  int mHeight;
  public boolean pressed;
  
  OurButton(int mX, int mY, int mWidth, int mHeight) {
    this.mX = mX;
    this.mY = mY;
    this.mWidth = mWidth;
    this.mHeight = mHeight;
  }
  
  public void setPressed(boolean value) {
    pressed = value;
    if(pressed) {
      myPort.write('h');
    } else {
      myPort.write('l');
    }
  }
  
  public void draw() {
    if(pressed) {
      fill(100, 0, 0);
    } else {
      fill(0, 100, 0);
    }
    stroke(255);
    rect(mX, mY, mWidth, mHeight);
  }
}
