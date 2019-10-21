# 为了找到图像中带有特定颜色的区域，画出区域外接圆和质心

import numpy as np
import cv2
import color_list

filename = '22.bmp'
color = 'black'
image = cv2.imread(filename)

#转到HSV空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#根据阈值构建掩膜
color_dict = color_list.getColorList()
mask = cv2.inRange(hsv, color_dict[color][0], color_dict[color][1])
#腐蚀操作
mask = cv2.erode(mask, None, iterations=2)
#膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
mask = cv2.dilate(mask, None, iterations=2)
#轮廓检测
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
#初始化瓶盖圆形轮廓质心
center = None
#如果存在轮廓
if len(cnts) > 0:
	#找到面积最大的轮廓
	c = max(cnts, key = cv2.contourArea)
	#确定面积最大的轮廓的外接圆
	((x, y), radius) = cv2.minEnclosingCircle(c)
	#计算轮廓的矩
	M = cv2.moments(c)
	#计算质心
	center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
	#只有当半径大于10时，才执行画图
	print(center)
	if radius > 10:
		cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
		cv2.circle(image, center, 5, (0, 0, 255), -1)

cv2.imshow('Image', image)
#键盘检测，检按q退出
cv2.waitKey(0)
