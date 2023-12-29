from pynput.mouse import Listener
import time
import os
import datetime

# Flag to indicate whether to monitor mouse movements
monitor_mouse = True

# Function to be called when the mouse is moved
def on_move(x, y):
    global monitor_mouse
    # Stop monitoring after the first movement
    monitor_mouse = False
    return False

# Create a mouse listener
while True:
    with Listener(on_move=on_move) as listener:
        # Keep the listener running as long as monitoring is enabled
        listener.join()

    # print("Mouse movement detected.")
    print('next detection in 60 secs')
    os.system(f'echo mouse movement detected>C:\\Users\\dell\\Desktop\\thehow\\PYTHON\\thehow_codes\\progmon\\{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.txt')
    time.sleep(3)
    os.system('git -C "C:\\Users\\dell\\Desktop\\thehow\\PYTHON\\thehow_codes\\progmon" add .')
    time.sleep(1)
    os.system('git -C "C:\\Users\\dell\\Desktop\\thehow\\PYTHON\\thehow_codes\\progmon" commit -m "mouse move detected"')
    time.sleep(1)
    os.system('git -C "C:\\Users\\dell\\Desktop\\thehow\\PYTHON\\thehow_codes\\progmon" push')
    # os.system('msg * 如须使用/关闭此计算机,请务必联系13592023682')
    time.sleep(60)
    monitor_mouse=True