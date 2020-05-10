import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (20, 20), (500, 500), (255, 0, 0), thickness=2)
cv2.line(img, (500, 20), (20, 500), (255, 0, 0), thickness=2)

cv2.rectangle(img, (20, 20), (400, 400), (0, 255, 0), thickness=4)
cv2.rectangle(img, (24, 24), (396, 396), (0, 0, 255), thickness=cv2.FILLED)

cv2.imshow("zeroes", img)
cv2.waitKey(0)

