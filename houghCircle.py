import numpy as np
import cv2 as cv

img = cv.imread('classicComputerVision/edge.jpeg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File couldn't be found"
img = cv.medianBlur(img, 5)
cimg = cv.imread('classicComputerVision/edge.jpeg')

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=30,
                          minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0:]:
    #drawing the outer circle...
    cv.circle(cimg,(i[0], i[1]), i[2], 255, 2)
    #drwaing center of circle
    cv.circle(cimg,(i[0], i[1]), 2, 255,3)


cv.imshow('Detected Circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
