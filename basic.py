import cv2 as cv

# img = cv.imread('Photos/cat.jpg')

img = cv.imread('Photos/park.jpg')
cv.imshow('img',img)

# Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur(gaussian)
# (3,3) = kernel size.
# BORDER_DEFAULT = 테두리 처리 방법.
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# 캐니 엣지는 라플라스 필터 방식을 개선한 방식으로 x와 y에 대해 1차 미분을 계산한 다음, 네 방향으로 미분합니다.
# 네 방향으로 미분한 결과로 극댓값을 갖는 지점들이 가장자리가 됩니다.
# 앞서 설명한 가장자리 검출기보다 성능이 월등히 좋으며 노이즈에 민감하지 않아 강한 가장자리를 검출하는 데 목적을 둔 알고리즘입니다.
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

# Dilating(확장) the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

# Eroding(축소) the image
eroded = cv.erode(canny, (3,3), iterations=1)
cv.imshow('eroded', eroded)

# Resize
# resized = cv.resize(img, (img.shape[1]//2,img.shape[0]//2))
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
resized1 = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
resized2 = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resized)
cv.imshow('resized1', resized1)
cv.imshow('resized2', resized2)

# Cropping(잘라내기)
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)