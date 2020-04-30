import cv2
import numpy as np


def detect_shotgun_holes(file):
    # Read in one image as grayscale
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    # To read in a video use the line below.
    # camera = cv2.VideoCapture(file) --> have to put in the correct avi or mp4 file.

    # Set up BlobDetector
    detector = cv2.SimpleBlobDetector_create()
    parameters = cv2.SimpleBlobDetector_Params()

    # Filter by Area
    parameters.filterByArea = True
    parameters.minArea = 25
    parameters.maxArea = 400000

    # Filter by Threshholds
    parameters.minThreshold = 1

    # This code below would make it choose darker blobs, but there is a logical error within the library.
    # # Filter by Color
    # parameters.filterByColor = 1
    # parameters.blobColor = 0

    # Filter by Circularity
    parameters.filterByCircularity = True
    parameters.minCircularity = 0.7

    # Filter by Convexity (what is this?)
    parameters.filterByConvexity = True
    parameters.minConvexity = 0.9

    # Filter by Inertia. Basically how elongated they are. A line has an InertiaRatio of zero, a circle has an
    # InertiaRatio of 1.
    parameters.filterByInertia = True
    parameters.minInertiaRatio = 0.35

    # Distance Between Blobs
    parameters.minDistBetweenBlobs = 0.5

    # Create a detector with the parameters.
    detector = cv2.SimpleBlobDetector_create(parameters)

    ''' Use this code when a video/camera stream is inputed. '''
    # while camera.isOpened():
    #     retval, im = camera.read()
    #     overlay = im.copy()
    #     keypoints = detector.detect(im)
    #     image_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #     cv2.imshow("Output", image_with_keypoints)
    #     cv2.waitKey(1)
    # camera.release()
    # cv2.destroyAllWindows()

    ''' Use this code for single images. '''
    # Detect blobs.
    keypoints = detector.detect(image)
    number_of_holes = len(keypoints)

    # Draw detected blobs as red circles.
    image_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("Keypoints", image_with_keypoints)
    cv2.waitKey(0)

    if number_of_holes < 10:
        print("No shotgun exit holes identified.")
    elif 10 <= number_of_holes <= 20:
        print(number_of_holes, "shotgun exit holes identified, needs user confirmation.")
    else:
        print(number_of_holes, "shotgun exit holes identified and confirmed.")
