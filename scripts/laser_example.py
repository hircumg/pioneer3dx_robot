#!/usr/bin/env python

import sys
from robot import *
import cv2
import rospy
import numpy as np



if __name__ == "__main__":
    robot = Robot()

    laser = robot.getLaser()
    dir = robot.getDirection()
    enc = robot.getEncoders()
    print("laser type: %s"% laser)
    print("Directon of robot: %s and values of encoders: left: %s, right: %s"%(dir,enc.get("left"),enc.get("right")))

    laser = laser.get('values')[40:len(laser.get('values'))-40]
    print(laser)
    print(len(laser))


    threshold = 0.5
    robot.setVelosities(0.2, 0)
    while(1):
        laser = robot.getLaser()
        laser = laser.get('values')[40:len(laser.get('values')) - 40]
        min = 5
        for i in laser:
            if i < min:
                min = i
        print("h = %s"%(min))

        if (min < threshold):
            print("wall")
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
        robot.sleep(0.01)

    exit(1)
