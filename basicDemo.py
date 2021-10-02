import RPi.GPIO as GPIO
import time
import random

NECK_PIN = 17
MOUTH_PIN = 27
L_EYE_PIN = 18
R_EYE_PIN = 16

def setup():
    global neck
    global mouth

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(NECK_PIN, GPIO.OUT)
    GPIO.setup(MOUTH_PIN, GPIO.OUT)
    GPIO.setup(L_EYE_PIN, GPIO.OUT)
    GPIO.setup(R_EYE_PIN, GPIO.OUT)
    neck = GPIO.PWM(NECK_PIN, 50)
    mouth = GPIO.PWM(MOUTH_PIN, 50)
    neck.start(10)
    mouth.start(2.5)
    time.sleep(1)

def shutdown():
    global neck
    global mouth
    neck.stop()
    mouth.stop()
    GPIO.cleanup()

def head_up():
    global neck
    neck.ChangeDutyCycle(2)

def head_down():
    global neck
    neck.ChangeDutyCycle(10)

def mouth_move():
        global mouth
        mouth.ChangeDutyCycle(3)
        time.sleep(random.random()/2)
        mouth.ChangeDutyCycle(7)
        time.sleep(random.random()/2)

def eyes_on():
    GPIO.output(L_EYE_PIN, GPIO.HIGH)
    GPIO.output(R_EYE_PIN, GPIO.HIGH)

def eyes_off():
    GPIO.output(L_EYE_PIN, GPIO.LOW)
    GPIO.output(R_EYE_PIN, GPIO.LOW)

setup()
for i in range(3):
    head_up()
    eyes_on()
    for i in range(20):
            mouth_move()
    head_down()
    eyes_off()
    time.sleep(4)
shutdown()