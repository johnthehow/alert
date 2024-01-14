from pynput.mouse import Listener
import time
import os
import subprocess
import datetime

# Flag to indicate whether to monitor mouse movements
monitor_mouse = True

log_path = './log/mousemove.txt'

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
    with open(log_path,mode='a',encoding='utf-8') as logfile:
        logfile.write(f'[{datetime.datetime.now()}] mouse movement detected\n')
    # os.system(f'echo mouse movement detected>.\\mouse_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.txt')
    time.sleep(3)
    os.system(f'git -C "{os.getcwd()}" add .')
    time.sleep(1)
    os.system(f'git -C "{os.getcwd()}" commit -m "mouse move detected"')
    time.sleep(1)
    os.system(f'git -C "{os.getcwd()}" push')
    time.sleep(60)
    monitor_mouse=True