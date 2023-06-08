import cv2 
import mediapipe as mp 

cap = cv2.VideoCapture(0)

mpFD = mp.solutions.face_detection
face_detection = mpFD.FaceDetection()

mpDraw = mp.solutions.drawing_utils



while True: 

    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    result = face_detection.process(imgRGB) 

    if result.detections: 
        for id, detection in enumerate(result.detections): 

            bboxC = detection.location_data.relative_bounding_box

            h, w, _  = img.shape 

            bbox = int(bboxC.xmin*w),  int(bboxC.ymin*h), int(bboxC.width*w), int(bboxC.height*h) 

            cv2.rectangle(img, bbox, (0,0,255), 2)






    cv2.imshow("img", img)
    cv2.waitKey(1)