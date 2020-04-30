import cv2
import numpy as np


def detect_color(file):
    # Read in the image.
    image = cv2.imread(file)

    # image = np.flip(imgaxis=1)

    # Convert the image from BGR to HSV color space (from red green blue/blue green red to hue saturation value). It is
    # not possible to only use RGB to detect color since the lighting will be constantly changing. To avoid the
    # mixing of chrominance (color related information) and luminance (intensity related information) data we need to
    # use HSV.
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # First we look for red.
    # Range for red; The first parameter is the hue, the second is the saturation, the third is the value.
    lower_red = np.array([0, 50, 20])
    upper_red = np.array([20, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    cv2.imshow("Test", mask1)
    cv2.waitKey(0)
    total_pixels = mask1.size
    detected_pixels = np.count_nonzero(mask1)
    percentage = (detected_pixels * 100 / total_pixels)
    print("Detected pixels:", detected_pixels)
    print("Total pixels:", total_pixels)
    print("Percentage of detected pixels: %2.2f %% " % percentage)
    if percentage > 2:
        print("Infestation identified.")
    else:
        print("No infestation detected.")
    # I am currently thinking if the detected > 0.5%, then it will be labeled positive for infestation.
    # 0.5 % sounds really low, but the program is amazing about not returning false positives where there is no red.
    # What about background stuff that could be red? Maybe 1-5% would be better. or 5-10%. needs additional testing.

