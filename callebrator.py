#!/usr/bin/env python
# encoding=utf-8

import cv2
import math
import sys
reload(sys)
sys.setdefaultencoding('utf8')

d_red = cv2.cv.RGB(150, 55, 65)
l_red = cv2.cv.RGB(250, 200, 200)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

detector = cv2.FeatureDetector_create('SimpleBlob')

while ret:
    ret, frame = cap.read()

    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fs = detector.detect(img2)
    fs.sort(key=lambda x: -x.size)

    def supress(x):
        for f in fs:
            distx = f.pt[0] - x.pt[0]
            disty = f.pt[1] - x.pt[1]
            dist = math.sqrt(distx * distx + disty * disty)
            if (f.size > x.size) and (dist < f.size / 2):
                return True

    sfs = [x for x in fs if not supress(x)]

    for f in sfs:
        cv2.circle(frame, (int(f.pt[0]), int(f.pt[1])), int(
            f.size), d_red, 2, cv2.CV_AA)
        cv2.circle(frame, (int(f.pt[0]), int(f.pt[1])), int(
            f.size), l_red, 1, cv2.CV_AA)

    print('there are {} points detected'.format(len(sfs)))

    cv2.putText(frame, '{}Points Counted'.format(
        len(sfs)), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
    cv2.putText(frame, 'Press Q to Exit', (
        0, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

    cv2.imshow('Calleberator', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
