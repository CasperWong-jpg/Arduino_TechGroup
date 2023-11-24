// Global Variables 
const int en = 8, dir = 10, pulse = 9;

// create stepper object 
StepperTB myStepper(en, dir, pulse);

// initialize pins
const int leftMotorButton = 6;
const int rightMotorButton = 7;
const int pumpButton = 12;
const int pump = 13;

// setup function: runs once
// -----------------------------------------------------------------------------
void setup(){
  // initialize pins
  myStepper.initPins();
}


// loop function: repeats indefinitely
// -------------------------------------------------------------------------------
void loop(){
  test_step(ccw);
}

int readLeftButton() {
  if (digitalRead(leftMotorButton) == HIGH) return 1;
  return 0;
}

int readRightButton() {
  if (digitalRead(rightMotorButton) == HIGH) return 1;
  return 0;
}

int readPumpButton() {
  if (digitalRead(pumpButton) == HIGH) return 1;
  return 0;
}

void water() {
  digitalWrite(pump, LOW);
  delay(800);
  digitalWrite(pump, HIGH);
}

void test_step(int dir){

  // Set speed
  myStepper.setSpeed(120);  //rpm

  // set direction
  myStepper.setDirection(dir);

  // 4 full revolution 
  int numStep = 800;

  // step function to spin motor 
  myStepper.step(numStep);
  delay(1000);  // in mS 
}


void test_rotate(){
  // Set speed
  myStepper.setSpeed(120);  //rpm

  // set direction
  myStepper.setDirection(ccw);

  myStepper.rotate(90);
  delay(1000); 
}
