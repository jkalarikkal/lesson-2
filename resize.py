import cv2

image1 = cv2.imread("pika.png")

cv2.imshow("Pika original", image1)

resizedImage = cv2.resize(image1, (300,300))

cv2.imshow("Pika Resize", resizedImage)

cv2.waitKey(0)
cv2.destroyAllWindows