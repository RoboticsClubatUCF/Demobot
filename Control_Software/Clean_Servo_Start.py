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

    flKnee.write(125)   #95     --30
    flFoot.write(75)    #80     --25

def F_rightForward():

    frKnee.write(70)    #100
    frFoot.write(95)   #90

def B_leftForward():

    blKnee.write(125)   #95
    blFoot.write(110)   #115

def B_rightForward():

    brKnee.write(65)    #95
    brFoot.write(100)   #95
  

  




def F_leftBackward():

    flKnee.write(80)    #95     --20
    flFoot.write(65)    #80     --15

def F_rightBackward():

    frKnee.write(115)   #100
    frFoot.write(100)    #90
  
def B_leftBackward():

    blKnee.write(80)    #95
    blFoot.write(105)   #115
  
def B_rightBackward():

    brKnee.write(110)   #95     previously at 110
    brFoot.write(105)   #95





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
i = 0
time.sleep(3)

F_leftForward()
B_rightForward()
time.sleep(1)
while(i < 5):
    
    F_leftBackward()
    F_rightForward()
    B_leftForward()
    B_rightBackward()
    time.sleep(1)
    
    F_leftForward()
    F_rightBackward()
    B_leftBackward()
    B_rightForward()
    time.sleep(1)

    i+=1


time.sleep(3)
straightenALL()
