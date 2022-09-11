import cv2
import numpy as np

img = cv2.imread("./milkdrop.bmp")

cv2.imshow('preview', img)
cv2.waitKey()

img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

threshold = 135

_, img_thresh = cv2.threshold(img_grayscale, threshold, 255, cv2.THRESH_BINARY)

height, width = img_thresh.shape[:2]

img_thresh_trim = img_thresh[100 : height, 100 : width]

contours, hierarchy = cv2.findContours(img_thresh_trim, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contour = list(filter(lambda x: cv2.contourArea(x) >= 1000, contours))

mask = np.zeros(img.shape, dtype = np.uint8)
drawed_mask = cv2.drawContours(mask, contour, -1, (255, 255, 255), -1, offset=(100,100))

output = cv2.bitwise_and(img, drawed_mask )

cv2.imshow("output", output)
cv2.waitKey()
cv2.destroyAllWindows()