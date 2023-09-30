import cv2 as cv
import numpy as np

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Park_colored', img)

# Translation
def translate(img, x, y):
    '''
    +x --> right, -x --> left
    +y --> down, -y --> up
    '''
    trans_mat = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])
    dimensation = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensation)

# trans_img = translate(img, -200, 300)
# cv.imshow('Park_Translated', trans_img)


# Rotation
def rotate(img, angle, rotation_point=None):
    (height, width) = img.shape[:2]
    if rotation_point  == None:
        rotation_point = (width//2, height//2)
    rotated_mat = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensation= (width, height)
    return cv.warpAffine(img, rotated_mat, dimensation)

# rotated_img = rotate(img, 90)
# cv.imshow('Park_rotated', rotated_img)

# rotated_img2 = rotate(rotated_img, 45)
# cv.imshow('Park_rotated2', rotated_img2)


# Resizing
# resized_img = cv.resize(img, (1000, 1000), interpolation=cv.INTER_CUBIC)
# cv.imshow('Park_resized', resized_img)

# Flipping
# cv.imshow('Park_flipped_verticle', cv.flip(img, 0))
# cv.imshow('Park_flipped_horizantal', cv.flip(img, 1))
# cv.imshow('Park_flipped_verticle_horizantal', cv.flip(img, -1))


# Cropping
# Numpy array slicing: element[start_y:end_y, start_x:end_x]     --- x = column, y = row
# cv.imshow('Park_cropped', img[0:100, 0:400])


if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()