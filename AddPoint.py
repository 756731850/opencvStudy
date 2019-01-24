# -*- coding: utf-8 -*-
# @Author: Xingmo

import cv2
import numpy as np

#git test

# 添加椒盐噪声
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
    # 读取图片
    img = cv2.imread('test.jpg')
    # 添加噪声
    saltImage = salt(img)
    # 图片显示
    cv2.imshow("Salt", saltImage)
    # 图片保存
    cv2.imwrite('salt.jpg',saltImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
