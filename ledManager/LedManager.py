import RPi.GPIO as GPIO ## Import GPIO library
import time

# set modes (out)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) # red
GPIO.setup(21, GPIO.OUT) # yellow
GPIO.setup(12, GPIO.OUT) # green


def blinkOK():
    # QR is OK
    times = 4
    for i in range(0,times):
        GPIO.output(12,True)
        time.sleep(0.5)
        GPIO.output(12,False)
        time.sleep(0.5)

def blinkKO():
    # QR is not OK
    times = 4
    for i in range(0,times):
        GPIO.output(7,True)
        time.sleep(0.5)
        GPIO.output(7,False)
        time.sleep(0.5)

def blinkSyncProblem():
    # sync Problem
    times = 9
    for i in range(0,times):
        GPIO.output(21,True)
        time.sleep(2)
        GPIO.output(21,False)
        time.sleep(2)

print("test blink ok")
blinkOK()
time.sleep(5)
print("test blink ko")
blinkKO()
time.sleep(5)
print("test blink sync ko")
blinkSyncProblem()