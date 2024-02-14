import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Default', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# print(f"Shape= img:{img.shape} Blue:{b.shape} Green:{g.shape} Red:{r.shape}")

# merged_img = cv.merge([b,g,r])
# cv.imshow('Merged', merged_img)

# b = cv.merge([b, blank, blank])
# g = cv.merge([blank, g, blank])
# r = cv.merge([blank, blank, r])

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# b_g = cv.merge([b, g, blank])
# cv.imshow('Blue_Green', b_g)

if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()