#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2, math
import rospy, rospkg, time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from xycar_msgs.msg import xycar_motor
from math import *
import signal
import sys
import os
import random

def signal_handler(sig, frame):
    import time
    time.sleep(3)
    os.system('killall -9 python rosout')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

image = np.empty(shape=[0]) 
bridge = CvBridge() 
motor = None 

CAM_FPS = 30    
WIDTH, HEIGHT = 640, 480    

def img_callback(data):
    global image
    image = bridge.imgmsg_to_cv2(data, "bgr8")

def drive(angle, speed):

    global motor

    motor_msg = xycar_motor()
    motor_msg.angle = angle
    motor_msg.speed = speed

    motor.publish(motor_msg)

def start():

    global motor, image

    rospy.init_node('driving')
    motor = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)
    image_sub = rospy.Subscriber("/usb_cam/image_raw/",Image,img_callback)

    print ("----- Xycar self driving -----")

    while not image.size == (WIDTH * HEIGHT * 3):
        continue
 
    while not rospy.is_shutdown():

        img = image.copy()  

        cv2.imshow("CAM View", img)
        cv2.waitKey(1)       
	
        angle = 0
        speed = 10

        drive(angle, speed)


if __name__ == '__main__':
    start()

