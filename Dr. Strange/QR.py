import cv2 as cv
import numpy as np

i=cv.imread('file.png') #for image in the .odt file

t = i*256 - i.std()

cv.imshow('img', t)
cv.imshow('i', i)
cv.waitKey(0)
cv.destroyAllWindows()
