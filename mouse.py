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
    with open(log_path,mode='a',encoding='utf-8') as log_file:
        log_file.write(f'[{datetime.datetime.now()}] mouse movement detected\n')
        try:
            msg = f'try to pull without proxy at {datetime.datetime.now()}\n'
            print(msg)
            log_file.write(msg)
            log_file.flush()
            subprocess.run('git config --global --unset-all http.proxy')
            subprocess.run('git config --global --unset-all https.proxy')
            subprocess.run('git pull',check=True, timeout=20)
        except subprocess.CalledProcessError:
            msg = f'failed to pull without proxy, trying to pull with proxy\n'
            print(msg)
            log_file.write(msg)
            log_file.flush()
            subprocess.run('git config --global https.proxy https://127.0.0.1:1080')
            subprocess.run('git config --global http.proxy http://127.0.0.1:1080')
            subprocess.run('git pull',check=True, timeout=20)
        except subprocess.TimeoutExpired:
            msg = f'failed to pull with/without proxy: timeout, subsequent codes discarded.\n'
            print(msg)
            log_file.write(msg)
            log_file.flush()
            subprocess.run('git config --global --unset-all http.proxy')
            subprocess.run('git config --global --unset-all https.proxy')
            continue
        except:
            msg = f'failed to pull with/without proxy, subsequent codes discarded.\n'
            print(msg)
            log_file.write(msg)
            log_file.flush()
            subprocess.run('git config --global --unset-all http.proxy')
            subprocess.run('git config --global --unset-all https.proxy')
            continue

        msg = f'trying to push at {datetime.datetime.now()}\n'
        print(msg)
        log_file.write(msg)
        log_file.flush()
        try:    
            subprocess.run('git add .')
            time.sleep(5)
            subprocess.run('git commit -m "scheduled push"')
            time.sleep(5)
            subprocess.run('git push', check=True, timeout=20)
            subprocess.run('git config --global --unset-all http.proxy')
            subprocess.run('git config --global --unset-all https.proxy')
        except:
            msg = f'push failed at {datetime.datetime.now()}\n'
            print(msg)
            log_file.write(msg)
            log_file.flush()
            subprocess.run('git config --global --unset-all http.proxy')
            subprocess.run('git config --global --unset-all https.proxy')
        else:
            msg = f'push done at {datetime.datetime.now()}\n'
            print(msg)
            log_file.write(msg)
            log_file.flush()
            subprocess.run('git config --global --unset-all http.proxy')
            subprocess.run('git config --global --unset-all https.proxy')
    time.sleep(60)
    monitor_mouse=True