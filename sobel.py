# -*- coding: utf-8 -*-
# @Author: Xingmo

####### cv2.sobel说明 #######
# cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) #返回dst(处理后图像)
# scr      图像
# ddepth   输出图像深度
#          S = 符号整型  U = 无符号整型  F = 浮点型
#          src.depth()= CV_8U，ddepth= -1 / CV_16S/ CV_32F/CV_64F
#          src.depth()= CV_16U/ CV_16S，ddepth= -1 CV_32F//CV_64F
#          src.depth()= CV_32F，ddepth= -1 CV_32F/CV_64F
#          src.depth()= CV_64F，ddepth= -1 /CV_64F
#          何时ddepth=-1，目的地图像将具有与源相同的深度
# dx
# dy
####### cv2.sobel说明END #######

import cv2
import numpy as np

img = cv2.imread('sobel.jpg', 0)

x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)

# cv2.convertScaleAbs 在输入数组的每个元素上，该函数依次执行三个操作：缩放，取绝对值，转换为无符号8位类型
# 转回uint8
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

# cv2.addWeighted(src1 , alpha, src2 , beta , gamma[, dst[, dtype]]) #返回dst(处理后图像)
# cv2.addWeighted(输入1, 分量1, 输入2, 分量2, 标量)
# dst = src1*alpha + src2*beta + gamma
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)

# 图像显示
cv2.imshow('origin',img)
cv2.imshow("absX", absX)
cv2.imshow("absY", absY)
cv2.imshow("Result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
