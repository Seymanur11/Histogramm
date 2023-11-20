import cv2
import numpy as np


lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])


video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()
    if not ret:
        break


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, lower_red, upper_red)


    result = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow("Original", frame)
    cv2.imshow("Result", result)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()