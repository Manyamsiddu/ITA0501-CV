import cv2
import numpy as np

# Load the main image and the watermark
main_image_path = 'cap.jpg.jpg'
watermark_path = 'spidy.png.jpg'

main_image = cv2.imread(main_image_path)
watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

# Get dimensions of main image and watermark
main_height, main_width, _ = main_image.shape
watermark_height, watermark_width, _ = watermark.shape

# Calculate the position to place the watermark in the center
position_x = (main_width - watermark_width) // 2
position_y = (main_height - watermark_height) // 2

# Create an overlay region for the watermark
overlay = main_image.copy()
overlay[position_y:position_y+watermark_height, position_x:position_x+watermark_width] = watermark

# Blend the overlay with the main image using transparency
alpha = 0.7  # Change this to control the transparency level
watermarked_image = cv2.addWeighted(main_image, 1, overlay, alpha, 0)

# Display the watermarked image
cv2.imshow('Watermarked Image', watermarked_image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
