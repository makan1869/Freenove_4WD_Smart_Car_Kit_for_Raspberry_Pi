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

files = os.listdir('pictures')
files.sort(reverse=True)
for file in files:
    if file.endswith("original.jpg"):
        img = cv2.imread("pictures/%s"%file, cv2.IMREAD_COLOR)
        line = cv2.imread(("pictures/%s"%file).replace("original.jpg","lines.jpg"), cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray', gray)
        cv2.imshow('Lines', line)
        cv2.waitKey(0)

cv2.destroyAllWindows()
