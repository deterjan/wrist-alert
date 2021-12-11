from machine import Pin, I2C, UART, Timer
from ssd1306 import SSD1306_I2C
import time

# SSD1306 oled screen
def setup_oled():
    i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    return oled

def display_oled(oled, msg, x=0, y=0):
    oled.text(msg, x, y)
    oled.show()

def clear_oled(oled):
    oled.fill(0)
    
def display_values(oled, pulse, spo2):
    pulse = "waiting.." if pulse == -1 else pulse
    spo2 = "waiting.." if spo2 == -1 else spo2
    clear_oled(oled)
    display_oled(oled, "Pulse: " + str(pulse))
    display_oled(oled, "SpO2:  " + str(spo2), y=20)

def display_alert(oled):
    display_oled(oled, "ALERT!", y=40)
    
def check_pulse(pulse, oled):
    if pulse != -1 and (pulse < 60 or pulse > 100):
        vibrate(-1)
        display_alert(oled)
        
def check_spo2(spo2, oled):
    if spo2 != -1 and spo2 < 95:
        vibrate(-1)
        display_alert(oled)

def vibrate(sec, stop=0):
    vib1 = Pin(28, Pin.OUT)
    vib2 = Pin(7, Pin.OUT)
    
    def high():
        vib1.high()
        vib2.high()
    
    def low(timer):
        vib1.low()
        vib2.low()
    
    if stop:
        low(None)
        return
    
    high()
    if sec > -1:
        tim = Timer(-1)
        tim.init(period=sec*1000, mode=Timer.ONE_SHOT, callback=low)
    
oled = setup_oled()

# push button
push = Pin(27, Pin.IN, Pin.PULL_DOWN)

# uart
uart = machine.UART(1, baudrate = 9600, rx=Pin(9), tx=Pin(8))

pulse = -1
spo2 = -1

display_oled(oled, "Pulse: Waiting..")
display_oled(oled, "SpO2:  Waiting..", y=20)
while True:
    time.sleep(1)
    
    if push.value():
        vibrate(0, stop=1)
        
    if uart.any():
        bin_data = uart.readline()
        str_data = bin_data.decode()
        print("Received: " + str_data)
        
        if str_data.startswith("p="):
            pulse = int(str_data[2:])
            display_values(oled, pulse, spo2)
            check_pulse(pulse, oled)
        
        if str_data.startswith("s="):
            spo2 = int(str_data[2:])
            display_values(oled, pulse, spo2)
            check_spo2(spo2, oled)
            
    
            

