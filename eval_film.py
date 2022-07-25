import cv2
import numpy as np

vector = np.zeros((4,2), np.int64)
# print(vector)
counter = 0

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_MBUTTONDOWN:
        vector[counter] = x,y
        counter = counter + 1
    if event == cv2.EVENT_LBUTTONDOWN:
        print(vector)

img = cv2.imread('Image/img070.jpg')

while True:
  if counter ==4:
    width, height = 250, 350
    pts1 = np.float32([vector[0],vector[1],vector[2],vector[3]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgoutput = cv2.warpPerspective(img, matrix,(width, height))
    cv2.imshow('Output image', imgoutput)
  for x in range(0, 4):
    cv2.circle(img, (vector[x][0], vector[x][1]), 3, (0, 255, 0), cv2.FILLED)

  cv2.imshow('Original image', img)
  cv2.setMouseCallback('Original image', mousePoints)
  cv2.waitKey(1)
