import RPi.GPIO as GPIO           # import RPi.GPIO module  
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  

PIN = 12
GPIO.setup(PIN, GPIO.OUT) # set a port/pin as an output   
GPIO.output(PIN, 1)       # set port/pin value to 1/GPIO.HIGH/True  
# GPIO.output(port_or_pin, 0)       # set port/pin value to 0/GPIO.LOW/False  

import time
time.sleep(5)    