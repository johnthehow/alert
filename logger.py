from pathlib import Path
import time
import datetime
import os




def change_monitor(log_file_path,git_repo_path,time_interval,max_time):
	start_time = time.time()
	while True:
		now_time = time.time()
		if now_time - start_time <= max_time:
			print(f'time elapsed: {int(now_time - start_time)} seconds',end='\x1b\r')
			last_update_time = os.path.getmtime(log_file_path)
			time.sleep(time_interval)
			now_update_time = os.path.getmtime(log_file_path)
			if now_update_time == last_update_time:
				pass
			else:
				with open(log_file_path,mode='r',encoding='utf-8') as file:
					lines = file.readlines()
					if len(lines) != 0:
						last_line = lines[-1]
						print('---------------------------')
						log_update_time = f'Log updated at {datetime.datetime.now()}'
						print(log_update_time)
						log_last_line = f'Last line: \n {last_line}'
						print(log_last_line)
						os.system(f'git -C "{git_repo_path}" pull')
						time.sleep(10)
						os.system(f'git -C "{git_repo_path}" add .')
						os.system(f'git -C "{git_repo_path}" commit -m "{log_update_time} with {log_last_line}"')
						os.system(f'git -C "{git_repo_path}" push')
					else:
						last_line = ''
						print('---------------------------')
						log_update_time = f'Log updated at {datetime.datetime.now()}'
						print(log_update_time)
						log_last_line = f'Last line: \n {last_line}'
						print(log_last_line)
						os.system(f'git -C "{git_repo_path}" pull')
						time.sleep(10)
						os.system(f'git -C "{git_repo_path}" add .')
						os.system(f'git -C "{git_repo_path}" commit -m "{log_update_time} with {log_last_line}"')
						os.system(f'git -C "{git_repo_path}" push')
		else:
			log_max_time = f'Max monitoring time {max_time} seconds reached at {datetime.datetime.now()}'
			print(log_max_time)
			os.system(f'git -C "{git_repo_path}" pull')
			time.sleep(10)
			os.system(f'git -C "{git_repo_path}" add .')
			os.system(f'git -C "{git_repo_path}" commit -m "{log_update_time} with {log_last_line}"')
			os.system(f'git -C "{git_repo_path}" push')
			time.sleep(20)
			break

if __name__ == '__main__':
	log_file_path = Path(input('Paste log file path here: \n'))
	git_repo_path = Path(__file__).parent
	# time_interval = float(input('Input time interval here(in secs): \n'))
	time_interval = 0.1
	max_time = int(input('Input maximum monitoring time here (in secs): \n'))

	change_monitor(log_file_path, git_repo_path, time_interval, max_time)
