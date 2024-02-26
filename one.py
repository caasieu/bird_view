import cv2
import numpy as np

img = cv2.imread('images/bcards.jpg')

width, height = 360, 260
points = np.float32([
  [507, 729],
  [1367, 857],
  [1359, 1379],
  [381, 1205]
])


#for x in range(0, 4):
#cv2.circle(img, (int(pts1[0][0]), int(pts1[0][1])), 10, (0,0,255), cv2.FILLED)



for point in points:
    cv2.circle(img, (int(point[0]), int(point[1])), 10, (0,0,255), cv2.FILLED)



cv2.namedWindow('My', cv2.WINDOW_NORMAL)
cv2.resizeWindow('My', 960, 880)

cv2.imshow('My', img)
cv2.waitKey(0)
