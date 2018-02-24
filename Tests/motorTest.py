import serial as serial
import RPi.GPIO as gpio
import time

ser = serial.Serial('/dev/ttyS0', 
		    baudrate=9600,
 		    parity=serial.PARITY_NONE,
		    stopbits=serial.STOPBITS_ONE,
		    bytesize=serial.EIGHTBITS,

	            timeout=1)

#while(True):
 #  ser.write('200')
#   time.sleep(1)
#   ser.write('0')
#   time.sleep(1)

#if KeyBoardInterrupt:
while(True):
	try:
		ser.write(chr(int('0')))
		time.sleep(1)
		ser.write(chr(int('100')))
		time.sleep(1)
	except(KeyboardInterrupt):
		ser.write(chr(int('0')))
