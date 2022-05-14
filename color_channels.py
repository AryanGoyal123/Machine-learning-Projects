import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')
cv.imshow('cat', img)

blank = np.zeros(img.shape[:2], dtype = "uint8")

b,g,r = cv.split(img)
#into blue green red

blue = cv.merge([b,blank,blank])

cv.imshow('Blue', blue)
#cv.imshow('green', g)
#cv.imshow('red', r)

#merge color chanel
#merged = cv.merge([b,g,r])
#cv.imshow('merged',merged)

cv.waitKey(0)