import cv2
import numpy as np

img = cv2.imread('Image/img070.jpg')
cv2.imshow('Original image', img)

ROI = cv2.selectROI('select ROI', img, fromCenter = False, showCrosshair = False)

print(ROI)

img_crop = img[int(ROI[1]):int(ROI[1]+ROI[3]),int(ROI[0]):int(ROI[0]+ROI[2])]
# img_crop = img[int(ROI[1]):int(ROI[3]),int(ROI[0]):int(ROI[2])]

print(img_crop)

cv2.imshow("crop", img_crop)


cv2.waitKey(0)
