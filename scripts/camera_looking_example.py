#!/usr/bin/env python

import sys
from robot_library.robot import *
import cv2
import rospy
import numpy as np
from time import time


if __name__ == "__main__":
    # initialize robot
    robot = Robot()

    # get image from camera
    img = robot.getImage()
    # open new window with original image
    # we also need convert RGB image info BGR image format for correct visualizing
    cv2.imshow('initial image', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

    img = img[430:800, 100:700]  # save only ground
    # open new window with cutted image
    # we also need convert RGB image info BGR image format for correct visualizing
    cv2.imshow('cutted image', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

    # make binary image
    ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 50, 255, cv2.THRESH_BINARY_INV)
    # open new window with binary image
    cv2.imshow('binary image', thresh)

    # wait any key
    cv2.waitKey(0)
    # close all opened windows with images
    cv2.destroyAllWindows()

