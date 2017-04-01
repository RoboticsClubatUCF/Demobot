import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('ballshit.jpeg',1)
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


