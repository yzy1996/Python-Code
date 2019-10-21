import cv2
import numpy as np
import time

cap = cv2.VideoCapture(3)


# color from website:https://blog.csdn.net/taily_duan/article/details/51506776
#black
low_range = np.array([0, 0, 0])
high_range = np.array([180, 255, 46])

#red

while(1):
    # get a frame and show
    ret, frame = cap.read()

    # change to hsv model
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get mask
    mask = cv2.inRange(hsv, low_range, high_range)
    dilated = cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)

    # detect red
    circles = cv2.HoughCircles(dilated, cv2.HOUGH_GRADIENT, 1, 1000, param1=15, param2=10, minRadius=0, maxRadius=50)

    if circles is not None:
        x, y, radius = circles[0][0]
        center = (x, y)
        cv2.circle(frame, center, radius, (0, 255, 0), 2)
        cv2.circle(frame, center, 2, (0,255,0), -1, 8, 0 );
        print('圆心：{}, {}'.format(x, y))

    cv2.imshow('result', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()