# How to start Franka simulation

`cd ~/ws_moveit/devel`

### source the setup file to initial the roslaunch command

`source setup.bash`

### start RVIZ to preview the simulation

`roslaunch panda_moveit_config demo.launch`

#### For now, U should see a robot arm in the RVIZ window. Use the middle botton on mouse for shifting and left for rotation.

To use the RVIZ for simulation, `conda` must be deactivated. The code is shown as below.

### if base is attached to the terminal command, use the following command

`conda deactivate`



# libfranka code and function

### motion_with_control  for raise up and down

`cd ~/libfranka/build`

`./examples/motion_with_control 172.16.0.2`

press Enter to continue...

### generate_joint_velocity_motion  for raise, twist and down

`cd ~/libfranka/build`

`./examples/generate_joint_velocity_motion 172.16.0.2`