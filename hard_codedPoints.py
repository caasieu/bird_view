import cv2
import numpy as np

img = cv2.imread('images/bcards.jpg')

# Defining the size of the cropped image
width, height = 460, 360

# Manually place points to select
points = np.float32([
  [507, 729],
  [1367, 857],
  [381, 1205],
  [1359, 1379],
])

points2 = np.float32([
    [0,0],
    [width, 0],
    [0, height],
    [width, height],
])

matrix = cv2.getPerspectiveTransform(points, points2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

#for x in range(0, 4):
#cv2.circle(img, (int(pts1[0][0]), int(pts1[0][1])), 10, (0,0,255), cv2.FILLED)

for point in points:
    cv2.circle(img, (int(point[0]), int(point[1])), 10, (0,0,255), cv2.FILLED)

cv2.namedWindow('My', cv2.WINDOW_NORMAL)
cv2.resizeWindow('My', 960, 880)

cv2.imshow('My', img)
cv2.imshow('Cropped Image', imgOutput)
cv2.waitKey(0)
