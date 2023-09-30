import cv2 as cv
import numpy as np


img = cv.imread('resources/Photos/cats 2.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank_img = np.zeros(img.shape, np.uint8)
# cv.imshow('Blank', blank_img)

# Using canny edge ditector
edges = cv.Canny(img, 200, 200)
cv.imshow('Edge', edges)
# Using threshold
# ret, thresh_img = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh_img)

contours, hierarchies = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'No. of contours found: {len(contours)}')

cv.drawContours(blank_img, contours, -1, (0, 0, 255), 2)
cv.imshow('Contours', blank_img)


# cv.imshow('Cats', edges)
if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()