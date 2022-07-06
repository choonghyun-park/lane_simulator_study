# Tutorial for Kookmin_AutoCon prereminary assingments
This is the simple tutorial for Kookmin university Autonomous contest preliminary assignments. You have to install some setups and build your workspace in the following workflow.

## Prerequisites
### Environments
Ubuntu 18.04 & ROS melodic

### Installation
Install setups\
`rosbridge`
```Terminal
sudo apt update
sudo apt install ros-melodic-rosbridge-server
```
dependency packages\
`ar-track-alvar`, `pygame`, `pillow`
```terminal
sudo apt update
sudo apt-get install ros-melodic-ar-track-alvar
pip2 install pygame==1.9.6
pip2 install pillow==6.2.2
```

### Create workspace
Create catkin_workspace and build for Kookmin_AutoCon repository.
```Terminal
mkdir -p ~/xytron_ws/src
cd ~/xytron_ws/src
git clone https://github.com/choonghyun-park/lane_simulator_study.git .
cd ..
catkin_make
```
If your catkin_make complete, now you are ready to launch the code.

## Launch simulator
### assignment1
Launch the rosbridge
```terminal
cd ~/xytron_ws
source devel/setup.bash
roslaunch rosbridge_server rosbridge_websocket.launch
```
Run the simulator
```terminal
cd ~/xytron_ws/src/xycar_sim_driving
./xycar3Dsimulator.x86_64
```
Launch the driving code for assignment1
```terminal
cd ~/xytron_ws
source devel/setup.bash
roslaunch xytron driving.launch
```



