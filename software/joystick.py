#!/usr/bin/env python3
# encoding: utf-8

import os
import time
import json
import pygame
import math
import requests
import socket

address = ('127.0.0.1', 3982)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('[Port Opened] ',address[0],':',address[1])
#trigger = [motor,motor1,motor2,motor3]
#s.sendto(trigger.encode(), address)

turnningSpeedSmall=60
turnningSpeed=80
turnningSpeedMax=90
servoStep=2
key_map = {"PSB_CROSS":2, "PSB_CIRCLE":1, "PSB_SQUARE":3, "PSB_TRIANGLE":0,
        "PSB_L1": 4, "PSB_R1":5, "PSB_L2":6, "PSB_R2":7,
        "PSB_SELECT":8, "PSB_START":9, "PSB_L3":10, "PSB_R3":11};

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.display.init()
pygame.joystick.init()

c=0
if False and pygame.joystick.get_count() > 0 :
    js=pygame.joystick.Joystick(0)
    js.init()
    jsName = js.get_name()
    print("Name of the joystick:", jsName)
    jsAxes=js.get_numaxes()
    print("Number of axif:",jsAxes)
    jsButtons=js.get_numbuttons()
    print("Number of buttons:", jsButtons);
    jsBall=js.get_numballs()
    print("Numbe of balls:", jsBall)
    jsHat= js.get_numhats()
    print("Number of hats:", jsHat)

connected = False
trigger = [0,0,0,0,310,168]
while True:
    trigger = [0,0,0,0,trigger[4],trigger[5]]
    if os.path.exists("/dev/input/js0") is True:
        if connected is False:
            jscount =  pygame.joystick.get_count()
            if jscount > 0:
                try:
                    js=pygame.joystick.Joystick(0)
                    js.init()
                    connected = True
                except Exception as e:
                    print(e)
            else:
                pygame.joystick.quit()
    else:
        if connected is True:
            connected = False
            js.quit()
            pygame.joystick.quit()
    if connected is True:
        pygame.event.pump()
        try:
            if js.get_button(key_map["PSB_R1"]) :
                print("PSB_R1")
                trigger[4]+=servoStep
                trigger[5]-=servoStep
            if js.get_button(key_map["PSB_L1"])  :
                print("PSB_L1")
                trigger[4]-=servoStep
                trigger[5]-=servoStep
            if js.get_button(key_map["PSB_SQUARE"]) :
                print("PSB_SQUARE")
                trigger[0]-=turnningSpeed
                trigger[1]+=turnningSpeed
                trigger[2]+=turnningSpeed
                trigger[3]-=turnningSpeed
            if js.get_button(key_map["PSB_CIRCLE"]) :
                print("PSB_CIRCLE")
                trigger[0]+=turnningSpeed
                trigger[1]-=turnningSpeed
                trigger[2]-=turnningSpeed
                trigger[3]+=turnningSpeed
            if js.get_button(key_map["PSB_R2"]) :
                print("PSB_R2")
                trigger[4]+=servoStep
                trigger[5]+=servoStep
            if js.get_button(key_map["PSB_L2"]) :
                print("PSB_L2")
                trigger[4]-=servoStep
                trigger[5]+=servoStep
            if js.get_button(key_map["PSB_TRIANGLE"]) :
                print("PSB_TRIANGLE")
                for i in range(4):
                    trigger[i]+=turnningSpeed
            if js.get_button(key_map["PSB_CROSS"]) :
               print("PSB_CROSS")
               for i in range(4):
                    trigger[i]-=turnningSpeed

            if js.get_button(key_map["PSB_L3"]) :
                print("PSB_L3")
            if js.get_button(key_map["PSB_R3"]) :
                print("PSB_R3")


            hat = js.get_hat(0)
            #print('(hat)',hat)
            if hat[0] > 0 :
                print("hat[0] +++")
                trigger[0] = trigger[0]+turnningSpeed
                trigger[2] = trigger[2]+turnningSpeed
                trigger[3] = trigger[3]-turnningSpeed
                trigger[1] = trigger[1]-turnningSpeed

            if hat[0] < 0:
                print("hat[0] ---")
                trigger[0] = trigger[0]-turnningSpeed
                trigger[2] = trigger[2]-turnningSpeed
                trigger[3] = trigger[3]+turnningSpeed
                trigger[1] = trigger[1]+turnningSpeed

            if hat[1] > 0 :
                print("hat[1] +++")
                for i in range(4):
                    trigger[i]=trigger[i]+turnningSpeed


            if hat[1] < 0:
                print("hat[1] ---")
                for i in range(4):
                    trigger[i]=trigger[i]-turnningSpeed

            detect_lowerbound = 0.01
            lx = js.get_axis(0)
            ly = -1*js.get_axis(1)
            rx = js.get_axis(2)
            ry = -1*js.get_axis(3)
            if  -detect_lowerbound <lx <detect_lowerbound  :
                 pass
            else:
                print('axis_lx', lx)
                if lx<0:
                    trigger[0]=trigger[0]+lx*turnningSpeedSmall
                    trigger[2]=trigger[2]+lx*turnningSpeedSmall
                    trigger[1]=trigger[1]-lx*turnningSpeedSmall
                    trigger[3]=trigger[3]-lx*turnningSpeedSmall
                else:
                    trigger[0]=trigger[0]+lx*turnningSpeedSmall
                    trigger[2]=trigger[2]+lx*turnningSpeedSmall
                    trigger[1]=trigger[1]-lx*turnningSpeedSmall
                    trigger[3]=trigger[3]-lx*turnningSpeedSmall


            if  -detect_lowerbound <ly <detect_lowerbound  :
                pass
            else:
                print('axis_ly', ly)
                for i in range(4):
                    trigger[i]=trigger[i]+ly*turnningSpeed

            if  -detect_lowerbound <rx <detect_lowerbound  :
                pass
            else:
                print('axis_rx', rx)
                trigger[0]+=turnningSpeed*rx*1.3
                trigger[1]-=turnningSpeed*rx*1.3
                trigger[2]-=turnningSpeed*rx*1.3
                trigger[3]+=turnningSpeed*rx*1.3

            if  -detect_lowerbound <ry <detect_lowerbound  :
                 pass
            else:
                  print('axis_ry', ry)
                  for i in range(4):
                    trigger[i]+=turnningSpeed*ry


            if js.get_button(key_map["PSB_START"]):
                print('PSB_START')
        except Exception as e:
            print(e)
            connected = False
    for i in range(4):
        trigger[i] = (trigger[i])*1
        trigger[i] = max(min(trigger[i],turnningSpeedMax),-1*turnningSpeedMax)
    trigger[5] = max(min(trigger[5],330),155)
    trigger[4] = max(min(trigger[4],430),220)

    #print("Send ",trigger)
    s.sendto(str(trigger).encode(), address)
    time.sleep(0.06)
s.close()