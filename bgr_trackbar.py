import cv2 as cv
import numpy as np

cv.namedWindow("BGR")
BGR = np.zeros((500,500,3),np.uint8)
def func(x):
    pass
cv.createTrackbar("Blue","BGR",0,255,func)
cv.createTrackbar("Green","BGR",0,255,func)
cv.createTrackbar("Red","BGR",0,255,func)

while True:
    cv.imshow("BGR",BGR)
    blue = cv.getTrackbarPos("Blue","BGR")
    green = cv.getTrackbarPos("Green","BGR")
    red = cv.getTrackbarPos("Red","BGR")
    BGR[:] = [blue,green,red]
    cv.waitKey(1)



