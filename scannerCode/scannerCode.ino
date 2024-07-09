#include <AFMotor.h>

// Define the pins for the ultrasonic sensor
const int trigPin = 28;
const int echoPin = 46;

AF_Stepper motor1(200, 1);  // Create motor1 instance with 200 steps per revolution, connected to port 1
AF_Stepper motor2(200, 2);  // Create motor2 instance with 200 steps per revolution, connected to port 2

void setup() {
  Serial.begin(9600);       // Start serial communication at 9600 baud

  // Set the ultrasonic sensor pins as input and output
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  motor1.setSpeed(100);     // Set initial speed for motor1 (100 RPM)
  motor2.setSpeed(100);     // Set initial speed for motor2 (100 RPM)
}

double readUltrasonicSensor() {
  // Send a 10-microsecond pulse to trigger pin to start the ranging
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the signal from the echo pin, which is the time (in microseconds) from sending to receiving the echo
  long duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in cm
  double distance = (duration * 0.034) / 2;

  return distance;
}

void loop() {
  for(int k = 0; k < 30; k ++) {
    // Move motor1 by 1 degree every second till 360 degrees
    for (int i = 0; i < 46; i++) {
      motor1.step(1, FORWARD, SINGLE);  // Move motor1 one step forward

      // Measure distance 20 times during each step of motor1
      for (int j = 0; j < 20; j++) {
        double distance = readUltrasonicSensor();  // Read and convert the distance from the ultrasonic sensor
        Serial.println(distance);
      }

      delay(1000);  // Wait for 1 second
    }

    // Move motor2 by 1 degree every second till 360 degrees
    for (int i = 0; i < 5; i++) {
      motor2.step(1, BACKWARD, SINGLE);  // Move motor2 one step backward
      delay(1000);                      // Wait for 1 second
    }
  }

  for (int i = 0; i < 60; i++) {
    motor2.step(1, FORWARD, SINGLE);  // Move motor2 one step backward
    delay(100);                      // Wait for 1 second
  }

  // Add any additional logic here if needed
  while (true); // Stops the loop
}
