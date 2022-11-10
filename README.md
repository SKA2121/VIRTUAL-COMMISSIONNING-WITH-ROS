# VIRTUAL-COMMISSIONNING-WITH-ROS

This repository is meant for ros related virtual commissioning work. 

Here, you will have all the packages ready to use with ROS. The package vc_ros contains the OPCUA client created to connect with the signals created in SIMIT. 

On the other hand, conveyor_gazebo contains the environnement for simulating the scenario with ROS. 

## Usage

Please remember that all these packages are meant to be copied into the src folder of your catkin workspace. Once that is done, you can the go a step backward with the "cd .." command and execute a "catkin_make" to rebuild your environment followed by the "source devel/setup.bash" to update your environment parameters. 
