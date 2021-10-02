import RPi.GPIO as GPIO

L_EYE_PIN = 18
R_EYE_PIN = 16

class Eyes:
    def __init__(self):
        GPIO.setup(L_EYE_PIN, GPIO.OUT)
        GPIO.setup(R_EYE_PIN, GPIO.OUT)
        print("Init eyes")
    
    def turn_on(self):
        GPIO.output(L_EYE_PIN, GPIO.HIGH)
        GPIO.output(R_EYE_PIN, GPIO.HIGH)
        print("Turning on eyes")

    def turn_off(self):
        GPIO.output(L_EYE_PIN, GPIO.LOW)
        GPIO.output(R_EYE_PIN, GPIO.LOW)
        print("Turning off eyes")
    

    def shut_down(self):
        print("Shutting down eyes")
