import cv2 
import os 

files = os.listdir()

img_path_list = []

for file in files: 
    if file.endswith(".jpg"): 
        img_path_list.append(file)

hog = cv2.HOGDescriptor()

hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for img_path in img_path_list: 
    image = cv2.imread(img_path)

    rects, weight = hog.detectMultiScale(image, padding = (8,8), scale = 1.05)

    for (x,y,w,h) in rects: 
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)  

    cv2.imshow("Pedestrian", image)
    if cv2.waitKey(1) & 0xFF == ord("q"): continue
        
