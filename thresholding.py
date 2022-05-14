import cv2 as cv
from cv2 import threshold
from cv2 import adaptiveThreshold
from cv2 import mean
import numpy as np
import matplotlib.pyplot as plt

#focus on certain parts of the image
img = cv.imread('Photos/Cats.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)
#convert to binary -- black and white

#simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simpel thres',thresh)

#adaptive
adaptive_Threshold =  cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('adapt', adaptive_Threshold)



cv.waitKey(0)