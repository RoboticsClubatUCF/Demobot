import RPi.GPIO as GPIO
import time
import serial
import numpy as np

# WALKERBOT

# Sample motor code
#ser.write(chr(int('255'))) #motor2 max forward
#ser.write(chr(int('1')))   #motor1 max reverse

# serial setup for motors
#ser = serial.Serial('/dev/tty0',9600, timeout=1)

# GPIO pins that servos are connected to:
# 11, 13, 15, 40, 38, 36
# SERVO controls:
# 7.5 neutral, 2.5 is zero, 12.5 is 180

##### Servo setup #####
# For AR-3600HB Robot Servo
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#GPIO.setup(7, GPIO.OUT) # pin 11 used 
GPIO.setup(11, GPIO.OUT) # pin 15 used
GPIO.setup(13, GPIO.OUT)
##### PWM setup #####
#s11 = GPIO.PWM(7, 50) # setting pin to pulse-width modulation with frequency of 50 hertz 
s13 = GPIO.PWM(11, 50)
s15 = GPIO.PWM(13, 50)

while(True):
 #   print("7s15.start(7.5) # shoulder neutral 7.5
#    s11.start(7.5) # mid neutral 7.3
    s13.start(6.5) # bot neutral 7.7
    #s15.start(6.5) # shoulder neutral 7.5
    time.sleep(1)
    s13.start(7.5) # bot neutral 7.7
    #s15.start(7.5) # shoulder neutral 7.5
    time.sleep(1)
    s13.start(8.5) # bot neutral 7.7
    #s15.start(8.5) # shoulder neutral 7.5
    time.sleep(1)

     #print("Motor!")
     #ser.write(chr(int('60'))) #some shit
#    time.sleep(1)

s11.stop # stopping PWM
s13.stop
s15.stop

GPIO.cleanup() # resets GPIO pin


