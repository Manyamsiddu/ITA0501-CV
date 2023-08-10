import cv2
import numpy as np
image_path = 'spidy.png.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)  # Adjust the kernel size as needed
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
black_hat = cv2.subtract(closed_image, image)
cv2.imshow('Original Image', image)
cv2.imshow('Closed Image', closed_image)
cv2.imshow('Black Hat', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
