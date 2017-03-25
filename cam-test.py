import cv2
from time import sleep

camera_port = 0

ramp_frames = 30

camera = cv2.VideoCapture(camera_port)

def get_image():

	retval, im = camera.read()
	return im

for i in xrange(ramp_frames):
	temp = get_image()
print("Taking image...")

num = 0
for x in range(30):

	camera_capture = get_image()
	file = "/home/wes/Desktop/vid/test_image" + str(num) + ".png"
	cv2.imwrite(file, camera_capture)
	num += 1
	print("SHIT")
	sleep(1/30)

# cv2.imwrite(file, camera_capture)

del(camera)
