#!/usr/bin/env python
# coding=utf-8
import cv2
import numpy as np

debug = 0


def rotateImage(image, angle):
    image_center = tuple(np.array(image.shape) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = \
        cv2.warpAffine(image, rot_mat, image.shape, flags=cv2.INTER_LINEAR)
    return result


def sixposition(fs):
    p2x, p2y = fs[1].pt
    p3x, p3y = fs[2].pt
    if p3x - p2x < 5:  # The "5" need to be fixed to meet the true environment
        return u'豎'
    else:
        return u'橫'


def two_three_position(fs):
    p1x, p1y = fs[0].pt
    p3x, p3y = fs[-1].pt
    if ((p3y - p1y) / (p3x - p1x) < 0):
        return u'反斜'
    else:
        return u'斜槓'


def position(fs):
    if len(fs) == 6:
        return sixposition(fs)
    elif (len(fs) == 2 or len(fs) == 3):
        return two_three_position(fs)
    else:
        return 'none'


orig = cv2.imread("img/sample_6.jpg")
img = orig.copy()
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img2 = rotateImage(img2, 90)

detector = cv2.FeatureDetector_create('SimpleBlob')
fs = detector.detect(img2)
fs.sort(key=lambda x: x.pt)
print(len(fs), position(fs))

if debug == 1:
    for points in fs:
        print('(%d,%d)' % points.pt)
