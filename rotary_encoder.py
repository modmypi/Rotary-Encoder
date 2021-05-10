#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:40:57 2021

@author: nivethithakannan
"""
from RPi import GPIO
from time import sleep

PIN_CLK = 17
PIN_DAT = 18

GPIO.setmode(GPIO.BCM)

try:
    GPIO.setup(PIN_CLK,GPIO.IN)
    GPIO.setup(PIN_DAT,GPIO.IN)
    GPIO.output(PIN_CLK,1)
except:
    print("ERROR. Unable to setup the configuration requested"  )                                   


sleep(0.5)
counter = 0
clkLastState = GPIO.input(PIN_CLK)

try:

        while True:
                clkState = GPIO.input(PIN_CLK)
                dtState = GPIO.input(PIN_DAT)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print(counter)
                clkLastState = clkState
                sleep(0.01)
finally:
        GPIO.cleanup()
