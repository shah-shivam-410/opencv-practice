import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Default', img)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

# Simple Thresholding

threshold, thresh_img = cv.threshold(gray_img, 150, 100, cv.THRESH_BINARY)
print(threshold)
cv.imshow('Thresholt_img', thresh_img)

# Adaptive Thresholding
adaptive_thresh_img = cv.adaptiveThreshold(gray_img, 100, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 101, 10.0)
cv.imshow('adaptive_thresh_img', adaptive_thresh_img)

if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()