import cv2
import numpy as np

from sklearn.metrics import mean_squared_error

img = cv2.imread('Image/img070.jpg')
cv2.imshow('Original image', img)

ROI = cv2.selectROI('select ROI', img, fromCenter = False, showCrosshair = False)

print(ROI)

img_crop = img[int(ROI[1]):int(ROI[1]+ROI[3]),int(ROI[0]):int(ROI[0]+ROI[2])]
# cv2.imshow("crop", img_crop)

v = np.empty([ROI[3],ROI[2]])
for i_w in range(ROI[2]):
  for i_h in range(ROI[3]):
    x = img_crop[i_h, i_w]
    v[i_h, i_w] = sum(x)/3.0

# print (v)
print (np.mean(v))
v_mean = np.full_like(v,np.mean(v))
rmse = mean_squared_error(v, v_mean, squared = False)
print (rmse)

cv2.waitKey(0)
