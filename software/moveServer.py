#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
* @par Copyright (C): 2010-2020, hunan CLB Tech
* @file         Basic_movement
* @version      V2.0
* @details
* @par History

@author: zhulin
"""
from LOBOROBOT import LOBOROBOT  # 载入机器人库
import  RPi.GPIO as GPIO
import os
import time
import sys
import socket





address = ('127.0.0.1', 3982)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
s.settimeout(1)
print('[Port Opened] ',address[0],':',address[1])
def main():
    clbrobot = LOBOROBOT() # 实例化机器人对象
    data=[0.0,0.0,0.0,0.0,0.0,0.0]
    while True:
        try:
            data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
            data = data.decode()
            data = eval(data)
            print('[Received]', data)
        except socket.timeout:
            for i in range(4):
                data[i]=0
            print('[Receiving]')

        for i in range(4):
            speed = data[i]
            if speed>0:

                clbrobot.MotorRun(i,'forward',speed)
            else:

                clbrobot.MotorRun(i,'backward',-1*speed)

        data[5] = max(min(data[5],310),155)
        data[4] = max(min(data[4],430),220)
        clbrobot.pwm.setPWM(10,0,data[4])
        clbrobot.pwm.setPWM(9,0,data[5])





main()
clbrobot.t_stop(0)
GPIO.cleanup()