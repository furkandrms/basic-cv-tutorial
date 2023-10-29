import cv2
import os 

files = os.listdir()

img_path_list = []

for file in files: 
    if file.endswith(".jpg"): 
        img_path_list.append(file)


for i in img_path_list: 
    image = cv2.imread(i)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = cv2.CascadeClassifier("/Users/furkandurmus/Desktop/Computer Vision/Nesne-Tespiti-1/Cat Detection/haarcascade_frontalcatface.xml")
    face_detect = detector.detectMultiScale(gray, scaleFactor = 1.045, minNighbors = 2) 

    for (j, (x,y,w,h)) in enumerate(face_detect): 
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,255), 2)
        cv2.putText(image, "Kedi {}".format(j+1), (x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,255,255),2)
    
    cv2.imshow(i, image)
    if cv2.waitKey(0) & 0xFF == ord("q"): continue




