import cv2 as cv
img = cv.imread('DogAndTheMountains.tif', cv.IMREAD_UNCHANGED)
#Sometimes... keeping things the way they are, is a nice approach to a problem

#cv.imshow('img', img)
#cv.waitKey(0)
#cv.destroyAllWindows()

c,m,y,k = cv.split(img)#CMYK

#cv.imshow('channel', y)
#cv.waitKey(0)
#cv.destroyAllWindows()

y1 = cv.bitwise_xor(y,k) #ROX

#cv.imshow('channel', y1)
#cv.waitKey(0)
#cv.destroyAllWindows()

_, thresh = cv.threshold(y1, 1, 255, cv.THRESH_BINARY) # @1

cv.imshow('channel', thresh)
cv.waitKey(0)
cv.destroyAllWindows()