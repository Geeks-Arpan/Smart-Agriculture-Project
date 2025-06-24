from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import utime

# Initialize I2C and OLED display
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000) # Adjust pins if necessary
oled = SSD1306_I2C(128, 64, i2c)
# 128x64 OLED display

# Initialize onboard LED and ADC for moisture sensor
led_onboard = Pin(25, Pin.OUT)
adc = ADC(26) # Moisture sensor connected to ADC pin 26
conversion_factor = 100 / 65535 # Convert ADC reading to percentage

while True:
# Read and calculate moisture level
moisture = 100 - (adc.read_u16() * conversion_factor)
print("Moi:", round(moisture, 3), "%", utime. localtime())

# Clear OLED display and show moisture level
oled.fill(0) # Clear the screen
oled.text("Moi: { :. 3f}%".format(moisture), 0, 0) # Display moisture level
oled.show()

# Control LED based on moisture level
if moisture >= 70:
led_onboard.value(0) # Turn off LED if moisture is sufficient
utime.sleep(1) # Delay for 30 seconds
else:
led_onboard. toggle() # Toggle LED for low moisture alert
# Blink LED every 500 ms

utime.sleep_ms(0.05)
