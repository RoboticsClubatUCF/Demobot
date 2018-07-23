import serial

serU = serial.Serial('/dev/ttyACM0', 9600)

serM = serial.Serial('/dev/ttyS0', 9600, timeout=1)

while True:
    if serU.in_waiting > 0:
        distance = serU.readline()
        print distance
        
        if int(distance) < 50:
            print "Object!!!" 
            serM.write(chr(int('0'))) #stop
    
        else:
            print "No Object In Front of Vehicle"
            serM.write(chr(int('127'))) 
            serM.write(chr(int('255')))
            
    
    