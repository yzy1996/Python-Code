import cv2
import pyautogui
from pynput.mouse import Button, Controller

## 使用pynput库进行控制
mouse = Controller()
print('鼠标位置', mouse.position)

#获取屏幕的尺寸
print('屏幕尺寸', pyautogui.size())

#获取当前鼠标的位置

print('鼠标位置', pyautogui.position())
