#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from opcua import Client, ua 
import rospy
from sensor_msgs.msg import JointState



def ConnectSignals() :

# Connect to OPC UA server fro; SIMIT after you have created the server
	client = Client('opc.tcp://192.168.100.10:47144')
#192.168.237.1
	client.connect()
	print("Connexion ok, great news")

# Connect to signals from SIMIT

	client.get_namespace_array()
	objects = client.get_objects_node()

	simit_signals = objects.get_children()[1]
	simit_signals.get_children()


	global joint_1_angle, joint_2_angle, joint_3_angle, joint_4_angle, joint_5_angle, joint_6_angle
	joint_1_angle=simit_signals.get_children()[5].get_children()[0]
	joint_2_angle=simit_signals.get_children()[5].get_children()[1] 
	joint_3_angle=simit_signals.get_children()[5].get_children()[2] 
	joint_4_angle=simit_signals.get_children()[5].get_children()[3] 
	joint_5_angle=simit_signals.get_children()[5].get_children()[4] 
	joint_6_angle=simit_signals.get_children()[5].get_children()[5]  

	print(joint_1_angle)
	print(joint_2_angle)
	print(joint_3_angle)
	print(joint_4_angle)
	print(joint_5_angle)
	print(joint_6_angle)

# Subscribe to the topics to obtain the related joints 

	rospy.init_node('simit_kinova', anonymous = True)
	ros_joints_sub = rospy.Subscriber('/j2n6s300_driver/out/joint_state', JointState, JointCallback)
	rate = rospy.Rate(1)

#Create an instance of the JointState message
	js = JointState()

	
#disconnect from the server
def JointCallback(data):
    global joint_1_angle, joint_2_angle, joint_3_angle, joint_4_angle, joint_5_angle, joint_6_angle
# Transmit the joint values to SIMIT 
    joint_1_angle.set_value(data.position[0])
    joint_2_angle.set_value(data.position[1])
    joint_3_angle.set_value(data.position[2])
    joint_4_angle.set_value(data.position[3])
    joint_5_angle.set_value(data.position[4])
    joint_6_angle.set_value(data.position[5])



if __name__ == '__main__':
    try:
        ConnectSignals()
    except rospy.ROSInterruptException:
        pass

