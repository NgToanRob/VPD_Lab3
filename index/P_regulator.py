#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

motor = LargeMotor('outA')

kp = 15
pos = 360

data = open('P_regulator_Kp' + str(kp) + '.txt', 'w')

data.write('0 0 \n')
motor.position = 0
timestart = time.time()

while True:
    timenow = time.time() - timestart
    u = kp * (motor.position - pos)

    if u <= -100:                              
        motor.run_direct(duty_cycle_sp=100)
    elif u >= 100:
        motor.run_direct(duty_cycle_sp=-100)
    else:
        motor.run_direct(duty_cycle_sp=u)
    data.write(str(timenow) + ' ' + str(motor.position) + '\n')
    if time.time() - timestart > 5:
        break
motor.stop(stop_action='brake')
data.close()
    # time.sleep(2);

