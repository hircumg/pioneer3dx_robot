#!/usr/bin/env python

import sys
from robot_library.robot import *
import cv2
import rospy
import numpy as np



if __name__ == "__main__":

    # initialize robot
    robot = Robot()


    # get laser values
    laser = robot.getLaser()

    # get values of laser and remove some extreme values because laser see himself
    laser = laser.get('values')[40:len(laser.get('values'))-40]
    print(laser)

    # how close robot could go to the obstacles
    threshold = 0.5

    robot.setVelosities(0.3, 0)

    while True:

        robot.setVelosities(0.3, 0)
        laser = robot.getLaser()
        laser = laser.get('values')[40:len(laser.get('values')) - 40]

        # find minimum value if laser values
        min = 5
        for i in laser:
            if i < min:
                min = i
        print("h = %s"%(min))

        # Check should or should not robot turn to avoid obstacle
        if (min < threshold):
            print("There's an obstacle near")
            robot.setVelosities(0,0.3)
            while(min <= threshold):
                laser = robot.getLaser()
                laser = laser.get('values')[40:len(laser.get('values')) - 40]
                min = 5
                for i in laser:
                    if i < min:
                        min = i
                print("h = %s" % (min))
                robot.sleep(0.5)

            print("no wall")
            robot.setVelosities(0.3, 0)

        # some delay for don't overload computation
        robot.sleep(0.005)

    exit(1)
