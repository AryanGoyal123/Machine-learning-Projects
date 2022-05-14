#draw shapes and write on images in cv

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
blank = np.zeros((500,500,3), dtype='uint8') #height,width,color channels

#paint the image a certain color
#blank[:] = 0,255,0

#some part of it
#blank[200:300, 300:400] = 0,255,0

#rectangle
cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=2)
#cv.imshow('Green', blank)

#draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
cv.imshow("Circle", blank)

#draw a line
cv.line(blank, (250,250), 40, (0,0,255), thickness=3)

#write
cv.putText(blank, 'Hello', (225,225), (300,400), cv.FONT_HERSHEY_TRIPLEX, 1, (0,255,0), 2)
cv.imshow('text', blank)

#give the circle a center of where to put the circle
#cv.imshow('cat', img)
cv.waitKey(0)
