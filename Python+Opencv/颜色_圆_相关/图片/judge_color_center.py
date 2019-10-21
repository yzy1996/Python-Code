# 该程序是为了判断给定图片的主要颜色，并找到主要颜色的质心
# 思路为：用不同颜色进行过滤，求出每种颜色滤波后的面积，找到最大面积的滤波颜色为目标颜色，然后找到质心

import cv2
import colorList

def getColor(frame):
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	maxsum = 0
	color = None
	color_dict = colorList.getColorList()

	# 对每个颜色进行判断
	for d in color_dict:
		# 根据阈值构建掩膜
		mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
		# 腐蚀操作
		mask = cv2.erode(mask, None, iterations=2)
		# 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
		mask = cv2.dilate(mask, None, iterations=2)	
		img, cnts, hiera = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		# 有轮廓才进行后面的判断
		if len(cnts) > 0:	
			# 计算识别区域的面积
			sum = 0
			for c in cnts:
				sum += cv2.contourArea(c)
			
			# 找到最大面积并找到质心
			if sum > maxsum :
				maxsum = sum	
				if maxsum != 0:
					color = d
				else:
					color = None
				# 找到面积最大的轮廓
				c = max(cnts, key = cv2.contourArea)
				# 确定面积最大的轮廓的外接圆
				((x, y), radius) = cv2.minEnclosingCircle(c)
				# 计算轮廓的矩
				M = cv2.moments(c)
				# 计算质心
				center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
 
	return color, center
 
if __name__ == '__main__':
	filename = '22.bmp' 
	frame = cv2.imread(filename)
	print('判断主要颜色为：', getColor(frame)[0], '圆心为：', getColor(frame)[1])