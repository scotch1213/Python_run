import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[:] = 0,255,0

# column, row
# blank[100:200, 100:400] = 0,0,255

# 2. Draw a Rectangle
# width, height, BGR, 
# cv.rectangle(blank, (0,0), (250,500), (255,0,0), thickness=2)
# cv.rectangle(blank, (0,0), (250,500), (255,0,0), thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (255,0,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. draw a circle
# centre, radius, bgr, thickness
cv.circle(blank, (250,250), 30, (0,0,255), thickness=2)
cv.imshow('Circle', blank)

# 4. draw a line
cv.line(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (255,255,0), thickness=4)
cv.imshow('line', blank)

# 5. Write a text
cv.putText(blank, 'Hello, Opencv', (100, 100), cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)