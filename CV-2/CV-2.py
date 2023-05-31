import cv2 
import numpy as np 

"""
img = np.zeros((512,512,3), np.uint8) #Görüntü oluşturma 

cv2.imshow("Image", img)

cv2.line(img, (0,0), (256,256), (0,255,0), 3) #Çizgi oluşturma
cv2.imshow("Line", img)
 

cv2.rectangle(img, (0,0), (256,256),(0,0,255), cv2.FILLED) #Dörtgen oluşturma
cv2.imshow("Rectangle", img)


cv2.circle(img, (300,300), 45, (255,0,0), cv2.FILLED) #Daire oluşturma
cv2.imshow("Circle", img)


cv2.putText(img, "Put Text", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255)) #Metin oluşturma
cv2.imshow("Put Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread("/Users/furkandurmus/Desktop/Computer Vision/Images/IMG_5055.jpg") #Görseli İçeri Aktarma
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

hor = np.hstack((img, img)) #Yatay Birleştirme 
cv2.imshow("hor", hor)
cv2.waitKey(0)
cv2.destroyAllWindows()


ver = np.vstack((img, img)) #Dikey Birleştirme 
cv2.imshow("ver", ver)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

