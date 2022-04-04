# ROS Robot OpenCV

- This project has been developed on [University of Toronto Robosoccer Team project](https://github.com/utra-robosoccer/Tutorials-2020). 

## Prerequisites
- Ubuntu 20.04.4 LTS
- ROS
- Python
- OpenCV

## Repo
Use the terminal for executing the following commands
```
cd 
mkdir -p catkin_ws/src
cd catkin_ws/src
git clone https://github.com/Armanasq/ros_robot_opencv.git
```
## Other Repos
- Some users may need to download the following repos to ensure the project run correctly.

- Please note that some/many packages are not available for ROS Neotic so, to solve this problem you can clone each one and try to install them manually.

- To solve the above problem (E: Unable to locate package *** ) I recommend to use the following comand below

```
cd ~/catkin_ws/src/

git clone https://github.com/ros-perception/vision_opencv.git

git clone https://github.com/ros-drivers/four_wheel_steering_msgs.git

git clone https://github.com/ros-controls/urdf_geometry_parser.git

git clone https://github.com/ros-drivers/video_stream_opencv.git

git clone https://github.com/ros-visualization/interactive_marker_twist_server.git

git clone https://github.com/cra-ros-pkg/robot_localization.git

git clone https://github.com/ros-teleop/teleop_twist_joy.git

git clone https://github.com/ros-teleop/twist_mux.git

git clone https://github.com/ros-geographic-info/unique_identifier.git

git clone https://github.com/ros/common_msgs.git

git clone https://github.com/ros-drivers/four_wheel_steering_msgs.git

git clone https://github.com/ros-controls/ros_control.git

catkin build 

rosdep update
```

## Updating Dependencies
```
cd ~/catkin_ws/
rosdep update
rosdep install --from-paths src --ignore-src -r -y --rosdistro neotic
sudo apt-get update
```

## Building ROS Robot OpenCV package
First build the project and source the setup file so that the system knows where to look for your build files
```
cd ~/catkin_ws
catkin build catkin build ros_robot_opencv 
source devel/setup.bash
```

## Launch the robot
```
roslaunch ros_robot_opencv gazebo.launch 
```
rosrun ros_robot_opencv motor_controller 


## Commands used during tutorial
useful tip: press tab to auto-complete words as you type commands
Open a new terminal to run commands for the robot

Spin the left arm

```
rostopic pub /left_wheel_controller/command std_msgs/Float64 "data: 1.0" 

```
Stop from spining
```
rostopic pub /left_wheel_controller/command std_msgs/Float64 "data: 0.0" 

```
