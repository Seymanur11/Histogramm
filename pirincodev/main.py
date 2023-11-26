import cv2
import numpy as np


background = np.zeros((500, 500, 3), dtype=np.uint8)


np.random.seed(42)
for _ in range(10):
    x, y = np.random.randint(50, 450), np.random.randint(50, 450)
    cv2.circle(background, (x, y), 10, (255, 255, 255), -1)


cv2.imwrite("rice_image.jpg", background)

import cv2


image = cv2.imread("rice_image.jpg")


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)


_, labels = cv2.connectedComponents(thresh)
rice_count = len(np.unique(labels)) - 1


cv2.imshow("Original Image", image)
cv2.imshow("Thresholded Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("Pirinç Sayısı:", rice_count)