
```markdown
# Computer Vision İşlemleri

Bu proje, temel Computer Vision işlemlerini gerçekleştirmek için Python kullanarak oluşturulmuştur. Aşağıda, projede kullanılan işlemleri ve ilgili methodları bulabilirsiniz.

## Gereksinimler

- Python 3.x
- OpenCV kütüphanesi

## Görüntü Oluşturma Ve Şekil Çizdirme

Görüntü işleme işlemlerinde bazen yeni görüntüler oluşturmanız ve üzerlerinde şekiller çizdirmeniz gerekebilir. İşte bir örnek:

import cv2
import numpy as np

# Siyah bir görüntü oluşturma
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Kırmızı bir dikdörtgen çizdirme
cv2.rectangle(image, (100, 100), (400, 400), (0, 0, 255), 2)

# Yeşil bir daire çizdirme
cv2.circle(image, (250, 250), 100, (0, 255, 0), -1)
```

## Görseli Yatay Ve Dikey Birleştirme

Birçok durumda, farklı görüntüleri yatay veya dikey olarak birleştirmeniz gerekebilir. İşte bir örnek:

```python
import cv2
import numpy as np

# İlk görüntüyü yükleme
image1 = cv2.imread('image1.jpg')

# İkinci görüntüyü yükleme
image2 = cv2.imread('image2.jpg')

# Görüntüleri yatay birleştirme
horizontal_stack = np.concatenate((image1, image2), axis=1)

# Görüntüleri dikey birleştirme
vertical_stack = np.concatenate((image1, image2), axis=0)
```

## Görsel Perspektif Düzeltme

Perspektif düzeltme işlemi, bir görüntünün perspektif etkilerini gidermek için kullanılır. İşte bir örnek:

```python
import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('image.jpg')

# Görüntü üzerinde dört nokta belirleme (perspektif dönüşümünü belirlemek için)
points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.float32)

# Hedef dört noktayı belirleme (düzeltilecek perspektifi belirlemek için)
target_points = np.array([[0, 0], [300, 0], [300, 300], [0, 300]], dtype=np.float32)

# Perspektif dönüşüm matrisini hesaplama
perspective_matrix = cv2.getPerspectiveTransform(points, target_points)

# Görüntüyü perspektif dönü

şümü uygulayarak düzeltme
perspective_corrected_image = cv2.warpPerspective(image, perspective_matrix, (300, 300))
```

## Görüntü Birleştirme

Görüntü birleştirme işlemi, farklı görüntülerin birleştirilerek tek bir panoramik görüntü oluşturulmasını sağlar. İşte bir örnek:

```python
import cv2
import numpy as np

# İlk görüntüyü yükleme
image1 = cv2.imread('image1.jpg')

# İkinci görüntüyü yükleme
image2 = cv2.imread('image2.jpg')

# Görüntüler arasında özelliklerin eşleştirilmesi
# ...

# Görüntüleri birleştirme
result = cv2.merge((image1, image2))
```

