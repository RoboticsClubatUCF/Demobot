#!/usr/bin/env python
import rospy
from std_msgs.msg import String

latitude = ''
longitude = ''

def longitude(longi):
	global longitude
	rospy.loginfo(rospy.get_caller_id() + '   long: %s', longi.data)
	longitude = longi.data

def latitude(lat):
	global latitude
	rospy.loginfo(rospy.get_caller_id() + '   lat: %s', lat.data)
	latitude = lat.data

def gps():
    rospy.init_node('gps', anonymous=False)
    rospy.Subscriber('read_0100', String, latitude)
    rospy.Subscriber('read_0101', String, longitude)

    pub = rospy.Publisher('gpsDir', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():	
        gpsDir = 'Forward'
        rospy.loginfo(gpsDir)
        pub.publish(gpsDir)  

        rate.sleep()

if __name__ == '__main__':
    gps()
