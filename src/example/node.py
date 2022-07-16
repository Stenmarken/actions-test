#! /usr/bin/python

import rospy

def test_function():
    rospy.init_node("node")
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            print("What's up")
            rate.sleep()
        except rospy.ServiceException as e:
            print("Something went wrong %s", e)

if __name__ == '__main__':
    test_function()