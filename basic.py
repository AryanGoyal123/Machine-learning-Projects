import cv2 as cv
import cv2
from cv2 import COLOR_BGR2GRAY


#read images and videos
img = cv.imread('Photos/cat.jpg')

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

    #only for live video
    #instance change of the frame coming into the computer

#resize and rescale images
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) #define a new size of the array
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height) #set the dimensions of the pixels array
    
    return cv2.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#read videos
capture = cv.VideoCapture('Videos/dog.mp4') #zero is the camera

while True:
        isTrue, frame = capture.read()
        cv.imshow('Video',frame)
        
        frame_resized = rescaleFrame(frame)
        
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

capture.release()
cv.destroyAllWindows()


#converting to grayscale
gray = cv.cvtColor(img, cv,COLOR_BGR2GRAY)
cv.imshow('Cat',img) #name,what image

#blur an image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #kernal size

#edge cascade in the images
canny = cv.Canny(img, 125,125)

cv.waitKey(0)
