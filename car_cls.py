import RPi.GPIO as GPIO

class Car():
    def __init__(self, ln1, ln2, ln3, ln4, ena, enb):
        self.ln1: int = ln1
        self.ln2: int = ln2
        self.ln3: int = ln3
        self.ln4: int = ln4
        self.ena = ena 
        self.enb = enb
        self.speed: int = 25

        GPIO.setup(self.ln1, GPIO.OUT)
        GPIO.setup(self.ln2, GPIO.OUT)
        GPIO.setup(self.ln3, GPIO.OUT)
        GPIO.setup(self.ln4, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.enb, GPIO.OUT)

        GPIO.output(self.ln1, GPIO.LOW)
        GPIO.output(self.ln2, GPIO.LOW)
        GPIO.output(self.ln3, GPIO.LOW)
        GPIO.output(self.ln4, GPIO.LOW)

        self.pa = GPIO.PWM(self.ena, 1000)
        self.pb = GPIO.PWM(self.enb, 1000)

        self.pa.start(25)
        self.pb.start(25)
        
    def forward(self):
        GPIO.output(self.ln1, GPIO.HIGH)
        GPIO.output(self.ln2, GPIO.LOW)
        GPIO.output(self.ln3, GPIO.HIGH)
        GPIO.output(self.ln4, GPIO.LOW)
    def backward(self):
        GPIO.output(self.ln1, GPIO.LOW)
        GPIO.output(self.ln2, GPIO.HIGH)
        GPIO.output(self.ln3, GPIO.LOW)
        GPIO.output(self.ln4, GPIO.HIGH)
    def right(self):
        GPIO.output(self.ln1, GPIO.LOW)
        GPIO.output(self.ln2, GPIO.HIGH)
        GPIO.output(self.ln3, GPIO.HIGH)
        GPIO.output(self.ln4, GPIO.LOW)
    def left(self):
        GPIO.output(self.ln1, GPIO.HIGH)
        GPIO.output(self.ln2, GPIO.LOW)
        GPIO.output(self.ln3, GPIO.LOW)
        GPIO.output(self.ln4, GPIO.HIGH)
    def stop(self):
        GPIO.output(self.ln1, GPIO.LOW)
        GPIO.output(self.ln2, GPIO.LOW)
        GPIO.output(self.ln3, GPIO.LOW)
        GPIO.output(self.ln4, GPIO.LOW)
        self.set_speeds(25)
        
    def set_speeds(self, s1, s2=None):
        self.pa.ChangeDutyCycle(s1)
        if s2 is None:
            s2 = s1
        self.pb.ChangeDutyCycle(s2)
    def close(self):
        GPIO.cleanup()