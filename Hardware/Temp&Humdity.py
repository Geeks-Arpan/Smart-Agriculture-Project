from machine import Pin, I2C
import ssd1306
import utime as time
from dht import DHT11

# Initialize 12C for OLED
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)

# Define OLED width and height
oled_width = 128
oled_height = 64

# Initialize the OLED display
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=@x3C)

# Initialize the DHT11 sensor
pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
try:
# Trigger measurement
sensor.measure()

# Handle temperature and humidity as callable or property
try:
t = sensor.temperature() # Callable method
h = sensor.humidity()
except TypeError:
t = sensor.temperature # Property
h = sensor.humidity

# Print to console
print("Temperature: {]℃".format(t))
print("Humidity: {]%".format(h))
print("\n")

# Display on OLED
oled.fill(0) # Clear the screen
oled.text("Temp & Humi Sens", 0, 0)
oled.text("Temp: {} C".format(t), 0, 20)
oled.text("Humi: {} %".format(h), 0, 30)
oled.show()

except Exception as e:
print("Error reading DHT11:", e)
oled.fill(0)
oled.text("Sensor Error", 0, 10)
oled.show()

time.sleep(3) # Wait 3 seconds before the next reading

