# -*-coding: utf-8-*-

import RPi.GPIO as GPIO ## Import GPIO library
import time


class LedManager:

    def __init__(self):
        # set modes (out)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT) # red
        GPIO.setup(27, GPIO.OUT) # yellow
        GPIO.setup(17, GPIO.OUT) # green


    def blinkOK(self):
        # QR is OK
        times = 4
        for i in range(0,times):
            GPIO.output(17,True)
            time.sleep(0.5)
            GPIO.output(17,False)
            time.sleep(0.5)

    def blinkKO(self):
        # QR is not OK
        times = 4
        for i in range(0,times):
            GPIO.output(4,True)
            time.sleep(0.5)
            GPIO.output(4,False)
            time.sleep(0.5)

    def blinkSyncProblem(self):
        # sync Problem
        times = 9
        for i in range(0,times):
            GPIO.output(27,True)
            time.sleep(2)
            GPIO.output(27,False)
            time.sleep(2)