import cv2 as cv
import numpy as np
#read images and videos
img = cv.imread('Photos/park.jpg')

#Translate
def translate(img, x, y):
    transMat= np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)

#rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #scale value as 1.0
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)
    
#we can rotate a rotated image easily

#flipping
# 0 flip vertically
# 1 flip horizontally
# -1 both vertically and horizontally

#cropping
cropped = img[200:400, 300:400] #the start to finish of the x and y values

cv.imshow('park', translated)
cv.waitKey(0)