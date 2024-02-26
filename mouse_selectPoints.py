import cv2
import numpy as np

img = cv2.imread('images/bcards.jpg')
# Defining an array of circles | 4 rows each having 2 columns
circles = np.zeros((4,2), np.float32)
counter = 0

# Defining the size of the cropped image
width, height = 460, 360
def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        # append x and y values in the counter matrix
        circles[counter] = x, y
        counter = counter + 1

        #print(x,y)
        #print(circles)


while True and cv2.waitKey(1) & 0xFF != ord('q'):
    cv2.namedWindow('Mouse Select Points', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Mouse Select Points', 860,680)

    pointDimensions = np.float32([
        [0,0],
        [width, 0],
        [0, height],
        [width, height]
    ])

    if counter == 4:
        matrix = cv2.getPerspectiveTransform(circles, pointDimensions)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))

        # Display the cropped mouse selected image
        cv2.imshow('Cropped Image', imgOutput)



    for point in circles:
        cv2.circle(img, (int(point[0]),int(point[1])), 5, (0,255,0), cv2.FILLED)

    cv2.imshow('Mouse Select Points', img)
    cv2.setMouseCallback('Mouse Select Points', mousePoints)
