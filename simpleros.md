# creating node and simple publisher
```
mkdir -p ~/simpleros_ws/src
cd ~/simpleros_ws
catkin_make
cd ~/simpleros_ws/src
catkin_create_pkg beginner_tutorials rospy std_msgs 
```
create talker.py
```
cd ~/simpleros_ws/src/beginner_tutorials
mkdir scripts
```
please create talker.py here\
give permission using chmod
```
chmod +x talker.py
```
catkin_make
```
cd ~/simpleros_ws
catkin_make
```
launch
```
rosrun beginner_tutorials talker.py
```


