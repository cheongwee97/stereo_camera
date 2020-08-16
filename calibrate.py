#Code structure mainly based on https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html

import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

def calibrate(camera,boardSize): #left or right camera
    bH,bW = boardSize[0],boardSize[1]
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((bH*bW,3), np.float32)
    objp[:,:2] = np.mgrid[0:bH,0:bW].T.reshape(-1,2)*20 #20mm square

    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    images = glob.glob('image_data/' + camera + '/*.jpg')

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, boardSize,None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray,corners,(5,5),(-1,-1),criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, boardSize, corners2,ret)
            cv2.imshow('img',img)
            cv2.waitKey(500)

    cv2.destroyAllWindows()


    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    np.save(camera+'_camera/ret',ret)
    np.save(camera+'_camera/mtx',mtx)
    np.save(camera+'_camera/dist',dist)
    np.save(camera+'_camera/rvecs',rvecs)
    np.save(camera+'_camera/tvecs',tvecs)
    

    if(camera == 'left'):
        img = cv2.imread('stereo_image/left.png')
    else:
        img = cv2.imread('stereo_image/right.png')
    h,  w = img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    # crop the image
    x,y,w,h = roi
    dst = dst[y:y+h, x:x+w]
    if(camera == 'left'):
        img = cv2.imwrite('stereo_image/L.png',dst)
    else:
        img = cv2.imwrite('stereo_image/R.png',dst)
    plt.imshow(dst)
    plt.show()

    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        mean_error += error

    print ("total error: ", mean_error/len(objpoints))
    return

calibrate('left', (7,9))
calibrate('right',(7,9))