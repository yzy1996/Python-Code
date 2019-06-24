import cv2
import numpy as np
#创建一个大小800*800的空帧
frame = np.zeros((800,800,3),np.uint8)
#初始化测量坐标和鼠标运动预测的数组
last_measurement = current_measurement = np.array((2,1),np.float32)
print(last_measurement)
last_predicition = current_prediction = np.zeros((2,1),np.float32)
'''
    mousemove()函数在这里的作用就是传递X,Y的坐标值，便于对轨迹进行卡尔曼滤波
'''
def mousemove(event,x,y,s,p):
    #定义全局变量
    global frame,current_measurement,measurements,last_measurement,current_prediction,last_prediction
    #初始化
    last_measurement = current_measurement
    last_prediction = current_prediction
    #传递当前测量坐标值
    current_measurement = np.array([[np.float32(x)],[np.float32(y)]])
    #用来修正卡尔曼滤波的预测结果
    kalman.correct(current_measurement)
    # 调用kalman这个类的predict方法得到状态的预测值矩阵，用来估算目标位置
    current_prediction = kalman.predict()
    #上一次测量值
    lmx,lmy = last_measurement[0],last_measurement[1]
    #当前测量值
    cmx,cmy = current_measurement[0],current_measurement[1]
    #上一次预测值
    lpx,lpy = last_prediction[0],last_prediction[1]
    #当前预测值
    cpx,cpy = current_prediction[0],current_prediction[1]
    #绘制测量值轨迹（绿色）
    cv2.line(frame,(lmx,lmy),(cmx,cmy),(0,100,0))
    #绘制预测值轨迹（红色）
    cv2.line(frame,(lpx,lpy),(cpx,cpy),(0,0,200))

cv2.namedWindow("kalman_tracker")

cv2.setMouseCallback("kalman_tracker",mousemove)

kalman = cv2.KalmanFilter(4,2)  # 状态空间的维数 和 测量值维数
#设置测量矩阵
kalman.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
#设置转移矩阵
kalman.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],np.float32)
#设置过程噪声协方差矩阵
kalman.processNoiseCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],np.float32)*0.03

while True:
    cv2.imshow("kalman_tracker",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
