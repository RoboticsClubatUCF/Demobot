import urllib2
import serial
from time import sleep
import math
from collections import deque
import numpy as np
import argparse
import imutils
import cv2


#######################
#### OPEN CV SETUP ####
#######################


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
#greenLower = (29, 86, 6)
#greenUpper = (64, 255, 255)
# yellowLower = (20,64,117)
#yellowUpper = (41,173,255)
#yellowLower = (23,97,116)
# yellowLower = (19, 98,198) WOrkING FOR OTHER BALL
# yellowUpper = (255, 255, 255)
pinkUpper = (240,255,255)
pinkLower = (121,39,98)
pts = deque(maxlen=args["buffer"])

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0)
	camera.set(4, 240)
	camera.set(3, 320)
# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])


# ball tracking function
# Idea: in this function, while ball is not within critical area, 
#       continue to rotate. Need to find x & y coordinates

def track():
	while True:
		# grab the current frame
		(grabbed, frame) = camera.read()

		# if we are viewing a video and we did not grab a frame,
		# then we have reached the end of the video
		if args.get("video") and not grabbed:
			break
		
		# resize the frame, blur it, and convert it to the HSV
		# color space
		frame = imutils.resize(frame, width=500)
		# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, pinkLower, pinkUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		# find contours in the mask and initialize the current
		# (x, y) center of the ball
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)[-2]
		center = None

		# only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			# only proceed if the radius meets a minimum size
			if radius > 10:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv2.circle(frame, (int(x), int(y)), int(radius),
					(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)

		# update the points queue
		pts.appendleft(center)

		# loop over the set of tracked points
		for i in xrange(1, len(pts)):
			# if either of the tracked points are None, ignore
			# them
			if pts[i - 1] is None or pts[i] is None:
				continue

			# otherwise, compute the thickness of the line and
			# draw the connecting lines
			thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
			cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
			# print(pts)
			# point = (250, )
			# cv2.circle(frame, point, 2, (255,255,255), thickness=1,lineType=8,shift=0)

		checkRange(pts)	# uses our check range function to attempt to center the bot  
		# show the frame to our screen
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the 'q' key is pressed, stop the loop
		if key == ord("q"):
			break

# VERY VERY UNTESTED 4/15/17			
def checkRange(pts):
		
	center = 250	
	xRange = 50
	yRange = 50

	for i in xrange(1, len(pts)):

		if(pts[i] is not None):
			
			if(pts[i][0] > (center + xRange)):
				step_right()
			if(pts[i][0] < (center - xRange)):
				step_left()





#############################
#### MOTOR CONTROL SETUP ####
#############################


def setup():

	global ser
	ser = serial.Serial('/dev/ttyS0',9600, timeout=1) #establish serial connection

	if(check_connect()):
		print('INTERNET CONNECTED')
	else:
		print('INTERNET NOT CONNECTED')

	ser.write(chr(int(0)))
	print("WRITTEN")

def check_connect():  #checking for internet connection


	try:
		urllib2.urlopen('http://216.58.192.142', timeout=1)
		return True
	except urllib2.URLError as err:
		return False

	return False	

#UNTESTED 4/15/17
def step_right(): #a turn that rotates the bot a set distance, rather than for a set time

	stepTime = 5 #how long the turn takes, different depending on "size" of step
	global turning = True
	x=0
	while(turning):

		ser.write(chr(int('100'))) #motor1 1/2 speed forward (91)
		ser.write(chr(int('155'))) #motor2 1/2 speed reverse  (160)

		if(x > stepTime):
			turning = False
		x +=1
		sleep(1)
	ser.write(chr(int('0'))) # shuts down motors		
	return

#UNTESTED 4/15/17
def step_left(): #a turn that rotates the bot a set distance, rather than for a set time

	stepTime = 5 #how long the turn takes, different depending on "size" of step
	global turning = True
	x=0
	while(turning):

		ser.write(chr(int('224'))) #motor2 1/2 speed forward
		ser.write(chr(int('32'))) #motor2 1/2 speed reverse
		
		if(x > stepTime):
			turning = False
		x +=1
		sleep(1)
	ser.write(chr(int('0'))) # shuts down motors		
	return	


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

def search(time): # for finding ball, then stops if ball is found

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

    
######################
#### MAIN SECTION ####
######################


#setup()
track()
camera.release()
cv2.destroyAllWindows()

