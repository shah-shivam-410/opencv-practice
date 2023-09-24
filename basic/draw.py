import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# Painting blank image

# Specific portion of image
# blank[:] = 50,0,50
# blank[200:300, 300:400] = 0, 0, 255
# blank[200:300, 200:300] = 0, 0, 255

# Rectangle
# cv.rectangle(blank, (200, 200), (300, 300), (255, 0, 0), thickness=2)
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=cv.FILLED)

# Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0, 0, 255), thickness=cv.FILLED) 

# Line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=2, lineType=cv.LINE_4)

# Text
cv.putText(blank, 'Hello OpenCV', (100, 375), cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0))

cv.imshow('Drawing', blank)
if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()