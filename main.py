#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

int stepCounter = 0

# Write your program here.
#ev3.speaker.beep()

# Initialize EV3 Brick
ev3 = EV3Brick()

# Initialize EV3 MotorA
motor_a = Motor(Port.A)

# Initialize EV3 MotorB
motor_b = Motor(Port.B)

# Initialize EV3 MotorC
motor_c = Motor(Port.C)

# Initialize EV3 MotorD
motor_d = Motor(Port.D)


#Run motor A at a speed of 360 degress/s for 500ms, stop type is default(coast) and wait is default(true)
#motor_a.run_time(360, 2000)

#Run motor B at a speed of 360 degress/s for 500ms, stop type is default(coast) and wait is default(true)
#motor_b.run_time(360, 2000)

#Following route to task
class FirstRoute
    colorVariable = Color()
    if colorVariable = Color.BLACK:
        motor_a.run_time(180, 500, Brake.coast wait.false)
        motor_b.run_time(90, 500)

    elif colorVariable = Color.WHITE:
        motor_a.run_time(90, 250, Brake.coast wait.false)
        motor_b.run_time(180, 250)
        pass 

#Moves stepcounter every 500 ms
class CountingSteps
    while stepCounter < 10:
        motor_a.run_time(360, 500, Brake.coast, wait.false)
        motor_b.run_time(360, 500)
        sleep(500)
        stepCounter = stepCounter + 1
        #stepCounter +=1
        pass

#Gripping the wheel and pulls it backwards
class GripWheel
    motor_c.run_time(180, 1000)
    
    motor_a.run_time(-360, 2000, Brake.coast, wait.false)
    motor_b.run_time(-360, 2000)
