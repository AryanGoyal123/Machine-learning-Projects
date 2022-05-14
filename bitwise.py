import cv2 as cv
from cv2 import rectangle
from cv2 import circle
from cv2 import bitwise_and
from cv2 import bitwise_or
import numpy as np

blank = np.zeros((400,400), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200,255, -1)


cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise AND -- the intersection of the images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_and)

#OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('OR', bitwise_or)

cv.waitKey(0)