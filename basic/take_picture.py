import cv2

# Reading webcam and taking picture
capture = cv2.VideoCapture(0)
while True:
    frameReceived, frame = capture.read()
    if not frameReceived:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        cv2.imwrite('resources/Photos/my_photo.jpg', frame)
        break

capture.release()
cv2.destroyAllWindows()