import cv2
import numpy as np

#访问元素

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 0
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img


if __name__ == '__main__':
    img1 = cv2.imread("img\\test.jpg")
    saltImage = salt(img1, 500)
    cv2.imshow("Salt", saltImage)
    cv2.imwrite('salt.jpg', saltImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
