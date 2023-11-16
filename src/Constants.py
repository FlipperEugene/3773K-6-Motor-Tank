from vex import *

class Team:
    Red = 0
    Blue = 1
    Skills = 2


    
"""Sensors"""
inertial_sensor_port = Ports.PORT5


"""Drive Base

+------+
| 1  2 | "Bottom Middle Motors"
|      |
| 3  4 | "Bottom Motors"
| 5  6 | "Top Motors"
+------+
1, 3, and 5 are the left side motors please check
to make sure what motors need to be inverted 
to prevent overheating and blowing a motor.
for me motors 3 and 1 are inverted and the top motor is motor 5.

"""
"""Left Side Motors"""
Motor_1 = Ports.PORT20
Motor_3 = Ports.PORT19
Motor_5 = Ports.PORT18

"""Right Side Motors"""

Motor_2 = Ports.PORT13
Motor_4 = Ports.PORT12
Motor_6 = Ports.PORT11
