import cv2
import numpy as np

'''
#低通滤波
#低通滤波器的目标是降低图像的变化率。
# 如将每个像素替换为该像素周围像素的均值。
# 这样就可以平滑并替代那些强度变化明显的区域。
# 在OpenCV中，可以通过blur函数做到这一点
#dst = cv2.blur(image,(5,5));
'''


img = cv2.imread('img/test.jpg')
result = cv2.blur(img, (5, 5))

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
