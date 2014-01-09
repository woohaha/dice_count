import cv2
import math
import numpy as np

d_red = cv2.cv.RGB(150, 55, 65)
l_red = cv2.cv.RGB(250, 200, 200)

orig = cv2.imread("img/sample_6.jpg")
img = orig.copy()
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.FeatureDetector_create('SimpleBlob')
fs = detector.detect(img2)
fs.sort(key=lambda x: -x.size)

print(len(fs)) #dice dots

#TODO distinct the two position of 2, 3, 6 dots


