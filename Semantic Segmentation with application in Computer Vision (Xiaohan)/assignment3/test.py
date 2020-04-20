import numpy as np
from imageio import imread
from cv2 import cv2

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

m, n = 1,1
img = imread('castle.png')
im = PepperandSalt(img, 0.1)

kernel = np.ones((m, n), np.uint8)
imopen = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
cv2.imshow("open",imopen)
imclose = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)
cv2.imshow("close",imclose)