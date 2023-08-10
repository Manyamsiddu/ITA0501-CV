import cv2
import numpy as np

# Load the image
image_path = 'spidy.png.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to create a blurred version of the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 2)

# Calculate the high-pass image (original image - blurred image)
high_pass_image = cv2.subtract(image, blurred_image)

# Define a scaling factor to control the strength of sharpening
scaling_factor = 2.0

# Calculate the high-boost mask (scaled high-pass image)
high_boost_mask = cv2.multiply(high_pass_image, scaling_factor)

# Combine the high-boost mask with the original image
sharpened_image = cv2.add(image, high_boost_mask)

# Display the original image, blurred image, high-pass image, high-boost mask, and sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('High-Pass Image', high_pass_image)
cv2.imshow('High-Boost Mask', high_boost_mask)
cv2.imshow('Sharpened Image (High-Boost)', sharpened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
