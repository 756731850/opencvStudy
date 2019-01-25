import cv2
import numpy as np
#保存图片


img = cv2.imread('img\\test.jpg')
cv2.imwrite('img\\cpy_test.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

cv2.imshow('copyImg', cv2.imread('img\\cpy_test.jpg'))
cv2.waitKey(0)
cv2.destroyAllWindows()
