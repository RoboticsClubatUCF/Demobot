#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
import numpy as np
import cv2 as cv


def faceCam():
	rospy.init_node('camera', anonymous=True)
	pub = rospy.Publisher('cameraData', Int16, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	cam = cv.VideoCapture(0)

	face_cascade = cv.CascadeClassifier("/opt/ros/kinetic/share/OpenCV-3.3.1-dev/haarcascades/haarcascade_frontalface_alt.xml")

	try:
		while not rospy.is_shutdown():

			ret,img = cam.read()
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

			faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags=cv.CASCADE_SCALE_IMAGE)
		

			numFaces = 0
			for (x, y, w, h) in faces:
				cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
				numFaces += 1
 
			cv.imshow('img',img)
			cv.waitKey(1)

			pub.publish(numFaces)
			rospy.loginfo(numFaces)
			rate.sleep()

	except(KeyboardInterrupt):
		cv.destroyAllWindows()
		cam.release()


if __name__ == '__main__':
    try:
        faceCam()
    except rospy.ROSInterruptException:
        pass


	
