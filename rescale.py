import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # available on image, video, live video
    width = int(frame.shape[1] * scale)         #frame.shape[1] == width
    height = int(frame.shape[0] * scale)        #frame.shape[0] == height
    
    dimension = (width,height)                  # as same as table.
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    #available on live video.
    capture.set(3,width)
    capture.set(4,height)
    
#------------- Reading images
img = cv.imread('Photos/cat.jpg')
resized_img = rescaleFrame(img, 0.5)
cv.imshow('Cat', img)
cv.imshow('Cat resized', resized_img)


#------------- Reading vidoes.
capture = cv.VideoCapture('Videos/dog.mp4');

while True :
    isTrue, frame= capture.read()
    
    frame_resize = rescaleFrame(frame, scale=0.2)
    
    cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resize)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()