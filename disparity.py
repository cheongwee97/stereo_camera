import numpy as np
import cv2
from matplotlib import pyplot as plt

def nothing(val):
    pass


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

TsuL = cv2.imread('Tsukuba_L.png',0)
TsuR = cv2.imread('Tsukuba_R.png',0)


cv2.namedWindow("Disparity",cv2.WINDOW_NORMAL)
cv2.createTrackbar("minDisparity", "Disparity", 0, 100, nothing)
cv2.createTrackbar("numDisparites", "Disparity", 1, 10, nothing)
cv2.createTrackbar("blockSize", "Disparity", 5, 50, nothing)
cv2.createTrackbar("P1", "Disparity", 0, 100, nothing)
cv2.createTrackbar("P2", "Disparity", 0, 100, nothing)
cv2.createTrackbar("disp12MaxDiff", "Disparity", 0, 50, nothing)
cv2.createTrackbar("preFilterCap", "Disparity", 0, 50, nothing)
cv2.createTrackbar("uniquenessRatio", "Disparity", 0, 50, nothing)
cv2.createTrackbar("speckleWindowSize", "Disparity", 0, 50, nothing)
cv2.createTrackbar("speckleRange", "Disparity", 0, 50, nothing)




while True:
    minDisparity_ = cv2.getTrackbarPos("minDisparity","Disparity")
    blockSize_ = cv2.getTrackbarPos("blockSize", "Disparity")
    numDisparities_ = cv2.getTrackbarPos("numDisparites", "Disparity") * 16
    P1_ = cv2.getTrackbarPos("P1", "Disparity")
    P2_ = cv2.getTrackbarPos("P2", "Disparity")
    disp12MaxDiff_ = cv2.getTrackbarPos("disp12MaxDiff", "Disparity")
    preFilterCap_ = cv2.getTrackbarPos("preFilterCap", "Disparity")
    uniquenessRatio_ = cv2.getTrackbarPos("uniquenessRatio", "Disparity")
    speckleWindowSize_ = cv2.getTrackbarPos("speckleWindowSize", "Disparity")
    speckleRange_ = cv2.getTrackbarPos("speckleRange", "Disparity")
    if(numDisparities_ == 0):
        numDisparities_ = 16
    if(blockSize_ % 2 == 0):
        blockSize_ += 1
    if(blockSize_ < 5):
        blockSize_ = 5
    stereo = cv2.StereoSGBM_create(minDisparity=minDisparity_,
                               numDisparities=numDisparities_, 
                               blockSize=blockSize_,
                               P1=P1_,
                               P2=P2_,
                               disp12MaxDiff=disp12MaxDiff_,
                               preFilterCap=preFilterCap_,
                               uniquenessRatio=uniquenessRatio_,
                               speckleWindowSize=speckleWindowSize_,
                               speckleRange=speckleRange_)
    disparity = stereo.compute(imgL,imgR)
    cv2.imshow("Frame", disparity.astype(np.uint8))
    cv2.imshow("Left image", imgL)
    cv2.imshow("Right image", imgR)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        parameters = (minDisparity_,numDisparities_,blockSize_,P1_,P2_,disp12MaxDiff_,preFilterCap_,uniquenessRatio_,speckleWindowSize_,speckleRange_)
        np.save("StereoSGBM_parameters",parameters)
        break

cv2.destroyAllWindows()
