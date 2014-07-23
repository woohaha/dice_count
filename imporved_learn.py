# !/usr/bin/env python
# coding=utf-8
import cv2
# import numpy as np
import Parallel

debug = True

def sixposition(fs):
    p2x, p2y = fs[1].pt
    p3x, p3y = fs[2].pt
    if p3x - p2x < 5:  # The "5" need to be fixed to meet the true environment
        return '豎'
    else:
        return '橫'


def two_three_position(fs):
    p1x, p1y = fs[0].pt
    p3x, p3y = fs[-1].pt
    if (p3y - p1y) / (p3x - p1x) < 0:
        return '反斜'
    else:
        return '斜槓'


def position(fs):
    if len(fs) == 6:
        return sixposition(fs)
    elif len(fs) == 2 or len(fs) == 3:
        return two_three_position(fs)
    else:
        return None


def getimg():
    with open('/dev/video0','rb')as cam:
        img=cam.read(102400)

    return img
img = cv2.imread("webcam.png",cv2.CV_LOAD_IMAGE_GRAYSCALE)
img2=cv2.bitwise_not(img)
cv2.imshow('img2BW.jpg',img2)
cv2.waitKey(0)
#cap = cv2.VideoCapture()
#ret, frame = cap.read()
#cap.release()
#buff=getimg()
#frame_string=StringIO.StringIO(buff)
#frame=cv2.imread(frame_string)
#if not ret:
#    raise Exception("Cannot Capture Video")
#img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img2 = rotateImage(img2, 90)

detector = cv2.FeatureDetector_create('SimpleBlob')
fs = detector.detect(img2)
fs.sort(key=lambda x: x.pt)
print(len(fs), position(fs))

if debug:
    for points in fs:
        print(points.pt)
