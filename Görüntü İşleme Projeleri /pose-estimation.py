import cv2 
import time 
import mediapipe as mp 

cap = cv2.VideoCapture("/Users/furkandurmus/Desktop/Computer Vision/Videos/video1.mp4")

mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils

pTime = 0

while True: 
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = pose.process(imgRGB)
    print(result.pose_landmarks)

    if result.pose_landmarks: 
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(result.pose_landmarks.landmark): 
            h, w, _ = img.shape

            cx, cy = int(lm.x*w), int(lm.y*h)

            if id == 5: 
                cv2.circle(img, (cx, cy), 6, (0,255,0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, "FPS" + str(int(fps)), (10,65), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,0,255))
    cv2.imshow("img", img)
    cv2.waitKey(50)