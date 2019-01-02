# -*- coding: utf-8 -*-
# @Author: Xingmo


import cv2

img = cv2.imread('test.jpg')

# split 返回BGR三个通道
b,g,r = cv2.split(img)

# merged 通道合并
merge = cv2.merge([b,g,r])
cv2.imshow('merge',merge)

#cv2.imshow("Red", r)
#cv2.imshow("Green", g)
#cv2.imshow("Blue", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
