from pynput import mouse


def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
