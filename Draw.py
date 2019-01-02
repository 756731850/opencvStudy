# -*- coding: utf-8 -*-
# @Author: Xingmo

####### 说明 #######
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate ]]) #返回hist
# 第一个参数为读取的图像，必须用方括号括起来。
# 第二个参数是用于计算直方图的通道，这里使用灰度图计算直方图，所以就直接使用第一个通道；
# 第三个参数是Mask，这里没有使用，所以用None。
# 第四个参数是histSize，表示这个直方图分成多少份（即多少个直方柱）。第二个例子将绘出直方图，到时候会清楚一点。
# 第五个参数是表示直方图中各个像素的值，[0.0, 256.0]表示直方图能表示像素值从0.0到256的像素。
# 最后是两个可选参数，由于直方图作为函数结果返回了，所以第六个hist就没有意义了（待确定）
# 最后一个accumulate是一个布尔值，用来表示直方图是否叠加。
#######
# cv.PolyLine(img, polys, is_closed, color, thickness=1, lineType=8, shift=0)  # 返回None
# img        读取的图像
# polys      多边形曲线的数组(各个坐标点)
# is_closed  绘制的折线是否关闭的标志,起始点是否有线连接，False为没有
# color      折线的颜色 [b,g,r]
# thickness  折线边缘的厚度
# lineType   线段的类型
# shift      顶点坐标中的小数位数
########   说明END   #######


import cv2
import numpy as np


# 将直方图(填充)转化为图片
def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0.0,255.0])
    # cv2.minMaxLoc 最大值maxVal和最小值minVal及它们的位置
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    # 创建全零图像
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.95* 256);

    for h in range(256):
        # hpt=0.95*256 0.95防止最大值为整张图片的高，每个hist与最大值的比*(256*0.95)即可表示该hist在图片中的高度
        intensity = int(hist[h]*hpt/maxVal)
        # cv2.line(图像img，第一个点坐标(x1,y1)，第二个点坐标(x2,y2)，颜色[b,g,r])
        cv2.line(histImg,(h,256), (h,256-intensity), color)

    return histImg

# 将直方图(折线)转化为图片
def DrawHist(img):
    # 建立空图片
    h = np.zeros((256,256,3))
    # 直方图中各bin的顶点位置
    bins = np.arange(256).reshape(256,1)
    # BGR三种颜色
    color = [ (255,0,0),(0,255,0),(0,0,255) ]

    for ch, col in enumerate(color):
        originHist = cv2.calcHist([img],[ch],None,[256],[0,256])
        # cv2.normalize(图像img,输出图像,归一化后最低值,归一化后最大值,规范化类型 cv2.NORM_MINMAX:仅针对密集阵列)
        cv2.normalize(originHist, originHist,0,255*0.9,cv2.NORM_MINMAX)
        # np.around(array) 取整数，但数据类型仍为float
        hist=np.int32(np.around(originHist))
        # np.column_stack 将两个1-D数组作为列堆叠成2维数组
        pts = np.column_stack((bins,hist))
        # cv2.polylines(图像img,多边形曲线的数组,绘制的折线是否关闭的标志,折线颜色)
        cv2.polylines(h,[pts],False,col)
    # np.flipud 在上/下方向翻转数组。
    h=np.flipud(h)
    return h
'''
####### 灰度图像———直方图(填充) #######
img = cv2.imread('001.jpg',0)
histimg = calcAndDrawHist(img,[255,255,255])
cv2.imshow('hist',histimg)
cv2.waitKey(0)
'''

####### 彩色图像———直方图(填充) #######
if __name__ == '__main__':
    # 读取图片
    img = cv2.imread("001.jpg")
    # cv2.spilt 返回BGR三个通道
    b, g, r = cv2.split(img)

    # calcAndDrawHist(图像img，color填[b,g,r])
    histImgB = calcAndDrawHist(b, [255, 0, 0])
    histImgG = calcAndDrawHist(g, [0, 255, 0])
    histImgR = calcAndDrawHist(r, [0, 0, 255])

    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    cv2.imshow("Img", img)
####### 彩色图像———直方图(折线) #######
if __name__ == '__main__':
    img = cv2.imread("test.jpg")
    h = DrawHist(img)
    cv2.imshow('colorhist',h)


cv2.waitKey(0)
cv2.destroyAllWindows()
