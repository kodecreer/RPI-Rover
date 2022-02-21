import cv2
import zmq
import base64
from car import car 


context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')

camera = cv2.VideoCapture(0)  # init the camera

while True:

        (grabbed, frame) = camera.read()  # grab the current frame
        if grabbed:
            grabbed, frame = camera.read()  # grab the current frame
            frame = cv2.resize(frame, (640, 480))  # resize the frame
            encoded, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer)
            footage_socket.send(jpg_as_text)
        key = cv2.waitKey(1)
        if key == 27:
            camera.release()
            cv2.destroyAllWindows()
            print ("\n\nBye bye\n")
            break
        elif key == ord('w'):
            car.forward()
        elif key == ord('s'):
            car.backward()