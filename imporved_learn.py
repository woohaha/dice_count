import cv2

orig = cv2.imread("img/sample_6_dash.jpg")
img = orig.copy()
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.FeatureDetector_create('SimpleBlob')
fs = detector.detect(img2)
# fs.sort(key=lambda x: -x.size)

print(len(fs))  # dice dots

#TODO distinct the two position of 2, 3, 6 dots
for points in fs:
    print('(%d,%d)' % points.pt)

p1x, p1y = fs[0].pt
p2x, p2y = fs[1].pt
if (p1y - p2y) < (p1x - p2x):
    print('upright')
else:
    print('dash')


