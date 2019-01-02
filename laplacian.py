# -*- coding: utf-8 -*-
# @Author: Xingmo

#######  cv2.Laplacian 说明 #######
# cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) #返回dst(处理后图像)
# src        图像
# ddepth     输出图像深度
#            S = 符号整型  U = 无符号整型  F = 浮点型
#            src.depth()= CV_8U，ddepth= -1 / CV_16S/ CV_32F/CV_64F
#            src.depth()= CV_16U/ CV_16S，ddepth= -1 CV_32F//CV_64F
#            src.depth()= CV_32F，ddepth= -1 CV_32F/CV_64F
#            src.depth()= CV_64F，ddepth= -1 /CV_64F
#            何时ddepth=-1，目的地图像将具有与源相同的深度
# dst        输出图像
# ksize      用于计算二阶微分滤波器的孔径大小，其大小必须是正数和奇数
# scale      缩放导数的比例常数，默认情况下没有伸缩系数
# delta      在结果存储之前添加到结果中的可选增量值，默认情况下没有额外的值加到dst中
# borderType 判断图像边界的模式。这个参数默认值为cv2.BORDER_DEFAULT
#######  cv2.Laplacian 说明END #######

import cv2
import numpy as np

# 图像读取
img = cv2.imread("laplacian.jpg", 0)

gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)
# cv2.convertScaleAbs 在输入数组的每个元素上，该函数依次执行三个操作：缩放，取绝对值，转换为无符号8位类型
# 转回uint8
dst = cv2.convertScaleAbs(gray_lap)

# 图像显示
cv2.imshow('origin',img)
cv2.imshow('laplacian',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
