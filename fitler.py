# -*- coding: utf-8 -*-
# @Author: Xingmo

import cv2
import numpy as np

######## 线性过滤器 #######
# 低通滤波(平滑图像)
# cv2.blur(图像,滤波器大小(num,num))  #返回dst(处理后图像)
#
# cv2.boxFilter(图像, -1, 滤波器大小(num,num)) #返回dst(处理后图像)
# 第二个参数-1表示与原图相同
#
# 高斯模糊
# cv2.GaussianBlur(图像,滤波器大小(num,num),X方向的高斯内核标准偏差) #返回dst(处理后图像)
######## 线性过滤器END #######
#
######## 非线性过滤器 #######
# 中值滤波
# cv2.medianBlur(图像,滤波器大小num)
####### 非线性过滤器END #######

def salt(img):
    for k in range(100):
        # 建立图片随机坐标点
        i = int(np.random.random()*img.shape[0])
        j = int(np.random.random()*img.shape[1])
        # 图片为灰度图像，有二维
        if img.ndim == 2:
            img[i,j] = 255
        # 图片为彩色图片，有三维，RGB
        elif img.ndim == 3:
            img[i,j,0] = 255
            img[i,j,1] = 255
            img[i,j,2] = 255
    return img

if __name__ == '__main__':
    #
    img = cv2.imread('filter.jpg',0)
    salt =salt(img)

    # 低通滤波
    dst1 = cv2.blur(salt,(5,5))
    # boxFilter
    dst2 = cv2.boxFilter(salt,-1,(5,5))
    # 高斯模糊
    dst3 = cv2.GaussianBlur(salt,(5,5),1.5)
    # 中值滤波
    dst4 = cv2.medianBlur(salt,5)

    # 图像显示
    # 对于椒盐噪声而言，中值滤波效果是最好的，其他效果差不多
    cv2.imshow('salt',salt)
    cv2.imshow('blur',dst1)
    cv2.imshow('boxFilter',dst2)
    cv2.imshow('GaussianBlur',dst3)
    cv2.imshow('medianBlur',dst4)


cv2.waitKey(0)
cv2.destroyAllWindows()
