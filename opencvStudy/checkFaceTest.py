import cv2
import numpy as py


#检测拐角
#与边缘检测不同，拐角的检测的过程稍稍有些复杂
# 。但原理相同，所不同的是先用十字形的结构元素膨胀像素，
# 这种情况下只会在边缘处“扩张”，角点不发生变化。
# 接着用菱形的结构元素腐蚀原图像，
# 导致只有在拐角处才会“收缩”，而直线边缘都未发生变化。

image = cv2.imread('img\\building.jpg', 0)
origin = cv2.imread('img\\building')

#构造5 * 5的结构元素，分别为十字形/菱形/方形/X形
cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
#菱形结构元素的定义
diamond = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0

square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
x = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
#使用cross膨胀图像
result1 = cv2.dilate(image, cross)
#使用菱形腐蚀图像
result1 = cv2.erode(image, diamond)

#使用X膨胀原图像
result2 = cv2.dilate(image, x)
#使用方形腐蚀图像
result2 = cv2.erode(image, square)

#将两幅闭运算的图像相减获得角
result = cv2.absdiff(result2, result1)
#使用阈值获得二值图
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)

#在原图上用半径为5的圆圈将点标出
for j in range(result.size):
    y = int(j / result.shape[0])
    x = j % result.shape[0]

    if result[x, int(y)] == 255:
        cv2.circle(image, (int(y), x), 5, (255, 0, 0))

cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


