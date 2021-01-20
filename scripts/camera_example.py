#!/usr/bin/env python3

import sys
from robot_library.robot import *
import cv2
import rospy
import numpy as np
from time import time


if __name__ == "__main__":
    # initialize robot
    robot = Robot()



    while(1):
        # get image from camera
        img = robot.getImage()
        img = img[430:800, 100:700]  # save only ground

        # make binary image
        ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 50, 255, cv2.THRESH_BINARY_INV)


        # calculate image moments to fing centre mass
        M = cv2.moments(thresh)
        area = M['m00']
        if area > 0:
            cx = int(M['m10'] / area)
            cy = int(M['m01'] / area)
        else:
            cx = 300
            cy = None


        up = (300 - cx) * 0.003
        robot.setVelosities(0.6, up)

        robot.sleep(0.005)


