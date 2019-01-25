import cv2

sheet = cv2.imread("timg.jpg", 30)

#图片转成灰度值图片
sheet2 = cv2.cvtColor(sheet, cv2.COLOR_BGR2GRAY)

#图片二值化
retval, sheet3 = cv2.threshold(sheet2, 180, 255, cv2.THRESH_BINARY_INV)

element = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

#膨胀
dilate = cv2.dilate(sheet3, element)

#腐蚀
erode = cv2.erode(sheet3, element)

result = cv2.absdiff(dilate, erode)

cv2.imshow("result", result)

#sheet = cv2.pyrMeanShiftFiltering(sheet, 15, 10)





cv2.waitKey(0)
cv2.destroyAllWindows()
