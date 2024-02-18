import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Default', img)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

# Laplacian
lap = cv.Laplacian(gray_img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplace', lap)

# Sobel
sobel_x = cv.Sobel(gray_img, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray_img, cv.CV_64F, 0, 1)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)

combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('combined_sobel', combined_sobel)

# Canny
canny = cv.Canny(gray_img, 150, 175)
cv.imshow('Canny', canny)

if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()