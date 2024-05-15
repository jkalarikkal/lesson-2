import cv2

image1 = cv2.imread("Ash.png")
image2 = cv2.imread("pika.png")

subtract = cv2.subtract(image1, image2)

cv2.imshow("SubtractImage", subtract)

cv2.waitKey(0)
cv2.destroyAllWindows()

