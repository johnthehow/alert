import psutil
import time
import os
from pathlib import Path
import datetime


def change_monitor(pid,git_repo_path,time_interval):
	start_time = time.time()
	while psutil.pid_exists(pid):
		time.sleep(1)
		continue
	else:
		os.system(f'git -C "{git_repo_path}" pull')
		time.sleep(10)
		with open(git_repo_path.joinpath('README.md'),mode='a+',encoding='utf-8') as file:
			file.write(str(datetime.datetime.now()))
			file.write('\r\n')
			file.write(__file__)
			file.write('\r\n')
		os.system(f'git -C "{git_repo_path}" add .')
		os.system(f'git -C "{git_repo_path}" commit -m "process terminated."')
		os.system(f'git -C "{git_repo_path}" push')
	return

if __name__ == '__main__':
	print('''
		Attention:\n
		1. the process must exist before the running of this monitor \n
		''')
	pid = int(input('input pid of the process to be monitored: \n'))
	git_repo_path = Path(__file__).parent
	time_interval = 1
	
	change_monitor(pid, git_repo_path, time_interval)





