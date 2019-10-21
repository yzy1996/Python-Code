# 该程序是为了判断出图片中的主要颜色（不只一种）
# 思路为：用不同颜色进行过滤，求出每种颜色滤波后的面积，找到最大面积的几个确定为主要颜色

import cv2
import numpy as np
import color_list
import heapq


def getColor(frame, count_color):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color = []

    color_dict = color_list.getColorList()

    # 颜色字典的颜色数量
    num_color = len(color_dict)
    sum = [0] * num_color
    search_color_list = []
    # 对每个颜色进行判断，d是颜色字符串（如：red）
    for (d, i) in zip(color_dict, range(num_color)):
        
        search_color_list.append(d)
        # 根据阈值构建掩膜
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        # 腐蚀操作
        mask = cv2.erode(mask, None, iterations=2)
        # 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
        mask = cv2.dilate(mask, None, iterations=2)
        img, cnts, hiera = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)
        # 有轮廓才进行后面的判断
        
        if len(cnts) > 0:
            for c in cnts:
                sum[i] += cv2.contourArea(c)

    find_color_list = heapq.nlargest(count_color, sum)
    for j in range(count_color):     
        color.append(search_color_list[sum.index(find_color_list[j])])

    return color


if __name__ == '__main__':

    # 设定要检测的图片
    filename = '111.jpg'
    # 设定要检测的颜色数量
    count_color = 3

    frame = cv2.imread(filename)

    print('判断主要的' + str(count_color) + '个颜色为：', ' '.join(getColor(frame, count_color)))
