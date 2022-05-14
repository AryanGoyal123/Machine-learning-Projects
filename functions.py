import cv2 as cv
from cv2 import COLOR_BGR2GRAY

#read images and videos
img = cv.imread('Photos/park.jpg')

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT) #kernal size

#edge cascade in the images
canny = cv.Canny(blur, 125,125)
#cv.imshow('cat', canny)

#dilate an image
dilated = cv.dilate(canny, (3,3), iterations=1)
#cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)

# cropping , basically array slicing
cropped = img[50: 200, 200:400]

cv.waitKey(0)
