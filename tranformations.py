import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('park', img)

# Translation Func
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('translated', translated)

# Rotation

# + --> CCW
# - --> CW
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('rotated', rotated)

rotated_rotated = rotate(rotated, -45) # rotate된 이미지의 ViewPort(블랙 포함)자체를 다시 돌려버림.
cv.imshow('rotated_rotated', rotated_rotated)

# Rsizing
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resize)

# Flipping
# Flipcode = 0, Inverse Y
# Flipcode = 1, Inverse X
# Flipcode = -1, Inverse XY
flipped = cv.flip(img, -1)
cv.imshow('flipped', flipped)

# Cropping(잘라내기)
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)