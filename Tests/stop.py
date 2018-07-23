import serial

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

while(True):
    ser.write(chr(int('0')))