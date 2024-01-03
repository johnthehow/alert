import psutil
import time
import os
from pathlib import Path
import datetime


def change_monitor(pid,git_repo_path,time_interval):
	start_time = time.time()
	while psutil.pid_exists(pid):
		time.sleep(time_interval)
		continue
	else:
		end_time = time.time()
		duration = end_time-start_time
		print(f'process {pid} no longer exist.')
		os.system(f'git -C "{git_repo_path}" pull')
		time.sleep(20)
		with open(git_repo_path.joinpath('README.md'),mode='a+',encoding='utf-8') as file:
			file.write('\r\n')
			file.write(f'process {pid} terminated at {datetime.datetime.now()}, duration: {duration} secs.')
			file.write('\r\n')
		os.system(f'git -C "{git_repo_path}" add .')
		os.system(f'git -C "{git_repo_path}" commit -m "process {pid} terminated, duration: {duration} secs."')
		os.system(f'git -C "{git_repo_path}" push')
	return

if __name__ == '__main__':
	git_repo_path = Path(__file__).parent
	print(f'''
		Attention:\n
		1. the process must exist before the running of this monitor \n
		2. the pid_monitory checks if a process is running every <time_interval> secs \n
		3. git repo path: {git_repo_path}
		''')
	pid = int(input('pid of the process to be monitored: \n'))
	time_interval = int(input('interval per check in secs: \n'))
	
	change_monitor(pid, git_repo_path, time_interval)





