import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/park.jpg')
blank = np.zeros(img.shape[0:2], dtype=np.uint8)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked_img = cv.bitwise_and(img, img, mask=mask)


cv.imshow('Blank', masked_img)


if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()