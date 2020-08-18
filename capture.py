import numpy as np
import cv2

cam0 = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(1)
left_count = 0
right_count=0

while True:
    ret0, frame0 = cam0.read()
    ret1, frame1 = cam1.read()
    k = cv2.waitKey(1)
    if (ret0):
        cv2.imshow('Cam 0', frame0)

        if k%256 == 32:
            # SPACE pressed
            cv2.imwrite("image_data/left/" + str(left_count) + ".png", frame0) #for taking images of calibration board
            # print("Input left image name")
            # leftname = input() 
            # cv2.imwrite("stereo_image/" + leftname + ".png", frame0)
            left_count += 1

    if (ret1):
        cv2.imshow('Cam 1', frame1)

        if k%256 == 32:
            # SPACE pressed
            cv2.imwrite("image_data/right/" + str(right_count) + ".png", frame1) #for taking images of calibration board
            # print("Input right image name")
            # rightname = input()          
            # cv2.imwrite("stereo_image/" + rightname + ".png", frame1)
            right_count += 1

    if k & 0xFF == ord('q'): # 'q' pressed
        break

# Release
cam0.release()
cam1.release()
cv2.destroyAllWindows()