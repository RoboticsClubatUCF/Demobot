import cv2
import imutils
import numpy as np
from collections import deque

class VideoCamera(object):


	def __init__(self):
		# Using OpenCV to capture from device 0. If you have trouble capturing
		# from a webcam, comment the line below out and use a video file
		# instead.
		self.video = cv2.VideoCapture(0)
                self.video.set(4,240)
		self.video.set(3,320)
		# If you decide to use video.mp4, you must have this file in the folder
		# as the main.py.
		# self.video = cv2.VideoCapture('video.mp4')

		# define the lower and upper boundaries of the "green"
        # ball in the HSV color space, then initialize the
        # list of tracked points
        self.yellowUpper = (30,135,255)
        self.yellowLower = (25,102,109)
        self.pinkLower = (121,39,98)
        self.pinkUpper = (240,255,255)
        self.pts = deque(maxlen=64)
    
	def __del__(self):
		self.video.release()
    
	def get_frame(self):
		success, frame = self.video.read()
		#frame = imutils.rotate_bound(frame, 180)
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		# resize the frame, blur it, and convert it to the HSV
		# color space
		#frame = imutils.resize(frame, width=500)
		# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, self.pinkLower, self.pinkUpper)
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
		self.pts.appendleft(center)

		# loop over the set of tracked points
		for i in xrange(1, len(self.pts)):
			# if either of the tracked points are None, ignore
			# them
			if self.pts[i - 1] is None or self.pts[i] is None:
				continue

			# otherwise, compute the thickness of the line and
			# draw the connecting lines
			thickness = int(np.sqrt(64 / float(i + 1)) * 2.5)
			cv2.line(frame, self.pts[i - 1], self.pts[i], (0, 0, 255), thickness)

		ret, jpeg = cv2.imencode('.jpg', frame)
		return jpeg.tostring()


	def get_circle_frame(self):

		success, frame = self.video.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT)

		if circles != None:

			circles = np.round(circles[0, :]).astype("int")

			for (x, y, r) in circles:
				cv2.circle(frame, (x,y), r, (0,255,0),4)
				cv2.rectangle(frame, (x-5, y-5), (x+5, y+5), (0,128,255), -1)

		ret, jpeg = cv2.imencode('.jpg', frame)
		return jpeg.tostring()		

				

		