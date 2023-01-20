from machine import Pin, I2C
import machine
from button import PushButton
import time
import utime

#Global Variable
ledTick = 0
buttonTick = 0

start_time = time.ticks_ms()

# class PushButton:
#     def __init__(self, pin_number, debounce_time = 50):
#         self.pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_UP)
#         self.debounce_time = debounce_time
#         self.last_state = self.pin.value()
#         
#     def read_button(self):    
#         current_state = self.pin.value()
#         if current_state != self.last_state:
#             self.last_state = current_state
#             if current_state == 0:
#                 time.sleep_ms(self.debounce_time)
#                 if self.pin.value() == 0:
#                     return "FALLING"
#             else:
#                 time.sleep_ms(self.debounce_time)
#                 if self.pin.value() == 1:
#                     return "RISING"

def millis():
    return time.ticks_ms() - start_time


print('Version: Read Push Button and Blink LED independance')

#setup Digital O/p
led = Pin(2, Pin.OUT)

gButton = PushButton (5)
button_state = ""
while True:
    button_state = gButton.read_button()
    
    if millis() >= ledTick:
        ledTick = millis()+1000
        led.value(not led.value())

    if button_state == "FALLING":
        print("Button pressed")       
        timestamp = utime.time()
        time_tuple = utime.localtime(timestamp)
        time_string = "{}-{:02d}-{:02d} {}:{}:{}".format(time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5])
        print(time_string)
       