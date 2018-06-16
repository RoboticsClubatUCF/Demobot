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


time.sleep(2)
print "Zeroing"



  #F +80                  #F -90
  #K +95                  #K -100
#Front left             #Front Right
  #K -95                  #K +100
  #F -80                  #F +90




  #F +115                 #F -95
  #K +95                  #K -95
#Back left              #Back Right
  #K -95                  #K +95
  #F -115                 #F +95






#your going to have to move one 
#leg at a time, but then have 
#them act directly after one another, 
#almost no delay
#https://youtu.be/Hzt18V3Uaxc







def F_leftForward():

    flFoot.write(55)    #80     --25
    time.sleep(1)
    flKnee.write(135)   #95     --40
    

def F_leftBackward():

    flKnee.write(80)    #95     --15
    flFoot.write(95)    #80     --15
  
def F_rightForward():

    frKnee.write(60)    #100
    frFoot.write(115)   #90
  
def F_rightBackward():

    frKnee.write(115)   #100
    frFoot.write(75)    #90



def B_leftForward():

    blKnee.write(135)   #95
    blFoot.write(90)   #115
  
def B_leftBackward():

    blKnee.write(80)    #95
    blFoot.write(130)   #115
  
def B_rightForward():

    brKnee.write(55)    #95
    brFoot.write(120)   #95
  
def B_rightBackward():

    brKnee.write(110)   #95     previously at 110
    brFoot.write(110)   #95





def straightenALL():
  
  flHip.write(100)  
  flKnee.write(95)  #lower is back
  flFoot.write(80)  #lower is back
  
  frHip.write(100)
  frKnee.write(100) #lower is forward
  frFoot.write(90)  #lower is forward
  
  blHip.write(100)
  blKnee.write(95)  #lower is outward
  blFoot.write(115) #lower is outward
  
  brHip.write(100)
  brKnee.write(95)  #lower is inward
  brFoot.write(95)  #lower is outward



straightenALL()

time.sleep(3)
F_leftForward()
##while(True):
##
##    F_leftForward()
##    B_rightForward()
##    time.sleep(0.8)
##    
##    F_leftBackward()
##    F_rightForward()
##    B_leftForward()
##    B_rightBackward()
##    time.sleep(0.8)
##    
##    F_leftForward()
##    F_rightBackward()
##    B_leftBackward()
##    B_rightForward()


time.sleep(3)
straightenALL()
