#!/usr/bin/env python3
import math

from ev3dev.ev3 import *
import time

motor = LargeMotor('outA')

def relay(pos):
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
        
        if time.time() - timenow > 5:
            break
    motor.stop(stop_action='brake')
    data.close()


def p(kp, pos):
    data = open('PPP ' + str(kp) + ' Data.txt', 'w')
    data.write('0 0 \n')
    motor.position = 0
    timestart = time.time()

    while True:
        timenow = time.time() - timestart
        u = kp * (pos - motor.position)
        if u <= -100:                              
            motor.run_direct(duty_cycle_sp=-100)
        elif u >= 100:
            motor.run_direct(duty_cycle_sp=100)
        else:
            motor.run_direct(duty_cycle_sp=u)
        data.write(str(timenow) + ' ' + str(motor.position) + '\n')
        if time.time() - timestart > 5:
            break
    motor.stop(stop_action='brake')
    data.close()

def pid(kp, ki, kd, pos):
    data = open('PID ' + str(kp) + ' ' + str(ki) + ' ' + str(kd) + ' Data.txt', 'w')
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
        enow = pos - motor.position
        ei = ei + enow * dtime
        ed = (enow - eprev) / dtime
        ireg = ei * ki

        U_t = int(enow * kp + ed * kd + ireg)
        if U_t > 100:
            U = 100
        elif U_t < -100:
            U = -100
        motor.run_direct(duty_cycle_sp=U)
        eprev = enow
        data.write(str(time.time() - timestart) + ' ' + str(motor.position) + '\n')
        prevtime = timenow

        if time.time() - timestart > 5:
            break
    motor.stop(stop_action='brake')
    data.close()

# Main
relay(360)


# for i in range(4,20,4):
#         for j in range(5,50,10):
#             pid(15, j, i, 360)
