import cv2 
import time 
import mediapipe as mp 

cap = cv2.VideoCapture("/Users/furkandurmus/Desktop/Computer Vision/Videos/video1.mp4")

mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils

while True: 
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = pose.process(imgRGB)
    print(result.pose_landmarks)

    if result.pose_landmarks: 
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)



    cv2.imshow("img", img)
    cv2.waitKey(50)