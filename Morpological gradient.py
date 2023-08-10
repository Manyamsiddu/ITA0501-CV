import cv2
import numpy as np
image_path = 'spidy.png.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=1)
eroded_image = cv2.erode(image, kernel, iterations=1)
morphological_gradient = cv2.subtract(dilated_image, eroded_image)
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Morphological Gradient', morphological_gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
