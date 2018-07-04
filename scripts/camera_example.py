#!/usr/bin/env python

import sys
from robot import *
import cv2
import rospy
import numpy as np
from time import time

def identify(frame):
    t_in = time()
    zones = [0, 0, 0]
    konst = 250
    frame = cv2.addWeighted(frame, 2, np.zeros(frame.shape, frame.dtype), 0.0, 0.0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GREY)

    # mask = cv2.inRange(hsv, (150,91,100),(200,250,255))
    mask = cv2.inRange(hsv, (0, 127, 47), (5, 255, 255))

    # mask = cv2.medianBlur(mask,3)



    # t_in = rospy.get_time() - t_in
    # rospy.loginfo("1. I got an image  at %s " %t_in)


    M = cv2.moments(mask)
    area = M['m00']
    if area > 0:
        cx = int(M['m10'] / area)
        cy = int(M['m01'] / area)
        cv2.circle(frame, (int(cx), int(cy)), 10, (255, 0, 0), -1)
        zones = [cx - 160, cy - 120, 0]
    else:
        cx = None
        cy = None
        zones = [0, 0, -1]

    print("area= %s, cx = %s, cy = %s" % (area, cx, cy))

    t_in = time() - t_in
    rospy.loginfo("I got an image  at %s " % t_in)

if __name__ == "__main__":
    print(sys.path)

    robot = Robot()
    img = robot.getImage()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = img[430:800,100:700] # save only ground


    while(1):
        t_in = time()
        img = robot.getImage()
        img = img[430:800, 100:700]  # save only ground

        # print(img.shape)

        ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 127, 255, cv2.THRESH_BINARY_INV)

        # print(thresh.shape)
        # thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
        # print(im)
        M = cv2.moments(thresh)
        area = M['m00']
        if area > 0:
            cx = int(M['m10'] / area)
            cy = int(M['m01'] / area)
            # cv2.circle(img, (int(cx), int(cy)), 10, (255, 0, 0), -1)
            # zones = [cx - 160, cy - 120, 0]
        else:
            cx = 300
            cy = None
            # zones = [0, 0, -1]


        up = (300 - cx) * 0.003
        robot.setVelosities(0.6, up)
        print("area= %s, cx = %s, cy = %s, up = %s" % (area, cx, cy, up))
        # cv2.imshow('tresh', thresh)
        # cv2.imshow('frame', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # rospy.sleep(2)
        # dir = robot.getDirection()
        # enc = robot.getEncoders()
        # print("Directon of robot: %s and values of encoders: left: %s, right: %s" % (dir, enc.get("left"), enc.get("right")))
        t_in = time() - t_in
        print("I got an image  at %s " % t_in)
        robot.sleep(0.05)



    dir = robot.getDirection()
    enc = robot.getEncoders()
    print("Directon of robot: %s and values of encoders: left: %s, right: %s"%(dir,enc.get("left"),enc.get("right")))
    #
    # robot.setVelosities(-0.5,-0.5)
    # rospy.sleep(2)
    # robot.setVelosities(0.0,0.0)
    # exit(1)
