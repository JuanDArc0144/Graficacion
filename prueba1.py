import cv2 as cv
print(cv.__version__)
img = cv.imread('tuxYRei.jpg')
cv.imshow('Tux', img)
print("Hello")