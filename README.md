# Perception-Challenge

Project to solve the coding challenge of Wisconsin Autonomous 
Submitted by: Saarthak Aggarwal (saggarwal29@wisc.edu)


# Answer Image

![answer](https://github.com/SaarSaar223/Perception-Challenge/assets/92472323/4b9d507a-03ba-4c1f-aa19-dec5c310e383)

# Methodology 

1. **Load and Convert Image:** Load the input image and convert it from BGR to RGB format for compatibility.
2. **Define Red Color Range:** Define a color range in RGB to identify red cones.
3. **Color Thresholding:** Create a binary mask to isolate pixels within the red color range.
4. **Edge Detection:** Apply Canny edge detection to identify edges in the binary mask.
5. **Contour Extraction:** Find and extract contours from the edge-detected image.
6. **Draw Contours and Fit Lines:** Draw contours around detected objects (red cones) and fit lines to represent their central axes.
7. **Display the Result:** Display the original image with drawn contours and central axis lines using Matplotlib.

This methodology was inspired by https://www.youtube.com/watch?v=Y7SkyY58aUw&ab_channel=ChrisDahms

# What did you try and why do you think it did not work?

As this was my first time working with openCV, I had to try a range of different methods and techniques to detect the cones in the image. However, once I found the youtube video, I was able to gain a starting point in order to complete the code. One thing that I had to try multiple times was how to set the range of the threshholds used to detect the cones and the way to blur the noise in the background. I also had to look deeply into how the code separates contours into "left" and "right" based on their positions. If the image contains red cones on both sides, this logic should correctly distinguish between them. If the separation logic is incorrect, it may not accurately draw lines through the center axes of the cones. By thoroughly inspecting and possibly adjusting these aspects of the code, it's possible to improve its accuracy and ensure it works as intended for a variety of images containing red cones.

# Requirements

opencv-python
numpy
matplotlib
