import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
from leg import Leg

# TEST

##### Servo setup #####
# For AR-3600HB Robot Servo
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

##### LEG setup #####
# Note: parameter list is: Leg(Name, horizontalShoulderServo, verticalShoulderServo, Adjacent Leg)
# only numbers for pins, servo setup happens in the Leg class.
frontRightLeg = Leg("Front Right Leg", 11, 13, None)

height = 120
width = 160
# third and twothird separate screen into 3 sections
third = width/3
twothird = third + third
minArea = 1 # minimum area to track object
criticalArea = 13000 # area to close claws (may be too large)
move = 0 # move legs
## TIMER VARIABLES ###
cTime = 0 # current time
pTime = 0 # previous time
timeDiff = 0 # time difference since last loop
Timer = .25 #.25 # time to wait


##### Camera/serial setup #####

cam = cv2.VideoCapture(0)
if cam.isOpened():
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,120) # Setting camera height and width
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,160) # in order to work with variables

try:
    while (True):
    ##### Setting up image tracking #####
    # big ball (pink): min: (121, 39, 98), max: (240, 255, 255)

        ret,frame = cam.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        image_mask=cv2.inRange(hsv,np.array([121,39,98]),np.array([240,255,255]))   
        erode=cv2.erode(image_mask,None,iterations=3)
        moments=cv2.moments(erode,True)
        area=moments['m00']
    
    ##### Movement decision making #####

        ## Timer ##
        pTime = cTime
        cTime = time.clock()
        timeDiff = cTime - pTime
        Timer -= timeDiff

        if moments['m00'] >=minArea:
            x=moments['m10']/moments['m00']
            y=moments['m01']/moments['m00']
            cv2.circle(frame,(int(x),int(y)),5,(0,255,0),-1)
    
            if (x>twothird):
                if(Timer < 0): # Wait until Timer runs out, then take action
                    if(move == 1):
                        move = frontRightLeg.step() # 180 degree
                    elif(move == 0):
                        move = frontRightLeg.pull() # 180 degree
                    Timer = .25 # resetting timer
    
        # showing camera frames on desktop
        cv2.imshow('eroded',erode)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==27:
            break

except(KeyboardInterrupt):
##### Cleanup #####
    frontRightLeg.cleanUp()
    gpio.cleanup() # resets GPIO pin
    cv2.destroyAllWindow()
    scam.release()
