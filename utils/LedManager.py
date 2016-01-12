# -*-coding: utf-8-*-

import RPi.GPIO as GPIO ## Import GPIO library
import time


class LedManager:

    def __init__(self):
        # set modes (out)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT) # red
        GPIO.setup(13, GPIO.OUT) # yellow
        GPIO.setup(11, GPIO.OUT) # green


    def blinkOK(self):
        # QR is OK
        times = 4
        for i in range(0,times):
            GPIO.output(11,True)
            time.sleep(0.5)
            GPIO.output(11,False)
            time.sleep(0.5)

    def blinkKO(self):
        # QR is not OK
        times = 4
        for i in range(0,times):
            GPIO.output(7,True)
            time.sleep(0.5)
            GPIO.output(7,False)
            time.sleep(0.5)

    def blinkSyncProblem(self):
        # sync Problem
        times = 9
        for i in range(0,times):
            GPIO.output(13,True)
            time.sleep(2)
            GPIO.output(13,False)
            time.sleep(2)