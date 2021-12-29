#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

motor = LargeMotor('outA')
kp = 15
ki = 0
kd = 1
pos = 360

data = open('PID_Kp' + str(kp) + '_Ki' + str(ki) + '_Kd' + str(kd) + '.txt', 'w')
data.write('0 0 \n')

motor.position = 0
timestart = time.time()

prevtime = timestart
dtime = 0
eprev = 0   
ei = 0      

while True:
    timenow = time.time()
    dtime = timenow - prevtime

    enow = motor.position - pos

    ei = ei + enow * dtime
    ed = (enow - eprev) / dtime
    ireg = ei * ki

    U_t = int(enow * kp + ed * kd + ireg)
    if U_t > 100:
        U = -100
    elif U_t < -100:
        U = 100
    motor.run_direct(duty_cycle_sp=U)
    eprev = enow
    data.write(str(time.time() - timestart) + ' ' + str(motor.position) + '\n')
    prevtime = timenow

    if time.time() - timestart > 5:
        break
motor.stop(stop_action='brake')
data.close()