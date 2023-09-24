import cv2 as cv


img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Park_colored', img)

# changing filter
gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Park_grayed', gray_img)
cv.imwrite('resources/Photos/park_grey.jpg', gray_img)

# five_img = cv.cvtColor(img, cv.COLOR_RGB2LAB)
# cv.imshow('Park_555', five_img)

# blur
# blurred_img = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Park_blurred', blurred_img)

# Edge cascade
# edge_img = cv.Canny(img, 200, 300)
# cv.imshow('Park_edge', edge_img)

# Dialating - dialate(smoothen) edges of structure image
# dialated_img = cv.dilate(edge_img, (7, 7), iterations=3)
# cv.imshow('Park_dialated', dialated_img)

# Eroding - get back structure edge from dialated image
# eroded_img =cv.erode(dialated_img, (7, 7), iterations=3)
# cv.imshow('Park_eroded', eroded_img)

# Resize
# resized_img = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Park_resized', resized_img)

# Crop the image
# Numpy array slicing: element[start_y:end_y, start_x:end_x]     --- x = column, y = row
# cropped_img = img[100:200, 400:600]
# cv.imshow('Park_cropped', cropped_img)


if cv.waitKey(10000) & 0xFF == ord('q'):
    cv.destroyAllWindows()