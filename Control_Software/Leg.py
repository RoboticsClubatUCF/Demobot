##################################################################
# DEMOBOT
#
# FILENAME Servo.py
#
# AUTHOR Chris Feltner <chris.feltner@knights.ucf.edu>
#        Joe Peaden <joe.peaden@gmail.com>
#
# BRIEF
#   Leg class
#
#
###################################################################

import RPi.GPIO as GPIO
import time

class Leg:

    def __init__(self, name, hs_servo_pin, vs_servo_pin, k_servo_pin):
        # hs for horizontal shoulder
        # vs for vertical shoulder
        # adj_leg is the adjacent leg
        # k for knee joint
        self.name = name

        horizontalShoulder = Servo(hs_servo_pin)
        verticalShoulder = Servo(vs_servo_pin)
        knee = Servo(k_servo_pin)

    # step(self)
    # step forward
    def step(self):
        verticalShoulder.setPosition(180)
        horizontalShoulder.setPosition(180)
        print("Stepping {} forward".format(name))

    # pull(self)
    # pull forward
    def pull(self):
        verticalShoulder.setPosition(90)
        horizontalShoulder.setPosition(90)
        print("Pulling {} backward".format(name))

    # cleanUp(self)
    # stop all servos in Leg
    def cleanUp(self):
        horizontalShoulder.stop
        verticalShoulder.stop
        knee.stop
