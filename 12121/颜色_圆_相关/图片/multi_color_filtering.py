# 按照选择的多种颜色对图片进行过滤

import  cv2
import numpy as np
import colorList

def get_color(frame, color1, color2):
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	color_dict = colorList.getColorList()
	mask1 = cv2.inRange(hsv, color_dict[color1][0], color_dict[color1][1])
	mask2 = cv2.inRange(hsv, color_dict[color2][0], color_dict[color2][1])
	mask = mask1 + mask2
	cv2.imwrite(filename + color1 + color2 + '.jpg', mask)

if __name__ == '__main__':
	filename ='222.jpg'
	color1 = 'blue'
	color2 = 'red'
	frame = cv2.imread(filename)
	get_color(frame, color1, color2)