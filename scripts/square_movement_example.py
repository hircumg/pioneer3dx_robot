#!/usr/bin/env python

import sys
from robot import *
import cv2
import rospy
import numpy as np
import math

robot = Robot()
radius_of_the_wheel = 0.09

def turn(add_deg):
    global robot
    current_dir =robot.getDirection()
    if type(add_deg) is int:
        add_deg_rad = add_deg * 3.14 / 180
    else:
        add_deg_rad = add_deg
    print("__________________________________________________")
    target_dir = current_dir + add_deg_rad
    e = (target_dir - current_dir + 9.42) % 6.28 - 3.14
    print("e: %s, current dir: %s and target dir: %s" % (e, current_dir, target_dir))

    if e > 0:
        robot.setVelosities(0, 0.3)
    else:
        robot.setVelosities(0, -0.3)

    while abs(e) > 0.005:
        current_dir = robot.getDirection()
        e = (target_dir - current_dir + 9.42) % 6.28 - 3.14
        up = e * 0.7
        up = (up if up > -0.4 else -0.4) if up < 0.4 else 0.4
        robot.setVelosities(0, up)
        print("e: %s, current dir: %s and target dir: %s"%(e,current_dir,target_dir))
        robot.sleep(0.001)

    robot.setVelosities(0,0)
    return target_dir

def moveDist(dist, target_dir = robot.getDirection()):
    global radius_of_the_wheel
    enc = robot.getEncoders()
    initial_enc = enc.get("left")
    dist_left = (dist * 1.0 / radius_of_the_wheel)
    if dist > 0:
        robot.setVelosities(0.1,0.0)
    else:
        robot.setVelosities(-0.1, 0.0)
    while abs(dist_left) > 0.005:
        enc = robot.getEncoders().get("left")
        dist_left = initial_enc + (dist * 1.0 / radius_of_the_wheel) - enc
        up = 0.1 * dist_left
        up = (up if up > -0.3 else -0.3) if up < 0.3 else 0.3


        current_dir = robot.getDirection()
        e = (target_dir - current_dir + 9.42) % 6.28 - 3.14
        up_ang = e * 0.5
        up_ang = (up_ang if up_ang > -0.3 else -0.3) if up_ang < 0.3 else 0.3
        robot.setVelosities(up, up_ang)


        print("begin in: %s current enc %s dist_left: %s and up: %s"%(initial_enc, enc, dist_left * radius_of_the_wheel, up))
        robot.sleep(0.001)

    robot.setVelosities(0, 0)

if __name__ == "__main__":
    robot = Robot()

    dir = robot.getDirection()
    enc = robot.getEncoders()
    print("Directon of robot: %s and values of encoders: left: %s, right: %s"%(dir,enc.get("left"),enc.get("right")))

    moveDist(1,turn(90))
    robot.sleep(1)
    moveDist(1,turn(90))
    robot.sleep(1)
    moveDist(1,turn(90))
    robot.sleep(1)
    moveDist(1,turn(90))
    robot.sleep(1)

    exit(1)
