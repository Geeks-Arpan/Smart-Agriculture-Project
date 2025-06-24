from machine import Pin, UART, I2C
import ssd1306
import time

# Initialize I2C for OLED
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
oled_width, oled_height = 128, 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=0x3C)

# UART for Modbus (adjust UART number, TX/RX pins as needed)
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# DE/RE Pins for RS485 direction control (enable sending)
DE = Pin(6, Pin.OUT)
RE = Pin(7, Pin.OUT)

# Enable RS485 transmit
def enable_tx():
    DE.value(1)
    RE.value(1)

# Enable RS485 receive
def enable_rx():
    DE.value(0)
    RE.value(0)

# Send Modbus query
def send_modbus_query(query):
    enable_tx()
    time.sleep(0.01)
    uart.write(query)
    time.sleep(0.01)
    enable_rx()
    time.sleep(0.05)
    response = uart.read()
    return response if response else None

# Extract data from response
def get_value_from_response(response):
    if response and len(response) >= 7:
        return response[4]  # Assuming value is at 5th byte
    return None

# Sample Modbus queries for NPK sensors (replace with actual commands)
n_query = b'\x01\x03\x00\x00\x00\x01\x84\x0A'  # Example for Nitrogen
p_query = b'\x01\x03\x00\x01\x00\x01\xD5\xCA'  # Example for Phosphorus
k_query = b'\x01\x03\x00\x02\x00\x01\x25\xCA'  # Example for Potassium

# Read NPK values
def read_npk_values():
    n_resp = send_modbus_query(n_query)
    time.sleep(0.25)
    p_resp = send_modbus_query(p_query)
    time.sleep(0.25)
    k_resp = send_modbus_query(k_query)
    time.sleep(0.25)

    n = get_value_from_response(n_resp)
    p = get_value_from_response(p_resp)
    k = get_value_from_response(k_resp)

    return n, p, k

# Display values on OLED
def display_npk_oled(n, p, k):
    oled.fill(0)
    oled.text("Soil NPK Values:", 0, 0)
    oled.text(f"N: {n if n is not None else 'Error'} mg/kg", 0, 15)
    oled.text(f"P: {p if p is not None else 'Error'} mg/kg", 0, 30)
    oled.text(f"K: {k if k is not None else 'Error'} mg/kg", 0, 45)
    oled.show()

# Main loop (you can put this in a while loop for continuous reading)
n, p, k = read_npk_values()
display_npk_oled(n, p, k)
