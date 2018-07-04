#!/usr/bin/env python

import sys
from robot import *
import cv2
import rospy
import numpy as np



if __name__ == "__main__":
    robot = Robot()

    dir = robot.getDirection()
    enc = robot.getEncoders()
    print("laser type: %s"% laser)
    print("Directon of robot: %s and values of encoders: left: %s, right: %s"%(dir,enc.get("left"),enc.get("right")))

    

    exit(1)
