import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/cats.jpg')
cv.imshow('Default', img)
# print(img.shape)

# avg_blur = cv.blur(img, (3,3))
# cv.imshow('Blurred', avg_blur)

# gausian_blur = cv.GaussianBlur(img, (3,3), 0)
# cv.imshow("Gausian_blur", gausian_blur)

# median_blur = cv.medianBlur(img, 3)
# cv.imshow("median_blur", median_blur)

bilateral_blur = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("bilateral_blur", bilateral_blur)

if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()