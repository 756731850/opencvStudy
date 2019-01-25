import cv2
import numpy as np

#复制图片

img = cv2.imread('img\\test.jpg')

emptyImg = np.zeros(img.shape, np.uint8)
emptyImg2 = img.copy

emptyImg3 = img.copy()

emptyImg4 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("emptyImg4", emptyImg4)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
