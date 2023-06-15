```markdown
# Computer Vision İşlemleri

Bu proje, temel Computer Vision işlemlerini gerçekleştirmek için Python kullanarak oluşturulmuştur. Aşağıda, projede kullanılan işlemleri ve ilgili methodları bulabilirsiniz.

## Gereksinimler

- Python 3.x
- OpenCV kütüphanesi

## Görsel İçeri Aktarma

Görüntü işleme işlemlerine başlamadan önce, bir görüntüyü yüklemeniz gerekebilir. İşte bir görüntüyü içeri aktarma işlemi:

```python
import cv2

# Görüntüyü yükleme
image = cv2.imread('image.jpg')
```

## Video İçeri Aktarma

Bir videoyu işlemek istiyorsanız, videoyu içeri aktarmanız gerekecektir. İşte bir videoyu içeri aktarma işlemi:

```python
import cv2

# Videoyu açma
video = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = video.read()
    
    if not ret:
        break

    # Frame üzerinde işlemler yapın

    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```

## Kamera Açma ve Video Kaydı Yapma

Kamerayı kullanarak gerçek zamanlı görüntü işleme yapmak ve video kaydetmek istiyorsanız, kamera açma ve video kaydı yapma işlemlerini kullanabilirsiniz:

```python
import cv2

# Kamerayı açma
camera = cv2.VideoCapture(0)

# Video kaydedici tanımlama
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = camera.read()
    
    if not ret:
        break

    # Frame üzerinde işlemler yapın

    cv2.imshow('Kamera', frame)
    output.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
output.release()
cv2.destroyAllWindows()
```

## Yeniden Boyutlandırma ve Kırpma

Görüntüyü yeniden boyutlandırma ve kırpma işlemleri, görüntüleri belirli boyutlara getirmek veya belirli bölgeleri seçmek için kullanılabilir:

```python
import cv2

# Görüntüyü yeniden boyutlandırma
resized_image = cv2.resize(image, (new_width, new_height))

# Görüntüyü kırpmak
cropped_image = image[y:y+h, x:x+w]
```

Bu dökümanda, temel Computer Vision işlemlerini Python dilinde nasıl gerçekleştireceğinizi bulabilirsiniz. Daha fazla işlem için OpenCV dokümantasyonunu inceleyebilirsiniz.

