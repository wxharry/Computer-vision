# test.py
import numpy as np
from imageio import imread
import matplotlib.pyplot as plt
from cv2 import cv2
#Function

def PepperandSalt(img,percetage):
    NoiseImg=img.copy()
    NoiseNum=int(percetage*img.shape[0]*img.shape[1])
    for i in range(NoiseNum):
        randX = np.random.randint(0, img.shape[0])
        randY = np.random.randint(0, img.shape[1])
        if np.random.random() <=0.5:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255          
    return NoiseImg

#Import image here
# Sample call
# castle.png
m, n = 3,3
img = imread('castle.png')
im = PepperandSalt(img, 0.1)
# imclose = inclosing(im, m, n)
# imopen = imopening(im, m, n)

kernel = np.ones((m, n), np.uint8)
imopen = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
imclose = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("open",imopen)
# cv2.imshow("close",imclose)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.figure()
plt.imshow(imopen, cmap='gray')
plt.figure()
plt.imshow(imclose, cmap='gray')
plt.show()