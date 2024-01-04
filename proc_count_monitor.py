import subprocess
import time

proc_name = input('process name: ')
stdout, stderr = subprocess.Popen(['powershell.exe', '-Command', f'(Get-Process -Name {proc_name}).Count'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate()
print(f'current # instances of {proc_name}: {stdout}')
alert_threshold = input('alert when process count <=: ')

start_time = time.time()


# Run the PowerShell command

while int(stdout) > int(alert_threshold):
	stdout, stderr = subprocess.Popen(['powershell.exe', '-Command', f'(Get-Process -Name {proc_name}).Count'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate()
	print(stdout)
	time.sleep(10)

end_time = time.time()
duration = end_time-start_time
print(f'proc {proc_name} num lower than {alert_threshold}.')
os.system(f'git -C "{git_repo_path}" pull')
time.sleep(20)
with open(git_repo_path.joinpath('README.md'),mode='a+',encoding='utf-8') as file:
	file.write('\r\n')
	file.write(f'process {pid} terminated at {datetime.datetime.now()}, duration: {duration} secs.')
	file.write('\r\n')
os.system(f'git add .')
os.system(f'git commit -m "proc {proc_name} num lower than {alert_threshold}, duration: {duration} secs."')
os.system(f'git push')