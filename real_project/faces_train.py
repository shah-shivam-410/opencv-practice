import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

people_list = []
for i in os.listdir('resources/Faces/train'):
    people_list.append(i)

print(people_list)

DIR = r'E:\Projects\python-projects\opencv-practice\resources\Faces\train'

features = []
labels =[]

haar_cascade = cv.CascadeClassifier('resources/haar_face.xml')

def create_train():
    for person in people_list:
        path = os.path.join(DIR, person)
        label = people_list.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_arr = cv.imread(img_path)
            gray_img = cv.cvtColor(img_arr, cv.COLOR_BGR2GRAY)

            faces_rectangle = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)
            for(x,y,w,h) in faces_rectangle:
                face_roi = gray_img[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)
                # cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

create_train()

# print(f'Length of feature: {len(features)}')
# print(features)
# print(f'Length of label: {len(labels)}')
# print(labels)

# cv.imshow('Feature', features[0])
# if cv.waitKey(10000) & 0xFF == ord('q'):
#     cv.destroyAllWindows()

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)
face_recognizer.save('output/face_trained.xml')
np.save('output/features.npy', features)
np.save('output/labels.npy', labels)