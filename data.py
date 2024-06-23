import serial
import time

# Set up the serial connection (replace 'COM3' with your serial port)
ser = serial.Serial('/dev/cu.usbserial-10', 9600, timeout=1)

data_counter = 0
value = 0

# Open a file to save the readings
with open('ultrasonic_readings.txt', 'w') as file:
    while True:
        if ser.in_waiting > 0:
            # Read the data from the serial port
            line = float(ser.readline().decode('utf-8').strip())
            
            if data_counter == 19:
                value = value / 20
                
                # Print the data to the console (optional)
                print(value)
                
                # Write the data to the file
                file.write(value + '\n')
                
                value = 0
                data_counter = 0
            else:
                value = value + line
                data_counter += 1
                print(value)

        # Small delay to avoid high CPU usage
        time.sleep(0.1)
