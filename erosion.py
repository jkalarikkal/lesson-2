import cv2
import numpy as np
image1 = cv2.imread("pika.png")

cv2.imshow("Pikaa", image1)

kernel = np.ones((5,5), np.uint8)
print(kernel)

image = cv2.erode(image1, kernel)

cv2.imshow("Eroded image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

