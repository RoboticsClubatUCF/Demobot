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

# SERVO controls:
# 7.5 neutral, 2.5 is zero, 12.5 is 180

# Leg class for grouping servos and making things easier
class Leg():

    def __init__(self, name, hs_servo_pin, vs_servo_pin, k_servo_pin, adj_leg):
        # hs for horizontal shoulder
        # vs for vertical shoulder
        # adj_leg is the adjacent leg
        # k for knee joint
        self.name = name

        horizontalShoulder = Servo(hs_servo_pin)
        verticalShoulder = Servo(vs_servo_pin)
        knee = Servo(k_servo_pin)
        

        #self.k_servo = GPIO.PWM(k_servo_pin, 50)
        #k_servo.start(7.5)

        #self.adj_leg = adj_leg

    def step(self):
        verticalShoulder.setPosition(180)
        horizontalShoulder.setPosition(180)
        print("Stepping {} forward".format(name))

    def pull(self):
        verticalShoulder.setPosition(90)
        horizontalShoulder.setPosition(90)
        print("Pulling {} backward".format(name))

    def cleanUp():
        horizontalShoulder.stop
        verticalShoulder.stop
        knee.stop
