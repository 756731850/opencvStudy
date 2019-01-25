import cv2
import numpy


img = cv2.imread('img\\ttt.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

print(cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE))
h = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(h) )

cv2.drawContours(img, h[1], -1, (0, 0, 255), 3)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

