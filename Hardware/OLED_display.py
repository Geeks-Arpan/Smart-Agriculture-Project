from machine import UART, Pin
import time

# Initialize UART with the correct pins and baud rate
uart = UART(1, baudrate=960e, tx=Pin(4), rx=Pin(5))

w Full command example (use the correct command for your sensor)
command =b\x01\x03\x00\x00\x00\x07\x04\x08' # Replace with your sensor's command

print("Sending command:", command)
uart.write(command)

w Wait for a response
time.sleep(1)

# Check for data
if uart.any():
response = uart. read()
  if response:
  print("Sensor connected and responded with data:", response)
  else:
  print("No response from sensor.")
else:
print("Sensor not connected or no response received.")
