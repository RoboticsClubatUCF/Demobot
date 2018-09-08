#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16

avoid = ''
camData = 0
gps_dir = ''

def avoid(av):
	global ultraRight
	rospy.loginfo(rospy.get_caller_id() + '   Avoid: %s', av.data)
	avoid = av.data

def gps(g):
	global ultraBack
	rospy.loginfo(rospy.get_caller_id() + '   GPS: %s', g.data)
	gps_dir = g.data

def cv(cam):
	global camData
	rospy.loginfo(rospy.get_caller_id() + '   Cam: %d', cam.data)
	camData = cam.data

def priority():
    rospy.init_node('priority', anonymous=False)
    rospy.Subscriber('objAvoid', String, avoid)
    rospy.Subscriber('gpsDir', String, gps)
    rospy.Subscriber('cameraData', Int16, cv)

    pub = rospy.Publisher('direction', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():	
        direc = 'Forward'
        rospy.loginfo(direc)
        pub.publish(direc)  

        rate.sleep()

if __name__ == '__main__':
    priority()
