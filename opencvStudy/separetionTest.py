import cv2
import numpy as np

#分离图像


img = cv2.imread('img\\test.jpg')
#b = np.zeros((img.shape[0], img.shape[1]), dtype = img.dtype)
#g = np.zeros((img.shape[0], img.shape[1]), dtype = img.dtype)
#r = np.zeros((img.shape[0], img.shape[1]), dtype = img.dtype)

#b[:, :] = img[:, :, 0]
#g[:, :] = img[:, :, 1]
#r[:, :] = img[:, :, 2]

b = cv2.split(img)[0]
g = cv2.split(img)[1]
r = cv2.split(img)[2]



merged = cv2.merge([b, g, r])
print("Merge by OpenCV")
print(merged.strides)

mergedByNp = np.dstack([b, g, r])

print("Merge by NumPy ")
print(mergedByNp.strides)
#NumPy数组的strides属性表示的是在每个维数上以字节计算的步长。

cv2.imshow("Blue", b)
cv2.imshow("Red", g)
cv2.imshow("Green", r)
cv2.imshow("img", img)
#cv2.imshow("merged", merged)
#cv2.imshow("mergedByNp", mergedByNp)
cv2.waitKey(0)
cv2.destroyAllWindows()
