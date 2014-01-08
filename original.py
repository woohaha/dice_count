import cv2
import numpy as np

WAITKEY_DELAY_MS = 10
STOP_KEY = 'q'

cv2.cv.NamedWindow("image - press 'q' to quit", cv2.cv.CV_WINDOW_AUTOSIZE);
cv2.cv.NamedWindow("post-process", cv2.cv.CV_WINDOW_AUTOSIZE);

key_pressed = False
while key_pressed != STOP_KEY:

    # grab image
    orig = cv2.cv.LoadImage('sample.jpg')

    # create tmp images
    grey_scale = cv2.cv.CreateImage(cv2.cv.GetSize(orig), 8, 1) #色size=orig depth=8 channel=1
    processed = cv2.cv.CreateImage(cv2.cv.GetSize(orig), 8, 1)

    cv2.cv.Smooth(orig, orig, cv2.cv.CV_GAUSSIAN, 3,
                  3) #Smooth(src,dst,smoothtype=CV GAUSSIAN,param1=3,param2=0,param3=0,param4=0)

    cv2.cv.CvtColor(orig, grey_scale, cv2.cv.CV_RGB2GRAY)

    # do some processing on the grey scale image
    cv2.cv.Erode(grey_scale, processed, None, 10) #Erode(src,dst,element=NULL,itertions=1)
    cv2.cv.Dilate(processed, processed, None, 10) #same as above
    cv2.cv.Canny(processed, processed, 5, 70, 3) #描draw edge
    cv2.cv.Smooth(processed, processed, cv2.cv.CV_GAUSSIAN, 15, 15)

    storage = cv2.cv.CreateMat(orig.width, 1, cv2.cv.CV_32FC3) #create a matrix 32bit depth, float, 3 channels

    # these parameters need to be adjusted for every single image
    HIGH = 50
    LOW = 140

    try:
        # extract circles
        cv2.cv.HoughCircles(processed, storage, cv2.cv.CV_HOUGH_GRADIENT, 2, 32.0, HIGH, LOW)

        for i in range(0, len(np.asarray(storage))):
            print "circle #%d" % i
            Radius = int(np.asarray(storage)[i][0][2])
            x = int(np.asarray(storage)[i][0][0])
            y = int(np.asarray(storage)[i][0][1])
            center = (x, y)

            # green dot on center and red circle around
            cv2.cv.Circle(orig, center, 1, cv2.cv.CV_RGB(0, 255, 0), -1, 8, 0)
            cv2.cv.Circle(orig, center, Radius, cv2.cv.CV_RGB(255, 0, 0), 3, 8, 0)

            cv2.cv.Circle(processed, center, 1, cv2.cv.CV_RGB(0, 255, 0), -1, 8, 0)
            cv2.cv.Circle(processed, center, Radius, cv2.cv.CV_RGB(255, 0, 0), 3, 8, 0)

    except:
        print "nothing found"
        pass

    # show images
    cv2.cv.ShowImage("image - press 'q' to quit", orig)
    cv2.cv.ShowImage("post-process", processed)

    cv_key = cv2.cv.WaitKey(WAITKEY_DELAY_MS)
    key_pressed = chr(cv_key & 255)
