from nanpy import Servo
import time

#Setup

frHip = Servo(6) #hip
frKnee = Servo(5)#knee
frFoot = Servo(4)#foot

flHip = Servo(3) #hip
flKnee = Servo(2)#knee
flFoot = Servo(13)#foot

brHip = Servo(12) #hip
brKnee = Servo(11)#knee
brFoot = Servo(10)#foot

blHip = Servo(9) #hip
blKnee = Servo(8)#knee
blFoot = Servo(7)#foot


# Zero
time.sleep(1)
print "Zeroing"

frHip.write(100)
frKnee.write(100)   #lower is forward
frFoot.write(90)    #lower is forward

flHip.write(100)
flKnee.write(95)    #lower is back
flFoot.write(80)    #lower is back

brHip.write(100)
brKnee.write(95)    #lower is inward
brFoot.write(95)    #lower is outward

blHip.write(100)
blKnee.write(95)    #lower is outward
blFoot.write(115)   #lower is outward

time.sleep(1)
