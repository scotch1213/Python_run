import cv2 as cv


#------------- Reading Images.
# img = cv.imread('Photos/cat.jpg')
#img = cv.imread('Photos/cat_large.jpg')

#cv.imshow('Cat', img)

## after 'val' time window close.
## val '0' = infinite time.
#------------- Reading Images.

#------------- Reading vidoes.
capture = cv.VideoCapture('Videos/dog.mp4')

while True :
    isTrue, frame= capture.read()
    
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()