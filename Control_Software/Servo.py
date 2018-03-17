##################################################################
# DEMOBOT
#
# FILENAME Servo.py
#
# AUTHOR Chris Feltner <chris.feltner@knights.ucf.edu>
#        Joe Peaden <joe.peaden@gmail.com>
#
# BRIEF
#   Servo class to abstract and encapsulate low-level servo setup.
#
#
###################################################################

import RPi.GPIO as GPIO

class Servo:
    # Constructor
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(7.5)

    # setPosition(self, position)
    # position - servo position in degrees
    # sets the position of the servo
    def setPosition(self, position):
        # change position in degrees to duty cycle
        # SERVO controls:
        # 7.5 neutral, 2.5 is zero, 12.5 is 180
        dutyCycle = (position/180)*10 + 2.5
        self.servo.ChangeDutyCycle(dutyCycle)
        

    # stop(self)
    # stops servo
    def stop(self):
        self.servo.stop
