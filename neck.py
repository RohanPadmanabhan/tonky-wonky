import RPi.GPIO as GPIO
NECK_PIN = 17


class Neck:
    def __init__(self):
        GPIO.setup(NECK_PIN, GPIO.OUT)
        self._servo = GPIO.PWM(NECK_PIN, 50)
        self._servo.start(10)
        print("Init neck")
    
    def raise_neck(self):
        self._servo.ChangeDutyCycle(2)
        print("Turning on neck")
    
    def lower_neck(self):
        self._servo.ChangeDutyCycle(10)
        print("Turning off neck")
    
    def shut_down(self):
        self._servo.stop()
        print("Shutting down neck")
