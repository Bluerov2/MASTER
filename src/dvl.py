#!/usr/bin/env python

import rospy
from uuv_sensor_ros_plugins_msgs.msg import DVL
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

class dvl:
	def __init__(self):
		sub_dvl = rospy.Subscriber('/desistek_saga/dvl', DVL, self.dvl_sub)
		sub_imu = rospy.Subscriber('/desistek_saga/imu', Imu, self.imu_sub)

		self.pubOdom = rospy.Publisher("/odom", Odometry, queue_size=1)

		self.timeDVL = rospy.get_time()
		self.previous_time = 0
		self.dvlseq = 0
		self.dvlsecs = 0
		self.dvlnsecs = 0
		self.dvlX = 0
		self.dvlY = 0
		self.dvlZ = 0
		self.OFFSET_X = 0
		self.OFFSET_Y = 0

		self.timeIMU = rospy.get_time()
		self.quaternionX = 0
		self.quaternionY = 0
		self.quaternionZ = 0
		self.quaternionW = 0
		self.imuX = 0
		self.imuY = 0
		self.imuZ = 0
		self.angvelX = 0
		self.angvelY = 0
		self.angvelZ = 0
		self.lastImuX = 0
		self.lastImuY = 0
		self.lastImuZ = 0

		self.dvlReceived = False

		self.estimated_traj_x = 0
		self.estimated_traj_y = 0
		self.estimated_traj_z = 0

	# The frequency of the DVL is lower than the IMU
	def dvl_sub(self,msg):

		self.timeDVL = rospy.get_time()

		self.dvlseq = msg.header.seq
		self.dvlsecs = msg.header.stamp.secs+1
		self.dvlnsecs = msg.header.stamp.nsecs
		self.dvlX = msg.velocity.z 		############ /!\ ###########
		self.dvlY = msg.velocity.y
		self.dvlZ = msg.velocity.x      ############ /!\ ###########

		self.dvlReceived = True

	# The frequency of the IMU is bigger than the DVL
	def imu_sub(self,msg):
		if self.dvlReceived == True:
			self.dvlReceived = False
			self.timeIMU = rospy.get_time()
			self.quaternionX = msg.orientation.x
			self.quaternionY = msg.orientation.y
			self.quaternionZ = msg.orientation.z
			self.quaternionW = msg.orientation.w
			X,Y,Z = self.quaternion_to_euler(self.quaternionX,self.quaternionY,self.quaternionZ,self.quaternionW)
			self.imuX = X
			self.imuY = Y
			self.imuZ = Z

			self.angvelX = msg.angular_velocity.x
			self.angvelY = msg.angular_velocity.y
			self.angvelZ = msg.angular_velocity.z

			self.estimateTraj()


	def estimateTraj(self):
		dt = float(self.timeDVL - self.previous_time)
		X = self.dvlX - self.OFFSET_X*(self.imuZ-self.lastImuZ)/dt
		Y = self.dvlY - self.OFFSET_Y*(self.imuZ-self.lastImuZ)/dt

		self.estimated_traj_x = self.estimated_traj_x + (X * dt * math.cos(self.imuZ) - Y * dt * math.sin(self.imuZ))
		self.estimated_traj_y = self.estimated_traj_y + (X * dt * math.sin(self.imuZ) + Y * dt * math.cos(self.imuZ))
		self.estimated_traj_z = self.estimated_traj_z - self.dvlZ * dt

		self.previous_time = self.timeDVL
		self.lastImuX = self.imuX
		self.lastImuY = self.imuY
		self.lastImuZ = self.imuZ

		self.convert_to_odom()

	def convert_to_odom(self):
		odm = Odometry()
		odm.header.seq = self.dvlseq
		odm.header.stamp.secs = self.dvlsecs
		odm.header.stamp.nsecs = self.dvlnsecs

		odm.header.frame_id = "desistek_saga/base_footprint"
		#odm.child_frame_id = "desistek_saga/base_footprint"

		odm.pose.pose.position.x = self.estimated_traj_x
		odm.pose.pose.position.y = self.estimated_traj_y
		odm.pose.pose.position.z = self.estimated_traj_z

		odm.pose.pose.orientation.x = self.quaternionX
		odm.pose.pose.orientation.y = self.quaternionY
		odm.pose.pose.orientation.z = self.quaternionZ
		odm.pose.pose.orientation.w = self.quaternionW
		self.pubOdom.publish(odm)

	def quaternion_to_euler(self,x,y,z,w):
		t0 = +2.0 * (w * x + y * z)
		t1 = +1.0 - 2.0 * (x * x + y * y)
		X = math.degrees(math.atan2(t0, t1))

		t2 = +2.0 * (w * y - z * x)
		t2 = +1.0 if t2 > +1.0 else t2
		t2 = -1.0 if t2 < -1.0 else t2
		Y = math.degrees(math.asin(t2))

		t3 = +2.0 * (w * z + x * y)
		t4 = +1.0 - 2.0 * (y * y + z * z)
		Z = math.atan2(t3, t4)

		return X, Y, Z

def main(args):
	rospy.init_node('read_dvl', anonymous=True)

	a = dvl()

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
		cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
