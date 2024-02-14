import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/park.jpg')
# cv.imshow('Default', img)
plt.imshow(img)
plt.show()


# Gray scale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# HSY scale
# HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', HSV)

# RGB scale
# RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', RGB)

# LAB scale
# LAB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('LAB', RGB)

# if cv.waitKey(10000) & 0xFF == ord('q'):
#     cv.destroyAllWindows()