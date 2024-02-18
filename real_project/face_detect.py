import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/group 2.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Default', gray_img)

haar_cascade = cv.CascadeClassifier('resources/haar_face.xml')
faces_rectangle = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)

# print(haar_cascade)
print(len(faces_rectangle))

for(x,y,w,h) in faces_rectangle:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Default', img)


if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()