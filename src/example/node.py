#! /usr/bin/python

import rospy

def test_function():
    rospy.init_node("node")
    rate = rospy.Rate(1)
    for i in range(0,100):
        print("What's up")
    rate.sleep()
    rospy.signal_shutdown("Finished")
    

if __name__ == '__main__':
    test_function()