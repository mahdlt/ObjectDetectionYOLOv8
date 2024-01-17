import cv2

# Read the image
image_path = 'clock.jpg'
image = cv2.imread(image_path)

# Define the coordinates of the bounding box (x, y, width, height)
bbox = (300, 75, 400, 610)

# Extract the coordinates
x, y, w, h = bbox

# Draw a bounding box on the image
color = (0, 255, 0)  # Green color for the bounding box
thickness = 2
cv2.rectangle(image, (x, y), (x + w , y + h), color, thickness)

# Add text to the edge of the bounding box
text = "clock 400*610"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
text_color = (255, 255, 255)  # White color for the text
text_thickness = 1
text_size = cv2.getTextSize(text, font, font_scale, text_thickness)[0]
cv2.putText(image, text, (x, y - 10), font, font_scale, text_color, text_thickness)

# Show the image with bounding box and text
cv2.imshow('Image with Bounding Box', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
# this is a comment for new commit
# another change