import cv2
import numpy as np

# 读取图像
img = cv2.imread('black-white.jpg')

# 变微灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 大津法二值化
retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

# 腐蚀和膨胀是对白色部分而言的，膨胀，白区域变大，最后的参数为迭代次数
# dst = cv2.dilate(dst, None, iterations=2)

# # 腐蚀，白区域变小
dst = cv2.erode(dst, None, iterations=2)

cv2.imshow('dst', dst)

cv2.waitKey(0)