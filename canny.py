# -*- coding: utf-8 -*-
# @Author: Xingmo

####### cv2.Canny 说明 #######
# cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) 返回edges(边缘图)
# image          原图像，该图像必须为单通道的灰度图
# threshold1     第一个阈值
# threshold2     第二个阈值
# apertureSize   Sobel算子的孔径大小，其有默认值3
# L2gradient     是否使用L2范数，一个计算图像梯度幅值的标识，默认值false
####### cv2.Canny 说明END #######

import cv2
import numpy as np

# 读取图片
img = cv2.imread('canny.jpg', 0)
# 高斯模糊
blur = cv2.GaussianBlur(img,(3,3),0)
canny = cv2.Canny(blur, 50, 200)

# 图像显示
cv2.imshow('origin',img)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
