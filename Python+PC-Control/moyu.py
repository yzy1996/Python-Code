# 摸鱼脚本：鼠标划拉划拉

from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
import time

mouse_move = Controller()

def move(t=10):
    mouse_move.move(10, 10)
    time.sleep(t)
    mouse_move.move(-10, -10)
    time.sleep(t)

def on_click(x, y, button, pressed):
    while True:2e
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()