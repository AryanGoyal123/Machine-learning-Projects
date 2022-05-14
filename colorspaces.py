import cv2 as cv
import numpy as np


img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)

#BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat',gray) #name,what image
cv.waitKey(0)

#BGR to hey saturation value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to LAB
lab= cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)
