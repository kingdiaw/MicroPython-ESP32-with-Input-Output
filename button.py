'''
This code defines a class PushButton which contains the logic for
reading the button state and debouncing. The class has a
constructor __init__(self, pin_number, debounce_time=50) that
takes a pin_number and an optional debounce_time as arguments.
The class also has a method read_button(self, edge_type = "RISING")
that takes an optional edge_type as an argument.

The class uses the machine module to access the pin, set it as an input,
and then returns the state of the button based on the edge type.
It uses the time.sleep_ms() function to introduce a delay of
debounce_time milliseconds between reading the button state.

You can create an object of the class and call the read_button() method
on it to read the button state.
You can also change the pin_number and debounce_time passed to the
constructor and edge_type passed to the method to suit your requirements.

if the state is "FALLING", it will print "Button pressed"

Note: The code uses the time.sleep_ms() function which is only available
on MicroPython. If you are using Python, you should use time.sleep()
instead and pass in the delay in seconds.
'''

import machine
import time

class PushButton:
    def __init__(self, pin_number, debounce_time = 50):
        self.pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_UP)
        self.debounce_time = debounce_time
        self.last_state = self.pin.value()
        
    def read_button(self):    
        current_state = self.pin.value()
        if current_state != self.last_state:
            self.last_state = current_state
            if current_state == 0:
                time.sleep_ms(self.debounce_time)
                if self.pin.value() == 0:
                    return "FALLING"
            else:
                time.sleep_ms(self.debounce_time)
                if self.pin.value() == 1:
                    return "RISING"
        elif current_state == 0:
            return "LOW"
        else:
            return "HIGH"