import psutil
import time
import os
from pathlib import Path
import datetime


def change_monitor(pid,git_repo_path,time_interval,max_time):
	start_time = time.time()
	while True:
		now_time = time.time()
		if now_time - start_time <= max_time:
			time.sleep(time_interval)
			print(f'time elapsed: {int(now_time - start_time)} seconds',end='\x1b\r')
			ifexist = psutil.pid_exists(pid)
			if ifexist == False:
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
				break
			else:
				pass
		else:
			print('max time reached')
			os.system(f'git -C "{git_repo_path}" pull')
			time.sleep(10)
			with open(git_repo_path.joinpath('README.md'),mode='a+',encoding='utf-8') as file:
				file.write(str(datetime.datetime.now()))
				file.write('\n')
				file.write(__file__)
				file.write('\n')
			os.system(f'git -C "{git_repo_path}" add .')
			os.system(f'git -C "{git_repo_path}" commit -m "max time reached."')
			os.system(f'git -C "{git_repo_path}" push')
			break
	return

if __name__ == '__main__':
	print('''
		Attention:\n
		1. the process must exist before the running of this monitor \n
		''')
	pid = int(input('input pid of the process to be monitored: \n'))
	git_repo_path = Path(__file__).parent
	time_interval = 0.1
	max_time = int(input('Input maximum monitoring time here (in secs): \n'))
	
	change_monitor(pid, git_repo_path, time_interval, max_time)





