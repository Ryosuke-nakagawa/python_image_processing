import cv2

img = cv2.imread("./milkdrop.bmp", 0)

threshold = 135

#大津の二値化に使用, 二値化された画像 = cv2.threshold(読み込んだ画像①, しきい値②, 変換後の値③, 二値化手法④)
ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)


cv2.imshow("img_th", img_thresh)
cv2.waitKey()
cv2.destroyAllWindows()