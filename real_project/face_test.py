import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

haar_cascade = cv.CascadeClassifier('resources/haar_face.xml')

# features = np.load('output/features.npy', allow_pickle=True)
# labels = np.load('output/labels.npy', allow_pickle=True)

peoples = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('output/face_trained.xml')

img = cv.imread(r'E:\Projects\python-projects\opencv-practice\resources\Faces\val\madonna\2.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces_rectangle = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)
for(x,y,w,h) in faces_rectangle:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    face_roi = gray_img[x:x+w, y:y+h]
    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {peoples[label]} with confidence = {confidence}')
    cv.putText(img, peoples[label], (x, y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)

cv.imshow('Detected_face', img)
cv.waitKey(0)