import black
import cv2 as cv
from cv2 import circle
import numpy as np
import matplotlib.pyplot as plt

#focus on certain parts of the image
img = cv.imread('Photos/Cats.jpg')
cv.imshow('Cat',img)
blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

circe= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(img,img,mask=circe)
#grayscale histogram
gray_hist = cv.calcHist([gray], [0],mask,[256],ranges=[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim(0.255)
plt.show()

cv.waitKey(0)