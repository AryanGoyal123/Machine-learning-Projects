import cv2 as cv
from cv2 import GaussianBlur
import numpy as np

#contours are the boundaries of an object, they can be edges, but they are differnt mathematically
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat',img) #name,what image

#smooth out the image by reduced the noise
# gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gauss', gauss)

#Averageing
average = cv.blur(img, (3,3))
cv.imshow('avg',average)

#median blur
#bilateral
bilateral = cv.bilateralFilter(img, 5, sigmaColor= 15, sigmaSpace=15)
cv.imshow('bilat', bilateral)

cv.waitKey(0)