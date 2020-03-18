#!/usr/bin/env python


import rospy
import struct
import numpy as np

from octomap_msgs.msg import Octomap
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header

def callback(arg):

    print(arg.resolution)




if __name__ == "__main__":

    rospy.init_node("3Dmapreader")
    while not rospy.is_shutdown():
        sub = rospy.Subscriber("/octomap_full",Octomap,callback)
