# code used from https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# https://stackoverflow.com/questions/47483951/how-to-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-image
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# boundaries = [([36, 25, 25], [70, 255, 25])]

# (lower, upper) = boundaries[0]
# lower = np.array(lower, dtype = "uint8")
# upper = np.array(upper, dtype = "uint8")

mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))
imask = mask > 0
green = np.zeros_like(image, np.uint8)
green[imask] = image[imask]

cv2.imshow("images", np.hstack([image, green]))

# gray = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
# thresh = 
cv2.waitKey(0)