import serial
import time

# Set up the serial connection (replace 'COM3' with your serial port)
ser = serial.Serial('/dev/cu.usbserial-10', 9600, timeout=1)

ding_counter = 0
data_counter = 0
value = 0

# Open a file to save the readings
with open('ideal.txt', 'w') as file:
    while True:
        if ser.in_waiting > 0:
            # Read the data from the serial port
            line = float(ser.readline().decode('utf-8').strip())
            
            if ding_counter == 45:
                # Print output to terminal
                print("9999.00 \n")
                
                # Write the data to the file
                file.write('9999.00 \n')
                
                # Reset the ding counter
                ding_counter = 0
            else:
                if data_counter == 19:
                    # Take average of the 20 readings taken to remove error
                    value = value / 20
                    value = round(value, 2)
                    
                    # Print the data to the console (optional)
                    print(value)
                    
                    # Write the data to the file
                    file.write(str(value) + '\n')

                    # Increment ding counter
                    ding_counter += 1
                    
                    # Reset the counters
                    value = 0
                    data_counter = 0
                else:
                    value = value + line
                    data_counter += 1

        # Small delay to avoid high CPU usage
        time.sleep(0.1)
