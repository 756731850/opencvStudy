import cv2
import numpy as np


#中值滤波消除噪点
#中值滤波在消除噪点时特别有用
#如果在某个像素周围有白色或黑色的像素，
# 这些白色或黑色的像素不会选择作为中值（最大或最小值不用），
# 而是被替换为邻域值。
img = cv2.imread('img\\salt.jpg')
result = cv2.medianBlur(img, 9)

cv2.imshow('img', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
