# !/usr/bin/env python
# coding=utf-8

import cv2
import numpy as np
#import Parallel
import math

debug = True


def sixposition(fs):
    p2x, p2y = fs[1].pt
    p3x, p3y = fs[2].pt
    if p3x - p2x < 5:  # The "5" need to be fixed to meet the real environment
        return True  # 縱向排列
    else:
        return False  # 橫向排列


def two_three_position(fs):
    p1x, p1y = fs[0].pt
    p3x, p3y = fs[-1].pt
    if (p3y - p1y) / (p3x - p1x) < 0:
        return True  # 反斜
    else:
        return False  # 斜槓


def position(fs):
    if len(fs) == 6:
        return sixposition(fs)
    elif len(fs) == 2 or len(fs) == 3:
        return two_three_position(fs)
    else:
        return None


def supress(x):
    for f in fs:
        distx = f.pt[0] - x.pt[0]
        disty = f.pt[1] - x.pt[1]
        dist = math.sqrt(distx * distx + disty * disty)
        if (f.size > x.size) and (dist < f.size / 2):
            return True


def markcircle(sfs, img):
    for f in sfs:
        cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(
            f.size), d_red, 2, cv2.CV_AA)
        cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(
            f.size), l_red, 1, cv2.CV_AA)
    return img

# img = cv2.imread("webcam.png", cv2.CV_LOAD_IMAGE_GRAYSCALE) #讀取樣版圖
# img2 = cv2.bitwise_not(img) #反色

d_red = cv2.cv.RGB(150, 55, 65)
l_red = cv2.cv.RGB(250, 200, 200)
cap = cv2.VideoCapture(0)
detector = cv2.FeatureDetector_create('SimpleBlob')
ret, frame = cap.read()
if not ret:
    raise Exception("Cannot Capture Video")

h, w = frame.shape[:2]
vis = np.zeros((h, w * 2 + 5), np.uint8)
vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
sfs = []

while ret:
    ret, frame = cap.read()
    img = frame.copy()
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vis[:h, :w] = frame

    fs = detector.detect(img2)
    fs.sort(key=lambda x: x.pt)
    sfs = [x for x in fs if not supress(x)]
    img = markcircle(sfs, img)
    vis[:h, w + 5:w * 2 + 5] = img
    if cv2.waitKey(10) & 0xFF == ord('c'):
        print(len(sfs), position(sfs))  # Output Compute Result
        if debug:
            for points in sfs:
                print(points.pt)
            cv2.imwrite('captured.jpg', vis)

    cv2.imshow('image', vis)
    if cv2.waitKey(11) & 0xFF == 27:  # Esc Key Code
        break

cap.release()
cv2.destroyAllWindows()
