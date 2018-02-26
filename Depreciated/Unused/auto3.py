import cv2
import serial
import numpy as np
import RPi.GPIO as gpio
def empty(z):
    pass
height=120
width=160
cross=width/2
centre=height/2
segment=height/5
minArea=20
maxArea=70
ser = serial.Serial('/dev/ttyS0',9600, timeout=1)
cam = cv2.VideoCapture(0)
if cam.isOpened():
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,120)
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,160)
while (True):
    ret,frame = cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    image_mask=cv2.inRange(hsv,np.array([121,39,98]),np.array([240,255,255]))   
    erode=cv2.erode(image_mask,None,iterations=3)
    moments=cv2.moments(erode,True)
    area=moments['m00']
    # if ball in critical area
    if area>maxArea:
        print("ball within critical area")
        ser.write(chr(int(str(127)))) # motor1 max
	ser.write(chr(int(str(255)))) # motor2 max
    elif moments['m00'] >=minArea:
        x=moments['m10']/moments['m00']
        y=moments['m01']/moments['m00']
        cv2.circle(frame,(int(x),int(y)),5,(0,255,0),-1)
        # if ball on right of camera
        if (x>cross):
                print("ball to the right")
                ser.write(chr(int('127'))) #motor1 max speed forward
		ser.write(chr(int('128'))) #motor2 max speed reverse 
        # if ball on left of camera
        elif (x<cross):
                print("ball to the left")
                ser.write(chr(int('255'))) #motor1 max speed forward
		ser.write(chr(int('1')))   #motor2 max speed reverse
	
                
## USED FOR UP AND DOWN 
        #if (y>centre):
         #      print("y > centre")
        #elif (y<centre):
         #       print("y < centre")

    # if ball out of critical area     
    if (area<minArea ):
        #print("ball out of critical area")
        #ser.write(chr(int('0')))
        #print("STOP")
        
        ser.write(chr(int('224'))) #motor2 1/2 speed forward
	ser.write(chr(int('32'))) #motor2 1/2 speed
        print("SEARCHING")
        
    # if ball in critical area
    #if area>maxArea:
     #   print("ball within critical area")
    # if ball is out of camera view
    if area==0:
        print("ball out of view")
    cv2.imshow('eroded',erode)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==27:
        break
       

cv2.destroyAllWindow()
cam.release()
