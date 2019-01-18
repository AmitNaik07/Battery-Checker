from pync import Notifier
import subprocess

#checks to see if the state of the battery is in dischage mode.
status =subprocess.Popen('pmset -g batt | grep -c "discharging"', shell=True, stdout=subprocess.PIPE).stdout
#checks the battery level.
rem =subprocess.Popen('pmset -g batt | grep -Eo "\d+%" | cut -d% -f1', shell=True, stdout=subprocess.PIPE).stdout
version =rem.read()
stat =status.read()
#print(stat.decode())
#print(version.decode())
if int(version.decode()) < 15 and int(stat.decode())==1:
	Notifier.notify('Insert Charger', title ='Battery Checker')
else:
	print("Battery level is okay.")	   
