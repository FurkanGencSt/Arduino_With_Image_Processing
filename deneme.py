import cv2

# Kamerayı aç
cap = cv2.VideoCapture(0)

# Yüz tanıma özelliği için bir nesne oluştur
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()

    # Görüntüyü siyah beyaz olarak dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # Tespit edilen yüzlerin koordinatlarına göre dikdörtgen çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow('frame', frame)

    # q tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
cap.release()

# Pencereleri kapat
cv2.destroyAllWindows()
