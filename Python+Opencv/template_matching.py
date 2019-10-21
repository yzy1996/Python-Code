# 2D图片的匹配

import cv2
import numpy as np
import math

image = cv2.imread("0.jpg")

image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

comple = cv2.imread("1.jpg",0)
# shape()得到的是行*列，所以需要倒序转换一下
w,h = comple.shape[::-1]
# 匹配比较
res = cv2.matchTemplate(image2, comple, cv2.TM_CCOEFF_NORMED)
# 设置阈值
threshold = 0.39
# 找到大于阈值的部分，返回值是坐标
loc = np.where(res >= threshold)
# *号是一个逆操作，二维[::-1]是将 行 倒序（最后一行变成了第一行）
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (255, 0, 255), 2)

cv2.imshow('result', image)

cv2.waitKey(0)
cv2.destroyAllWindows()