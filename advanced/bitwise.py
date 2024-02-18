import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

blank = np.zeros((400,400), dtype=np.uint8)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 190, 255, -1)

bitwise_and = cv.bitwise_and(rectangle, circle) # Intersecting
bitwise_or = cv.bitwise_or(rectangle, circle) # Intersectiing and Non-Intersecting
bitwise_xor = cv.bitwise_xor(rectangle, circle) # Non-Intersecting
bitwise_not = cv.bitwise_not(circle) # Complement

cv.imshow("Blank", bitwise_xor)

if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()