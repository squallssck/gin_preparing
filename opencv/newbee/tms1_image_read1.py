import numpy as np
import cv2 as cv

# Load an color image in grayscale
# img = cv.imread(D:/gin/gin_preparing/opencv/newbee/resources/dboy.jpg,cv.IMREAD_COLOR)
img = cv.imread('D:/gin/gin_preparing/opencv/newbee/resources/dboy.jpg',cv.IMREAD_GRAYSCALE)
# img = cv.imread('D:/gin/gin_preparing/opencv/newbee/resources/dboy.jpg',cv.IMREAD_UNCHANGED)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()