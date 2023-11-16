"""
This file goes on the vex brain over a USB cable, the rest of the code can be pushed using deploy.py
"""


from vex import *

brain = Brain()

from Robot import Control
robot = Control()
robot.print()
