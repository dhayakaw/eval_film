import sys
import cv2
import numpy as np
from sklearn.metrics import mean_squared_error
import decimal


args = sys.argv

path = args[1]
img = cv2.imread(path)
cv2.imshow('Original image', img)

while True:
  ROI = cv2.selectROI('select ROI', img, fromCenter = False, showCrosshair = False)

# print(ROI)

  img_crop = img[int(ROI[1]):int(ROI[1]+ROI[3]),int(ROI[0]):int(ROI[0]+ROI[2])]
  # cv2.imshow("crop", img_crop)

  v = np.empty([ROI[3],ROI[2]])
  for i_w in range(ROI[2]):
    for i_h in range(ROI[3]):
      x = img_crop[i_h, i_w]
      v[i_h, i_w] = sum(x)/3.0

# print (v)
  v_mean = np.full_like(v,np.mean(v))
  rmse = mean_squared_error(v, v_mean, squared = False)

  decimal.getcontext().prec = 3
  d_mean = decimal.Decimal(255-np.mean(v))
  d_rmse = decimal.Decimal(rmse)
  print ('mean: ' , +d_mean, ' rms: ', +d_rmse)
  print ('')

cv2.waitKey(0)
