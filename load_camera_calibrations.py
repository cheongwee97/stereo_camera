import numpy as np

camera = 'left'
print(np.load(camera+'_camera/ret.npy'))
print(np.load(camera+'_camera/mtx.npy'))
# print(np.load(camera+'_camera/dist.npy'))
# print(np.load(camera+'_camera/rvecs.npy'))
# print(np.load(camera+'_camera/tvecs.npy'))

camera = 'right'
print(np.load(camera+'_camera/ret.npy'))
print(np.load(camera+'_camera/mtx.npy'))
# print(np.load(camera+'_camera/dist.npy'))
# print(np.load(camera+'_camera/rvecs.npy'))
# print(np.load(camera+'_camera/tvecs.npy'))