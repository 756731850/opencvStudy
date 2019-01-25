import cv2
import numpy as np

#开运算和闭运算
#闭运算用来连接被误分为许多小块的对象，
# 而开运算用于移除由图像噪音形成的斑点。
# 因此，某些情况下可以连续运用这两种运算。
# 如对一副二值图连续使用 闭运算和开运算，
# 将获得图像中的主要对象。
# 同样，如果想消除图像中的噪声（即图像中的“小点”），
# 也可以对图像先用开运算后用闭运算，
# 不过这样也会消除一 些破碎的对象。

img = cv2.imread('img\\ttt.jpg', 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

#闭运算
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#显示腐蚀后的图像
cv2.imshow("Close", closed)


#开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("opened", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()
