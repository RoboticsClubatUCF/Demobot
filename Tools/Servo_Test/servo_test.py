##################################################################
# DEMOBOT
#
# FILENAME servo_test.py
# 
# AUTHOR Chris Feltner <chris.feltner@knights.ucf.edu>
#
# BRIEF
#   This script is designed to test individual servos by entering
#   a pin number and rotation amount.
#
#
###################################################################
import RPi.GPIO as GPIO
import time

def setupGPIOandPWM(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    servo = GPIO.PWM(pin, 50)
    servo.start(7.5)
    return servo

def main():
    print('Enter pin number: ')
    pin_number = int(input())
    servo = setupGPIOandPWM(pin_number)
    print('Enter servo duty cycle: ')
    duty_cycle = float(input())
    servo.ChangeDutyCycle(duty_cycle)
    servo.stop
    GPIO.cleanup()

if __name__ == '__main__':
    main()
