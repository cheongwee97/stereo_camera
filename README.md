
# Stereo Vision

In this project, I try to construct a homemade stereo camera, made up of 2 budget webcams that I've purchased at Sim Lim Sqaure, taped onto 2 ruler so that I will be able to keep the cameras in a fix posture and as aligned as possible.

![My camera](my_camera.jpg)

The cameras are both connected through a usb 2.0 hub, which poses an issue of limited usb bandwith.
Here is a link for a clearer explanation https://www.zonetrigger.com/articles/USB-overload/USB-bandwidth-troubleshooting.php.
Personally, I just kept trying different ports till it ultimately worked.

Stage 1 (Taking required images):
To take images for calibration, comment lines, 19,20,21,30,31,32 and uncomment lines 18 and 29 in capture.py, run code and hit enter to take image.
To take stereo images, undo the step above and likewise hit enter to take image. Fill in the filename for the left and right images.
Press q to exit.

Stage 2 (Calibrating Camera and undistorting image):
Run calibrate.py
The returned values after calibration are stored in right_camera and left_camera

Stage 3 (Creating depth image):
Run disparity.py, adjust trackbar to tune StereoSGBM_create parameters.
Press q to exit (parameters will be saved into StereoSGBM_parameters.npy)
Additionally, I've added the Tsukuba_L and Tsukuba_R images as a control (Change (imgL,imgR) to (TsuL,TsuR) on line 70,72 and 73)

Final thoughts:
The result for my depth image was a little dissapoiting and my current level of knowledge limits me to what went wrong, it'll be nice if someone could try out my project and educate me on what went wrong. Otherwise, I would want to proceed onto producing point clouds soon and all in all I had a great time reading up and applying cv knowledge that I've acquired last semester. Cheers!