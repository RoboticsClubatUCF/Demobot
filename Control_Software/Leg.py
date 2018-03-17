##################################################################
# DEMOBOT
#
# FILENAME Leg.py
#
# AUTHOR Chris Feltner <chris.feltner@knights.ucf.edu>
#        Joe Peaden <joe.peaden@gmail.com>
#        Harrison Black <harrison.w.black@gmail.com>
#
# BRIEF
#   Leg class; handles coordination of each servo in 
#   the particular leg
#
#
###################################################################

import RPi.GPIO as GPIO
import time
from Servo import Servo

class Leg:

    # constructor
    def __init__(self, name, shoulder_pin, knee_pin, ankle_pin):
        self.name = name
        self.shoulder = Servo(shoulder_pin)
        self.knee = Servo(knee_pin)
        self.ankle = Servo(ankle_pin)

    # step(self)
    # step forward
    def step(self):
        shoulder.setPosition(180)
        knee.setPosition(180)
        ankle.setPosition(180)
        print("Stepping {} forward".format(name))

    # pull(self)
    # pull forward
    def pull(self):
        shoulder.setPosition(90)
        knee.setPosition(90)
        ankle.setPosition(90)
        print("Pulling {} backward".format(name))

    # cleanUp(self)
    # stop all servos in Leg
    def cleanUp(self):
        shoulder.stop
        knee.stop
        ankle.stop

    # calibrate(self)
    # for initial calibration of leg joints using command line
    def calibrate(self):
        s_value = int(raw_input("s_value: "))
        k_value = int(raw_input("k_value: "))
        a_value = int(raw_input("a_value: "))
        self.shoulder.setPosition(s_value)
        self.knee.setPosition(k_value)
        self.ankle.setPosition(a_value)



        
