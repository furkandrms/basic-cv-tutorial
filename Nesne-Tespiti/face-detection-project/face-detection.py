""" 
In this project, we will be practicing within this module. Face Detection serves as a fundamental project in the field of computer vision. 
Face Detection involves the process of identifying faces in an image or video stream. 
Such techniques find applications in automation, security, games, and numerous other fields.

For our project, we will be utilizing the OpenCV library for face detection. 
OpenCV is a popular and powerful library in the domains of computer vision and image processing. 
The 'haarcascades' repository we're using hosts XML files containing pre-trained data for face detection. 
These files comprise the learned models that will be employed to detect faces.

The objective of the project is to perform face detection on live video or images captured from a camera. 
Upon successful detection, a rectangle will be drawn around each identified face.

This project serves as an excellent introduction for those looking to venture into the 
realm of computer vision and can also form the basis for more complex visual perception projects.

Repo URL =  https://github.com/opencv/opencv/tree/master/data/haarcascades

"""

import cv2 

face_cascade = cv2.CascadeClassifier("/Users/furkandurmus/Desktop/Computer Vision/Nesne-Tespiti-1/face-detection-project/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True: 

    ret, frame = cap.read()

    if ret: 

        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)

        for (x, y, w, h) in face_rect: 

            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 10)

        cv2.imshow("Face Detected", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): 
        
        break 

cap.release()
cv2.destroyAllWindows()

