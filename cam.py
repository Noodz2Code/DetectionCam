import cv2
import time
import datetime

#set on which camera to record using cv2.VideoCapture() method
camera = cv2.VideoCapture(0)

#add detection to face and body
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

while True:
    _, frame = camera.read()    #read the frame and display

    #change frame color to gray
    disp_color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #to detect face and body, set detectection speed with detectMultiScale() method
    faces = face_detector.detectMultiScale(disp_color, 1.1, 5)
    body = body_detector.detectMultiScale(disp_color, 1.2, 5)

    #draw a rectangle near the object if detected
    #for face
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 3)

    #for body
    for (x, y, width, height) in body:
        cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 3)

    cv2.imshow("Camera", frame)

    #way to quit the program, which ord('q') shows which key to press to quit
    if cv2.waitKey(1) == ord('q'):
        break

camera.release() 