#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial

direction = ''

def motor(di):
	global direction
	rospy.loginfo(rospy.get_caller_id() + '   Direction: %s', di.data)
	direction = di.data

def motor():
    rospy.init_node('motor', anonymous=False)
    rospy.Subscriber('direction', String, motor)

    serM = serial.Serial('/dev/ttySAC0', 9600, timeout=1)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():	

        rate.sleep()

if __name__ == '__main__':
    motor()
