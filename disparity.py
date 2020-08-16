import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('stereo_image/L.png',0)
imgR = cv2.imread('stereo_image/R.png',0)
fixed_height = 0
fixed_width = 0
if(imgL.shape[1] < imgR.shape[1]):
    fixed_height = imgL.shape[1]
else:
    fixed_height = imgR.shape[1]
if(imgL.shape[0] < imgR.shape[0]):
    fixed_width = imgL.shape[0]
else:
    fixed_width = imgR.shape[0]
imgL = cv2.resize(imgL, (fixed_height, fixed_width))
imgR = cv2.resize(imgR, (fixed_height, fixed_width))
# imgL = cv2.GaussianBlur(imgL,(3,3),None)
# imgR = cv2.GaussianBlur(imgR,(3,3),None)

TsuL = cv2.imread('Tsukuba_L.png',0)
TsuR = cv2.imread('Tsukuba_R.png',0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=5)
disparity = stereo.compute(imgL,imgR)

stereo2 = cv2.StereoBM_create(numDisparities=16,blockSize=5)
disparity2 = stereo2.compute(TsuL,TsuR)

plt.figure(1)
plt.subplot(221)
plt.imshow(imgL)
plt.subplot(222)
plt.imshow(imgR)
plt.subplot(223)
plt.imshow(disparity)

plt.figure(2)
plt.subplot(221)
plt.imshow(TsuL)
plt.subplot(222)
plt.imshow(TsuR)
plt.subplot(223)
plt.imshow(disparity2)
plt.show()