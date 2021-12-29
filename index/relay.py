#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

motor = LargeMotor('outA')

pos = 360
data = open('relay Data.txt', 'w')
data.write('0 0 \n')
# motor.position = 0
timestart = time.time()

while True:
    timenow = time.time() - timestart
    if motor.position < pos:
        motor.run_direct(duty_cycle_sp=100)
    elif motor.position > pos:
        motor.run_direct(duty_cycle_sp=-100)
    data.write(str(timenow) + ' ' + str(motor.position) + '\n')
    if time.time() - timestart > 5:
        break
motor.stop(stop_action='brake')
data.close()