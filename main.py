# John Henke
# EDNS 151 Computer Vision Subsystem

import cv2
import numpy as np
import shotgun_hole_detector
import color_detector

print("Pine Beetle CV Detection System.")
while True:
    print("1) Shotgun Hole Recognition.")
    print("2) Pine Needle Color Simulator.")
    print("3) Quit.")
    print("Choose an option from the list above.")
    user_choice = input("Choice> ")
    if user_choice == '1':
        print("You have chosen to identify shotgunholes. Please input an image that depicts the tree's trunk.")
        print("Input name of the file to be read, including the file extension, e.g. 'image.jpg'")
        file = input("File> ")
        shotgun_hole_detector.detect_shotgun_holes(file)

    elif user_choice == '2':
        print("You have chosen to identify color. Please input an image file that depicts the tree's needles.")
        file = input("File> ")
        color_detector.detect_color(file)

    elif user_choice == '3':
        break

    else:
        print("I didn't understand that option. Please input a valid option.")


