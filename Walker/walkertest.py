import RPi.GPIO as GPIO
import time


# SERVO: AR-3600HB Robot Servo
# Example file for servo control

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) # pin 11 used 
GPIO.setup(13, GPIO.OUT) # pin 13 used
GPIO.setup(15, GPIO.OUT) # pin 15 used
GPIO.setup(36, GPIO.OUT) # pin 11 used 
GPIO.setup(38, GPIO.OUT) # pin 13 used
GPIO.setup(40, GPIO.OUT)
GPIO.setwarnings(False) 


# setting pin to pulse-width modulation
# with frequency of 50 hertz
# q, p, and r are servos connected to pins 11, 13, and 15 respectively
p = GPIO.PWM(11, 50)
q = GPIO.PWM(13, 50)
r = GPIO.PWM(15, 50)
s = GPIO.PWM(36, 50)
t = GPIO.PWM(38, 50)
u = GPIO.PWM(40, 50)

p.start(7.5)
q.start(7.5) # sets duty cycle to 7.5
r.start(7.5)
s.start(7.5)
t.start(7.5) # sets duty cycle to 7.5
u.start(7.5)

try:
	while True:
		q.ChangeDutyCycle(7.5)
		p.ChangeDutyCycle(7.5) # Neutral
                r.ChangeDutyCycle(7.5)
                """
                s.ChangeDutyCycle(7.5)
		t.ChangeDutyCycle(7.5) # Neutral
                u.ChangeDutyCycle(7.5)
                """
		time.sleep(1)
		q.ChangeDutyCycle(12.5)
		p.ChangeDutyCycle(12.5) # 180 degrees
                r.ChangeDutyCycle(12.5)
                """
                s.ChangeDutyCycle(12.5)
		t.ChangeDutyCycle(12.5) # Neutral
                u.ChangeDutyCycle(12.5)
                """
		time.sleep(1)
		q.ChangeDutyCycle(2.5)
		p.ChangeDutyCycle(2.5) # 0 degrees
                r.ChangeDutyCycle(2.5)
                """
                s.ChangeDutyCycle(2.5)
		t.ChangeDutyCycle(2.5) # Neutral
                u.ChangeDutyCycle(2.5)
                """
		time.sleep(1)


except KeyboardInterrupt:
	p.stop # stopping pulse-width modulation
	q.stop
	r.stop
	s.stop
	t.stop
	u.stop
	GPIO.cleanup() # resets GPIO pin

