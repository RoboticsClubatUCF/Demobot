import urllib2
import serial
from time import sleep
import math

def setup():
	global ser
	ser = serial.Serial('/dev/ttyAMA0',9600, timeout=1) #establish serial connection

	if(check_connect()):
		print('INTERNET CONNECTED')
	else:
		print('INTERNET NOT CONNECTED')	

	ser.write(chr(int(0)))


def check_connect():  #checking for internet connection


	try:
		urllib2.urlopen('http://216.58.192.142', timeout=1)
		return True
	except urllib2.URLError as err:
		return False

	return False	


def turn_right(time): #where time is in seconds
	
	global turning
	turning = True
	x = 0
	while(turning):
		ser.write(chr(int('100'))) #motor1 1/2 speed forward (91)
		ser.write(chr(int('155'))) #motor2 1/2 speed reverse  (160)
		if(x > time):
			turning = False
		x += 1	
		sleep(1)

	ser.write(chr(int('0'))) # shuts down motors	
	return	

def turn_left(time):
	
	turning = True	
	x = 0
	while(turning):
		ser.write(chr(int('224'))) #motor2 1/2 speed forward
		ser.write(chr(int('32'))) #motor2 1/2 speed reverse
		if(x > time):
			turning = False
		x += 1	
		sleep(1)

	ser.write(chr(int('0'))) # shuts down motors	
	return	

def forward(speed, time): #takes value in range 1-64

	x = 0
	while(x < time):
		ser.write(chr(int(str(speed+64)))) #motor1 speed, variable
		ser.write(chr(int(str(speed +192 ))))
		x+=1
		sleep(1)

	ser.write(chr(int('0')))
	return		


setup()
turn_right(6)

