# 拾色器
# 该程序是为了拾取颜色，可以输出BGR、HSV、GRAY等格式

import cv2

# 定义鼠标交互函数
def mouseColor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('HSV:', hsv[y, x])  #输出图像坐标(x,y)处的HSV的值

img = cv2.imread('0.jpg')  #读进来是BGR格式
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #变成HSV格式
cv2.namedWindow("Color Picker")
cv2.setMouseCallback("Color Picker", mouseColor)
cv2.imshow("Color Picker", img)
if cv2.waitKey(0):
    cv2.destroyAllWindows()



