#!/usr/bin/env python
# PointCloud2 color cube
# https://answers.ros.org/question/289576/understanding-the-bytes-in-a-pcl2-message/
import rospy
import struct


from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header


def callback(arg):

    laser = LaserScan()


    if len(laser.ranges) < 200 :
        for i in range(len(arg.ranges)):
            sub = rospy.Subscriber("/desistek_saga/sonar", LaserScan, queue_size = 1)
            laser.header = arg.header            # timestamp in the header is the acquisition time on
            laser.angle_min = arg.angle_min        # start angle of the scan [rad]
            laser.angle_max = arg.angle_max        # end angle of the scan [rad]
            laser.angle_increment = arg.angle_increment  # angular distance between measurements [rad]
            laser.time_increment = arg.time_increment   # time between measurements [seconds] - if your scanne
            laser.scan_time = arg.scan_time        # time between scans [seconds]
            laser.range_min = arg.range_min        # minimum range value [m]
            laser.range_max = arg.range_max        # maximum range value [m]

            laser.ranges.append(arg.ranges[i])
            rospy.sleep(0.25)
            pub.publish(laser)

    else:
        for i in range(len(arg.ranges)):
            sub = rospy.Subscriber("/desistek_saga/sonar", LaserScan, queue_size = 1)
            laser.header = arg.header            # timestamp in the header is the acquisition time on
            laser.angle_min = arg.angle_min        # start angle of the scan [rad]
            laser.angle_max = arg.angle_max        # end angle of the scan [rad]
            laser.angle_increment = arg.angle_increment  # angular distance between measurements [rad]
            laser.time_increment = arg.time_increment   # time between measurements [seconds] - if your scanne
            laser.scan_time = arg.scan_time        # time between scans [seconds]
            laser.range_min = arg.range_min        # minimum range value [m]
            laser.range_max = arg.range_max        # maximum range value [m]
            laser.ranges[i] = arg.ranges[i]
            rospy.sleep(0.25)
            pub.publish(laser)


if __name__ == "__main__":
    rospy.sleep(5)
    while not rospy.is_shutdown():

        rospy.init_node("sonar")
        pub = rospy.Publisher("/own/simulated/sonar_LS", LaserScan, queue_size=1)
        sub = rospy.Subscriber("/desistek_saga/sonar", LaserScan, callback)
