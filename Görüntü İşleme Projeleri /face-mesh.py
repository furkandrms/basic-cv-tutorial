import cv2
import mediapipe as mp 

cap = cv2.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 2)

mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)




while True: 

    success, img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result =faceMesh.process(imgRGB)

    if result.multi_face_landmarks: 
        for faceLms in result.multi_face_landmarks:

            mpDraw.draw_landmarks(img, faceLms, 
                                  mpFaceMesh.FACEMESH_CONTOURS, 
                                  drawSpec, drawSpec)
            
        for id, lm in enumerate(faceLms.landmark): 

            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)



    cv2.imshow("img", img)
    cv2.waitKey(10)
