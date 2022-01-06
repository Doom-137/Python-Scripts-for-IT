from threading import Thread
import requests
import time
import smtplib
import sys
from email.mime.text import MIMEText
import os
import random

requests.packages.urllib3.disable_warnings()

cwd = os.getcwd()
emoji_list = [u"\U0001F614", u"\U0001F625", u"\U0001F616", u"\U0001F641", u"\U0001F61E"]

csds_file = "\\configuration_files\\clients.csds"

def update_randomize(list_e):
	return random.choice(list_e)

def create_dict_from_file(file_name, split_str):
	temp_dictionary = {}
	with open(file_name) as f:
		for line in f:
			key, val = line.split(split_str)
			temp_dictionary[key] = val
	return temp_dictionary

def send_email(input_message, email_to, client):
	gmail_user = ''
	gmail_pwd = ''
	
	msg = MIMEText(input_message)
	
	msg['Subject'] = update_randomize(emoji_list)
	msg['From'] = gmail_user
	msg['To'] = email_to
	
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.login(gmail_user, gmail_pwd)
	smtpserver.sendmail(msg['From'], msg['To'], msg.as_string())
	smtpserver.close()

clients = create_dict_from_file(cwd + csds_file, "\t")
	
#	clients = {"URL":"SENDTOEMAILADDRESS",
#	""}

## temporary dictionary used to do separate monitoring when a site is down
temp_dic = {}

def site_up():
	while True:
		for client, email in clients.items():
			try:
				r = requests.get(client)
				if r.status_code == 200:
					print client + ': OK'
					time.sleep(60)
				else:
					send_email(client + " is registering as down.\n\nI'll continue to monitor it.", email, client)
					temp_dic[client]=email
					del clients[client]
			except requests.ConnectionError:
				send_email(client + " is registering as down.\n\nI'll continue to monitor it.", email, client)
				temp_dic[client]=email
				del clients[client]

def site_down():
	while True:
		time.sleep(1800)
		for client, email in temp_dic.items():
			try:
				r = requests.get(client)
				if r.status_code == 200:
					print client + ' is back up.'
					send_email(client + ' is back up.', email, client)
					clients[client]=email
					del temp_dic[client]
				else:
					send_email(client + ' is down.', email, client)
					print client, 'is currently down, email sent.'
			except requests.ConnectionError:
				send_email(client + ' is down.', email, client)
				print client, 'is currently down, email sent.'

t1 = Thread(target = site_up)
t2 = Thread(target = site_down)
t1.start()
t2.start()
