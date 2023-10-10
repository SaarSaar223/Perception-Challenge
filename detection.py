import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img_path = "red.png"
img = cv2.imread(img_path)
img_height, img_width, _ = img.shape

# Convert the image to RGB format
img_in_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define color thresholds to identify red cones
threshold_low = np.array([150, 0, 0], dtype="uint8")
threshold_high = np.array([245, 40, 40], dtype="uint8")
img_threshold = cv2.inRange(img_in_color, threshold_low, threshold_high)

# Apply median blur to reduce noise
img_blurred = cv2.medianBlur(img_threshold, 5)

# Apply Canny edge detection (returns pixels)
img_borders = cv2.Canny(img_blurred, 80, 160)

# Find contours in the edge-detected image (returns curves)
contours, _ = cv2.findContours(
    np.array(img_borders), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Sort contours by area and keep the largest 14 for the 14 cones in the image
contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)[:14]

# Separate contours into left and right based on x-coordinate
contours_left = []
contours_right = []

for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        if cX < img_width / 2:
            contours_left.append(contour)
        else:
            contours_right.append(contour)

# Draw contours on the original image
cv2.drawContours(img_in_color, contours_left, -1, (0, 255, 0), 2)
cv2.drawContours(img_in_color, contours_right, -1, (0, 255, 0), 2)

# Fit lines to the contours using fitLine
line_params_left = cv2.fitLine(
    np.concatenate(contours_left), cv2.DIST_L2, 0, 0.01, 0.01
)
line_params_right = cv2.fitLine(
    np.concatenate(contours_right), cv2.DIST_L2, 0, 0.01, 0.01
)

# Calculate line endpoints
x1_left, y1_left = int(line_params_left[2] - 1000 * line_params_left[0]), int(
    line_params_left[3] - 1000 * line_params_left[1]
)
x2_left, y2_left = int(line_params_left[2] + 1000 * line_params_left[0]), int(
    line_params_left[3] + 1000 * line_params_left[1]
)

x1_right, y1_right = int(line_params_right[2] - 1000 * line_params_right[0]), int(
    line_params_right[3] - 1000 * line_params_right[1]
)
x2_right, y2_right = int(line_params_right[2] + 1000 * line_params_right[0]), int(
    line_params_right[3] + 1000 * line_params_right[1]
)

# Draw lines through contours_left and contours_right
cv2.line(img_in_color, (x1_left, y1_left), (x2_left, y2_left), (0, 255, 0), 3)
cv2.line(img_in_color, (x1_right, y1_right), (x2_right, y2_right), (0, 255, 0), 3)

# Display the result using matplotlib
plt.imshow(img_in_color)
plt.show()

# cv2.imwrite("answer.png", cv2.cvtColor(img_in_color, cv2.COLOR_RGB2BGR))
