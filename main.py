from car_cls import Car
import RPi.GPIO as GPIO
import time
import cv2

GPIO.setmode(GPIO.BCM)

ln1 = 3
ln2 = 4
ln3 = 14
ln4 = 15

ena = 2
enb = 18

def main():
    car = Car(ln1, ln2, ln3, ln4, ena, enb)
    camera = cv2.VideoCapture(0)
    key = 0
    while key != 27:
        ok, frame = camera.read()
        if ok:
            cv2.imshow('view', frame)
            key = cv2.waitKey(1)
            if key == ord('w'):
                car.forward()
            elif key == ord('s'):
                car.backward()
            elif key == ord('a'):
                car.left()
            elif key == ord('d'):
                car.right()
            elif key == ord('p'):
                car.stop()
            elif key == 49:
                car.set_speeds(50)
            elif key == 50:
                car.set_speeds(75)
            elif key == 51:
                car.set_speeds(100)
    camera.release()
    cv2.destroyAllWindows()
    car.close()
if __name__ == "__main__":
    try:
        main()
    except:
        GPIO.cleanup()