import cv2
import time
import datetime

#main camera
class OpenCamera():
    #set on which camera to record using cv2.VideoCapture() method
    camera = cv2.VideoCapture(0)

    #add detection to face and body
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")


class DetectionCam(OpenCamera):

    #check frame size for recorded video
    frame_size = (int(OpenCamera().camera.get(3)), int(OpenCamera().camera.get(4)))

    #save recording as mp4
    save_record = cv2.VideoWriter_fourcc(*"mp4v")

    output = cv2.VideoWriter("sample_video.mp4", save_record, 20.0, frame_size, True)

    while True:
        _, frame = OpenCamera().camera.read()    #read the frame and display

        #change frame color to gray
        disp_color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #to detect face and body, set detectection speed with detectMultiScale() method
        faces = OpenCamera().face_detector.detectMultiScale(disp_color, 1.1, 5)
        body = OpenCamera().body_detector.detectMultiScale(disp_color, 1.2, 5)    
        
        output.write(frame)

        output.release()

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

    OpenCamera().camera.release() 
    cv2.destroyAllWindows()

#to record
class recordFrame(DetectionCam):
    #start recording
    record = True

#main
def main():
    OpenCamera()
    DetectionCam()
    recordFrame()

main()