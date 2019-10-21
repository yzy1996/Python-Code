# 该程序为了找到图片中特定颜色的圆，返回圆心坐标，并标出圆
# 通过的是霍夫圆

import cv2
import numpy as np
import time
import color_list

def findPiccircle(frame, color):

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	
	color_dict = color_list.getColorList()
	mask = cv2.inRange(hsv, color_dict[color][0], color_dict[color][1])
	dilated = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
	## 需要修改minRadius以及maxRadius，用来限制识别圆的大小，排除其他的干扰
	circles = cv2.HoughCircles(dilated, cv2.HOUGH_GRADIENT, 1, 1000, param1=15, param2=10, minRadius=15, maxRadius=50)
	
	center = None
	if circles is not None:
		x, y, radius = circles[0][0]
		center = (x, y)
		cv2.circle(frame, center, radius, (0, 255, 0), 2)
		cv2.circle(frame, center, 2, (0,255,0), -1, 8, 0 );
		print('圆心：{}, {}'.format(x, y))
		
	cv2.imshow('result', frame)	
	
	if center != None:
		return center
	
			
if __name__ == '__main__':
	filename ='22.bmp'   ##修改为图片
	color = 'black'      ##修改颜色
	frame = cv2.imread(filename)
	findPiccircle(frame, color)
	cv2.waitKey(0)
