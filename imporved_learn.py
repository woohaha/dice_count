import cv2
import numpy as np


def rotateImage(image, angle):
    image_center = tuple(np.array(image.shape) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape, flags=cv2.INTER_LINEAR)
    return result


orig = cv2.imread("img/sample_2.jpg")
img = orig.copy()
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = rotateImage(img2, 90)

detector = cv2.FeatureDetector_create('SimpleBlob')
fs = detector.detect(img2)
# fs.sort(key=lambda x: -x.size)

print(len(fs))  # dice dots


#TODO distinct the two position of 2, 3, 6 dots
for points in fs:
    print('(%d,%d)' % points.pt)


def sixposition():
    p1x, p1y = fs[0].pt
    p2x, p2y = fs[1].pt
    if (p1y - p2y) < (p1x - p2x):
        print('upright')
    else:
        print('dash')


p1x, p1y = fs[0].pt
p3x, p3y = fs[-1].pt

if ((p3y - p1y) / (p3x - p1x) < 0):
    print('left')
else:
    print('right')

