import cv2
import numpy as np


# 反相灰度图，将黑白阈值颠倒
def accessPiexl(img):
    height = img.shape[0]
    width = img.shape[1]
    for i in range(height):
        for j in range(width):
            img[i][j] = 255 - img[i][j]
    return img


# 反相二值化图像
# 图像二值化（ Image Binarization）
# 就是将图像上的像素点的灰度值设置为0或255，
# 也就是将整个图像呈现出明显的黑白效果的过程。
def accessBinary(img, threshold=128):
    img = accessPiexl(img)
    # 边缘膨胀，不加也可以
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    _, img = cv2.threshold(img, threshold, 0, cv2.THRESH_TOZERO)
    return img


path = '1.jpg'

img = cv2.imread(path)
# cv2.imshow('origin', img)
# img = accessBinary(img)
#
# cv2.imshow('accessBinary', img)
# cv2.imwrite("output.png", img)

img = accessBinary(img)
cv2.imshow('acccessPiexl', img)
cv2.imwrite("output.png", img)
cv2.waitKey(0)
