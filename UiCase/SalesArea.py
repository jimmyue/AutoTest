#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2019年7月16日
@author: yuejing
'''
import sys
sys.path.append('..')
sys.path.append('./common')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common import oracleSql
from common import webpageHandle
import unittest
import time

class TestUi(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.browser=webpageHandle.webHandle(self.driver)
		self.browser.open_browser('http://car.waysdata.com')
		print('Open the browser')
		self.browser.find_element_located("css",".el-form-item:nth-child(1) .el-input__inner").send_keys("test")
		self.browser.find_element_located("css",".el-form-item:nth-child(2) .el-input__inner").send_keys("ways123" + Keys.RETURN)
		self.browser.find_element_located("css","#modules > table > tbody > tr:nth-child(1) > td:nth-child(1) > a").click()

	def test_salesArea(self):
		"""销量-区域市场"""
		browser = self.browser
		browser.find_element_located("link_text",u"区域市场").click()
		print('Title: ',browser.title())
		self.assertEqual(browser.title(),'销量分析-区域市场')
		browser.find_element_located("link_text",u"区域市场").click()
		browser.find_element_located("link_text",u"全国").click()
		time.sleep(1) #等待DIV弹出框加载
		browser.find_element_located("css",".jspPane li:nth-child(5) > a").click()
		browser.find_element_located("link_text",u"广东").click()
		browser.find_element_located("link_text",u"广州市").click()
		browser.find_element_located("css",".submit").click()
		browser.find_element_located("css","#source > a").click()
		browser.find_element_located("link_text",u"SP-零售量").click()
		time.sleep(3) #等待数据加载完成
		sales=browser.find_element_located("css","#summary > tbody > tr > td:nth-child(1) > p").text
		print('页面显示：',sales)
		sql='''
		select to_char(sum(bq_sales),'fm999,999,999,999') sale
		from fdm_CITY_REG_SUB_MODEL
		where ym=201512 and city_id=167
		'''
		sqlsales=oracleSql.sqlHandle('172.16.1.37','DBFM','STRIDE','stride#96').sqlQuery(sql)[0][0]
		print('数据库：',sqlsales)
		self.assertEqual(sales,sqlsales)

	def tearDown(self):
		time.sleep(1)
		print('Close the browser')
		self.browser.close_browser()

if __name__=="__main__":
	unittest.main()
