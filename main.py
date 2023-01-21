#IMPORT RELATED LIBRARY
from machine import Pin, I2C
from button import PushButton
import time
import utime

#CONSTANT

#GLOBAL VAR
ledTick = 0
buttonTick = 0
buttonState = ""

#USER DEFINE CLASS

#USER DEFINE FUNCTION
start_time = time.ticks_ms()
def millis():
    return time.ticks_ms() - start_time

print('Version: Read Push Button and Blink LED independance')

#SETUP SECTION
led = Pin(2, Pin.OUT)
gButton = PushButton (5)

#LOOP SECTION
while True:
    buttonState = gButton.read_button()
    
    if millis() >= ledTick:
        ledTick = millis()+1000
        led.value(not led.value())

    if buttonState == "FALLING":
        print("Button pressed")       
        timestamp = utime.time()
        time_tuple = utime.localtime(timestamp)
        time_string = "{}-{:02d}-{:02d} {}:{:02d}:{:02d}".format(time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5])
        print(time_string)
       