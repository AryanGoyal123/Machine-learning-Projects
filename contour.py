import cv2 as cv
import numpy as np

#contours are the boundaries of an object, they can be edges, but they are differnt mathematically
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat',img) #name,what image

blank = np.zeros(img.shape, dtype = "uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) #kernal size

canny = cv.Canny(img, 125,175)
cv.imshow('canny', canny)

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#the heir of the contours and what shapes are inside what shapes
print(f'{len(contours)} contours found')

#draw the contours using the value of the cv lib
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours drawn', blank)

#we can also use thresholding for contours
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.waitKey(0)

