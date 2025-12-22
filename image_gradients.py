import cv2
import numpy as np

image = cv2.imread("data/bricks_2.png", 0)

# Laplacian
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Sobel
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

laplacian = np.absolute(laplacian).astype(np.uint8)
sobelx = np.absolute(sobelx).astype(np.uint8)
sobely = np.absolute(sobely).astype(np.uint8)

combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

cv2.imshow("Original", image)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("SobelX", sobelx)
cv2.imshow("SobelY", sobely)
cv2.imshow("Combined", combined)
cv2.waitKey(0)