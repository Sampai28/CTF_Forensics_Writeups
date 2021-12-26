import cv2 as cv
import numpy as np
from PIL import Image

im = Image.open("HelloDarknessMyOldFriend.png")
#im.show()

im1 = np.array(im)
temp = im1*256-im1.std()

from PIL import Image
from matplotlib import cm
image = Image.fromarray(np.uint8(cm.gist_earth(temp)*255))

image.show()