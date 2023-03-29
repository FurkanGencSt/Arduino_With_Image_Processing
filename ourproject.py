import cv2
import numpy as np

# Kamerayı aç
capture = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü oku
    ret, frame = capture.read()

    # Görüntüyü BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mor renk için bir maske oluştur
    lower_purple = np.array([130, 50, 50])
    upper_purple = np.array([170, 255, 255])

    # İki maskeyi birleştir
    mask = cv2.inRange(hsv, lower_purple, upper_purple)

    # Maskenin alanını hesapla
    area = cv2.countNonZero(mask)

    # Ekranda mor renk algılandığında "bulundu" yazdır
    if area > 10000:
        print("bulundu")

    # Görüntüyü göster
    cv2.imshow("Kamera Görüntüsü", frame)

    # Q tuşuna basarak programı sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
capture.release()

# Pencereleri kapat
cv2.destroyAllWindows()
