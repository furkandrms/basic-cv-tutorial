import cv2
import tensorflow as tf
import numpy as np
import os

# Duygu etiketlerini tanımlayın
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Duygu tanıma modelini yükleyin
model = tf.keras.models.load_model('/Users/furkandurmus/Desktop/Computer Vision/face-emotion/emotionModel.hdf5')

# Yüz tespiti için Cascade sınıflandırıcısını yükleyin
cascade_path = '/Users/furkandurmus/Desktop/Computer Vision/face-emotion/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Video akışını başlatın
cap = cv2.VideoCapture("/Users/furkandurmus/Desktop/Computer Vision/face-emotion/example_video.mp4")  # 0, yerleşik kamera için kullanılan indeks

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (64, 64), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = np.expand_dims(roi, axis=0)
            roi = np.expand_dims(roi, axis=3)

            # Duygu tahminini yap
            preds = model.predict(roi)[0]
            label = emotions[np.argmax(preds)]
            label_position = (x, y)
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Çerçeveyi göster
    cv2.imshow('Emotion Detection', frame)

    # Çıkış için "q" tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
