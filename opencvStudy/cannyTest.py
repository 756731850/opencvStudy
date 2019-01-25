import cv2


#Canny边缘检测

img = cv2.imread('img\\test.jpg')

img = cv2.GaussianBlur(img, (3, 3), 0)
canny = cv2.Canny(img, 50, 150)

cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
