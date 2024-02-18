import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/Photos/cats.jpg')
cv.imshow('Default', img)

blank = np.zeros(img.shape[0:2], dtype=np.uint8)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked_img)

# Gray histogram

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# cv.imshow('Default', gray)

# plt.figure()
# plt.title("Gray-Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No. of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.grid(True)
# plt.show()

# Color Histogram

plt.figure()
plt.title("Gray-Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
plt.xlim([0,256])
plt.grid(True)

colors= ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist)

plt.show()

if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()