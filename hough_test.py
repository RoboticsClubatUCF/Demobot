import imutils
import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])	
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (11,11),0)
gray = cv2.erode(gray, None, iterations=2)
gray = cv2.dilate(gray, None, iterations=2)

circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)

if circles != None:
	circles = np.round(circles[0, :]).astype("int")

	for (x, y, r) in circles:

		cv2.circle(output, (x,y), r, (0,255,0),4)
		cv2.rectangle(output, (x-5, y-5), (x+5, y+5), (0,128,255), -1)


	cv2.imshow("output", np.hstack([image, output]))
	cv2.waitKey(0)
