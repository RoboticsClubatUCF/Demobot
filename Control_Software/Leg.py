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

        GPIO.setup(hs_servo_pin, GPIO.OUT)
        GPIO.setup(vs_servo_pin, GPIO.OUT)
        GPIO.setup(k_servo_pin, GPIO.OUT)
        
        self.hs_servo = GPIO.PWM(hs_servo_pin, 50)
        hs_servo.start(7.5)
        self.vs_servo = GPIO.PWM(vs_servo_pin, 50)
        vs_servo.start(7.5)
        #self.k_servo = GPIO.PWM(k_servo_pin, 50)
        #k_servo.start(7.5)

        #self.adj_leg = adj_leg

    def step(self):
        vs_servo.ChangeDutyCycle(12.5)
        hs_servo.ChangeDutyCycle(12.5)
        print("Stepping {} forward".format(name))

    def pull(self):
        vs_servo.ChangeDutyCycle(7.5)
        hs_servo.ChangeDutyCycle(7.5)
        print("Pulling {} backward".format(name))

    def cleanUp():
        hs_servo.stop
        vs_servo.stop
        k_servo.stop
