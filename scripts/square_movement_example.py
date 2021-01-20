#!/usr/bin/env python3

import sys
from robot_library.robot import *
import cv2
import rospy
import numpy as np
import math

# initialize robot
robot = Robot()
radius_of_the_wheel = 0.09

def turn(add_deg_rad):
    """This function turns robot to given angle in radians
    :return absolute angle for rotating"""
    global robot

    current_dir =robot.getDirection()
    target_dir = current_dir + add_deg_rad

    # calculate error of rotation
    e = (target_dir - current_dir + 9.42) % 6.28 - 3.14


    while abs(e) > 0.005:

        current_dir = robot.getDirection()
        e = (target_dir - current_dir + 9.42) % 6.28 - 3.14
        up = e * 0.7

        # for don't move so fast
        up = (up if up > -0.4 else -0.4) if up < 0.4 else 0.4

        robot.setVelosities(0, up)

        # some delay for don't overload computation
        robot.sleep(0.001)

    robot.setVelosities(0,0)
    return target_dir

def moveDist(dist, target_dir = robot.getDirection()):
    global radius_of_the_wheel

    # calculating how many radians to the required position left
    dist_left = (dist / radius_of_the_wheel)

    # save initial number of encoders
    initial_enc = robot.getEncoders().get("left")

    while abs(dist_left) > 0.005:
        # calculating how many radians to the required position left
        enc = robot.getEncoders().get("left")
        dist_left = initial_enc + (dist * 1.0 / radius_of_the_wheel) - enc
        up = 0.1 * dist_left
        up = (up if up > -0.3 else -0.3) if up < 0.3 else 0.3


        # trave to the angle
        current_dir = robot.getDirection()
        e = (target_dir - current_dir + 9.42) % 6.28 - 3.14
        up_ang = e * 0.5
        up_ang = (up_ang if up_ang > -0.3 else -0.3) if up_ang < 0.3 else 0.3

        robot.setVelosities(up, up_ang)

        # some delay for don't overload computation
        robot.sleep(0.001)

    robot.setVelosities(0, 0)

if __name__ == "__main__":
    robot = Robot()


    # just move square 1x1m
    moveDist(1,turn(1.57))
    robot.sleep(1)
    moveDist(1,turn(1.57))
    robot.sleep(1)
    moveDist(1,turn(1.57))
    robot.sleep(1)
    moveDist(1,turn(1.57))
    robot.sleep(1)

    exit(1)
