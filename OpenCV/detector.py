from shapedetector import ShapeDetector
import imutils
import cv2

''' FUNCTION: this file can be used to detect simple polygons (triangle, squares, rectangles) as well as circles
	      also makes use of adaptive thresholding, which mitigates the issues with lighting (somewhat)
    MAKES USE OF : class ShapeDetector from file shapedetector.py
'''    


camera = cv2.VideoCapture(0)
camera.set(4, 240)
camera.set(3, 320)

while True:

	(grabbed, image) = camera.read() #pull video from cv camera
	resized = imutils.resize(image, width=320)
	
	ratio = image.shape[0] / float(resized.shape[0])

	#image processing
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5,5), 0)
	thresh = cv2.adaptiveThreshold(blurred,175, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) #adaptive thresholding http://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html

	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	sd = ShapeDetector()

	for c in cnts:

		M = cv2.moments(c)
		if M["m00"] != 0:
			cX = int((M["m10"] / M["m00"]) * ratio)
			cY = int((M["m01"] / M["m00"]) * ratio)
		else:
			cX, cY = 0,0	

		shape = sd.detect(c)

		c = c.astype("int")
		cv2.drawContours(image, [c], -1, (0,255,0), 1)
		cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 2)

	cv2.imshow("Image", image)
	cv2.waitKey(1)	

camera.release()
cv2.destroyAllWindows()		

