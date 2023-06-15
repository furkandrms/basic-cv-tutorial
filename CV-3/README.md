
```markdown
# Computer Vision İşlemleri

Bu proje, temel Computer Vision işlemlerini gerçekleştirmek için Python kullanarak oluşturulmuştur. Aşağıda, projede kullanılan işlemleri ve ilgili yöntemleri bulabilirsiniz.

## Gereksinimler

- Python 3.x
- OpenCV kütüphanesi

## Görüntüleri Eşikleme

Görüntü eşikleme, bir görüntüdeki pikselleri belirli bir eşik değeriyle karşılaştırarak bir bölgenin parlaklık veya renk özelliklerine dayalı olarak sınıflandırmaktır. İşte bir örnek:

import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('image.jpg', 0)

# Eşik değerini belirleme
threshold_value = 128

# Görüntüyü eşikleme
_, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
```

## Görüntü Bulanıklaştırma

Görüntü bulanıklaştırma, bir görüntüdeki detayları azaltarak görüntüyü yumuşatma işlemidir. İşte bir örnek:

```python
import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('image.jpg')

# Görüntüyü bulanıklaştırma
blurred_image = cv2.blur(image, (5, 5))
```

## Gradyan Oluşturma

Gradyan oluşturma, bir görüntüdeki kenarları veya yoğunluk değişikliklerini vurgulamak için kullanılır. İşte bir örnek:

```python
import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('image.jpg', 0)

# Gradyanları hesaplama
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Gradyanları birleştirme
gradient_magnitude = cv2.addWeighted(np.absolute(gradient_x), 0.5, np.absolute(gradient_y), 0.5, 0)
```

## Histogramlar

Histogram, bir görüntüdeki piksellerin yoğunluk veya renk değerlerinin dağılımını gösteren bir grafiktir. İşte bir örnek:

```python
import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükleme
image = cv2.imread('image.jpg', 0)

# Histogramı hesaplama
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Histogramı görselleştirme
plt.plot

(histogram)
plt.xlabel('Piksel Değerleri')
plt.ylabel('Piksel Sayısı')
plt.show()
```

## Morfolojik Operasyonlar

Morfolojik operasyonlar, bir görüntüdeki şekil veya yapıyı değiştirmek veya vurgulamak için kullanılan temel işlemlerdir. İşte bir örnek:

```python
import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('image.jpg', 0)

# Yapısal elemanı oluşturma
kernel = np.ones((5, 5), np.uint8)

# Genişletme işlemi
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Aşındırma işlemi
eroded_image = cv2.erode(image, kernel, iterations=1)
```


