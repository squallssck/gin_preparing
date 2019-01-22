import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
# count = 0
# while(count<10):
while(True):
    #=== Capture frame-by-frame
    ret, frame = cap.read()
    #=== Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #=== Display the resulting frame
    # cv.imshow(str(count),gray)
    cv.imshow('image',gray)
    # count = count + 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# ===When everything done, release the capture
# cv.waitKey(0)
cap.release()
cv.destroyAllWindows()