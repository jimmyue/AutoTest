#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2019年5月21日
@author: yuejing
'''
import yagmail
from . import readConfig
import time

class emlHandle:
	Config = readConfig.ReadConfig()
	def __init__(self,host=Config.get_email("mail_host"),user=Config.get_email("mail_user"),password=Config.get_email("mail_pass")):
		self.host=host
		self.user=user
		self.password=password

	def emilSend(self,emailist,subject,contents,attachment=0):
		yag = yagmail.SMTP(user=self.user,password=self.password,host=self.host)
		try:
			if attachment==0:
				yag.send(emailist,subject,contents)
			else:
				yag.send(emailist,subject,contents,attachment)
			print('\nThe mail was sent successfully in '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
		except Exception as e:
			print (str(e))
		time.sleep(1)
