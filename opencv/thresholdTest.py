import cv2
img = cv2.imread('threshold.jpg', 50)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 膨胀图像 cv2.dilate(图像,元素结构)
dilate = cv2.dilate(img, element)

# 腐蚀图像 cv2.erode(图像,元素结构)
erode = cv2.erode(img, element)

result = cv2.absdiff(dilate, erode)
result = cv2.bitwise_not(result)
dd = cv2.dilate(result, element)
cv2.imshow("dd", dd)
retval, result = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

