import cv2 as cv


def rescaleframe(frame, scalefactor=0.4):
    # for standalone video and images
    width = int(frame.shape[1] * scalefactor)
    height = int(frame.shape[0] * scalefactor)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def change_resolution(capture, width, height):
    # only for live video
    capture.set(3, width)
    capture.set(4, height)
    return capture


# img = cv.imread('../resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.imshow('Resized image', rescaleframe(img, 0.1))
# if cv.waitKey(10000) & 0xFF == ord('q'):
#     cv.destroyAllWindows()


capture = cv.VideoCapture(0)
capture = change_resolution(capture, 500, 500)
while True:
    frameReceived, frame = capture.read()
    if not frameReceived:
        break
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
