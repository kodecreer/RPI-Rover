import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ln1 = 3
ln2 = 4
ln3 = 14
ln4 = 15

temp1 = 1

ena = 2
enb = 18

GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(ln3, GPIO.OUT)
GPIO.setup(ln4, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)

GPIO.output(ln1, GPIO.LOW)
GPIO.output(ln2, GPIO.LOW)
GPIO.output(ln3, GPIO.LOW)
GPIO.output(ln4, GPIO.LOW)

pa = GPIO.PWM(ena, 1000)
pb = GPIO.PWM(enb, 1000)

pa.start(25)
pb.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(ln1,GPIO.HIGH)
         GPIO.output(ln2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(ln1,GPIO.LOW)
         GPIO.output(ln2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(ln1,GPIO.LOW)
        GPIO.output(ln2,GPIO.LOW)
        GPIO.output(ln3, GPIO.LOW)
        GPIO.output(ln4, GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(ln1,GPIO.HIGH)
        GPIO.output(ln2,GPIO.LOW)
        GPIO.output(ln3, GPIO.LOW)
        GPIO.output(ln4, GPIO.HIGH)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(ln1,GPIO.LOW)
        GPIO.output(ln2,GPIO.HIGH)
        GPIO.output(ln3, GPIO.HIGH)
        GPIO.output(ln4, GPIO.LOW)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        pa.ChangeDutyCycle(25)
        pb.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        pa.ChangeDutyCycle(50)
        pb.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        pa.ChangeDutyCycle(100)
        pb.ChangeDutyCycle(100)
        x='z'
     
    elif x == 'tr':
        print('right')
        GPIO.output(ln1, GPIO.LOW)
        GPIO.output(ln2, GPIO.LOW)
        GPIO.output(ln3, GPIO.LOW)
        GPIO.output(ln4, GPIO.HIGH)
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
