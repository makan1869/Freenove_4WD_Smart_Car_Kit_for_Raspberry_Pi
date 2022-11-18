import threading
import time
import cv2
import numpy as np
import os

# img = cv2.imread('video.jpg', cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ksize = (10, 10)
#
# # Using cv2.blur() method
# blur = cv2.blur(gray, ksize)
# ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
#
# # the window showing output images
# # with the corresponding thresholding
# # techniques applied to the input images
# cv2.imshow('Binary Threshold', thresh1)
# cv2.imshow('Binary Threshold Inverted', thresh2)
# cv2.imshow('Truncated Threshold', thresh3)
# cv2.imshow('Set to 0', thresh4)
# cv2.imshow('Set to 0 Inverted', thresh5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


ksize = (5,5)

files = os.listdir('pictures_1')
files.sort(reverse=False)
for file in files:
    if file.endswith("original.jpg"):
        img = cv2.imread("pictures/%s"%file, cv2.IMREAD_COLOR)
        rows, cols, _ = img.shape
        print(rows, cols)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.blur(gray, ksize)
        ret, white = cv2.threshold(blur, 130, 255, cv2.THRESH_TOZERO)
        edges = cv2.Canny(white, 50, 150, apertureSize=3)

        lines = cv2.HoughLinesP(edges, 3, np.pi / 180, 100, minLineLength=30, maxLineGap=10)
        print(lines)
        cond = np.logical_and(np.logical_or(lines[:, 0 , 1] >= 150, lines[:, 0, 3] >= 150), abs(lines[:, 0, 1] - lines[:, 0, 3]) > 10 )
        lines = lines[cond, :]
        if type(lines) is np.ndarray:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if y1 > 150 or y2 > 150:
                    cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow('Original', img)
        cv2.imshow('Gray', gray)
        # cv2.imshow('Edges', edges)
        # cv2.imshow('White', white)
        cv2.waitKey(0)

cv2.destroyAllWindows()
