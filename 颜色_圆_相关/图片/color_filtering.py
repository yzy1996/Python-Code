# 按照选择的颜色对图片进行过滤

import cv2
import numpy as np
import color_list


def get_color(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_dict = color_list.getColorList()
    mask = cv2.inRange(hsv, color_dict[color][0], color_dict[color][1])
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 存储一张图片
    cv2.imwrite(filename + color + '.jpg', mask)
    # 展示一张图片
    cv2.imshow('Result', res)
    cv2.waitKey(0)
    

if __name__ == '__main__':
    filename = '33.bmp'
    color = 'black'
    frame = cv2.imread(filename)
    get_color(frame, color)
