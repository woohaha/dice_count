#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
cam = cv2.VideoCapture(0)   # 0 -> index of camera
while True:
    s, img = cam.read()
    if s:    # frame captured without any errors
        # cv2.namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        cv2.imshow("cam-test", img)
        if cv2.waitKey(0) or 0xFF == ord('q'):
            break
    else:
        raise Exception('Cannot Capture Video')
cam.release()
cv2.destroyAllWindows()
