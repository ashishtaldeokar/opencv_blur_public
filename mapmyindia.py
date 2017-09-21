import numpy as np
import cv2

faces = []

faces.append(cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml'))
faces.append(cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml'))
faces.append(cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt2.xml'))
faces.append(cv2.CascadeClassifier('./haarcascades/haarcascade_profileface.xml'))
faces.append(cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml'))

plates = []
plates.append(cv2.CascadeClassifier('./haarcascades/haarcascade_russian_plate_number.xml'))
plates.append(cv2.CascadeClassifier('./haarcascades/haarcascade_licence_plate_rus_16stages.xml'))

img = cv2.imread('peds2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# plates = number_plate.detectMultiScale(gray, 1.3, 5)
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for cascade in faces:
    face = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in face:
        roi_color = img[y:y+h, x:x+w]
        sub_face = cv2.GaussianBlur(roi_color,(23, 23), 30)
        # merge this blurry rectangle to our final image
        img[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

for cascade in plates:
    plate = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in plate:
        roi_color = img[y:y+h, x:x+w]
        sub_plate = cv2.GaussianBlur(roi_color,(23, 23), 30)
        # merge this blurry rectangle to our final image
        img[y:y+sub_plate.shape[0], x:x+sub_plate.shape[1]] = sub_plate
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]


cv2.imwrite('output2.jpg', img)
