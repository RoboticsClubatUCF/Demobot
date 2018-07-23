# Motor serial information:
# MOTOR 1: 1 reverse, 64 stop, 127 forward
# MOTOR 2: 128 reverse, 192 stop, 255 forward

import serial

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

while(True):
    ser.write(chr(int('127')))# Right Motor
    ser.write(chr(int('255')))# Left Motor