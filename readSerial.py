#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial

def read_serial():
    rospy.init_node('Arduino', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    serU = serial.Serial('/dev/ttyACM0', 9600)

    while not rospy.is_shutdown():
        if serU.in_waiting > 0:
            data = serU.readline()

            port = data[0:4].strip('\r\n')
            data = data[5:].strip('\r\n')

            pub = rospy.Publisher('read_' + port, String, queue_size=10)
            rospy.loginfo(data)
            pub.publish(data)
            rate.sleep()

if __name__ == '__main__':
    try:
        read_serial()
    except rospy.ROSInterruptException:
        pass
