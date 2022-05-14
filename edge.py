import cv2 as cv
from cv2 import threshold
from cv2 import adaptiveThreshold
from cv2 import mean
import numpy as np
import matplotlib.pyplot as plt

#focus on certain parts of the image
img = cv.imread('Photos/Cats.jpg')
cv.imshow('Cat',img)

#not gradients -- but they are very similar in terms of the programming

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64FC1)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('combined', combined_sobel)

cv.waitKey(0)