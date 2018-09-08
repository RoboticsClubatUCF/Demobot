#!/usr/bin/env python
import rospy
from std_msgs.msg import String

ultraForward = ''
ultraLeft = ''
ultraRight = ''
ultraBack = ''

def distanceForward(ultF):
	global ultraForward
	rospy.loginfo(rospy.get_caller_id() + '   UltraF: %s', ultF.data)
	ultraForward = int(ultF.data)

def distanceLeft(ultL):
	global ultraLeft
	rospy.loginfo(rospy.get_caller_id() + '   UltraL: %s', ultL.data)
	ultraLeft = int(ultL.data)

def distanceRight(ultR):
	global ultraRight
	rospy.loginfo(rospy.get_caller_id() + '   UltraR: %s', ultR.data)
	ultraRight = int(ultR.data)

def distanceBack(ultB):
	global ultraBack
	rospy.loginfo(rospy.get_caller_id() + '   UltraB: %s', ultB.data)
	ultraBack = int(ultB.data)

def ultra():
    rospy.init_node('ultra', anonymous=False)
    rospy.Subscriber('read_0000', String, distanceForward)
    rospy.Subscriber('read_0001', String, distanceLeft)
    rospy.Subscriber('read_0010', String, distanceRight)
    rospy.Subscriber('read_0011', String, distanceBack)

    pub = rospy.Publisher('objAvoid', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():	
        if (ultraForward > 50 and ultraLeft > 50 and ultraRight > 50):
            avoid = 'Forward'
            rospy.loginfo(avoid)
            pub.publish(avoid)   

        elif (ultraLeft < 50):
            avoid = 'Right'
            rospy.loginfo(avoid)
            pub.publish(avoid)

        elif (ultraRight < 50):
            avoid = 'Left'
            rospy.loginfo(avoid)
            pub.publish(avoid)

        rate.sleep()

if __name__ == '__main__':
    ultra()
