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

	def test_salesWhole(self):
		"""销量-整体市场"""
		browser = self.browser
		print('Title: ',browser.title())
		self.assertEqual(browser.title(),'销量分析-整体市场')
		browser.find_element_located("css","#source > a").click()
		browser.find_element_located("link_text",u"批发量").click()
		time.sleep(3)
		sales=browser.find_element_located("css","#summary > tbody > tr > td:nth-child(1) > p").text
		print('页面显示：',sales)
		sql='''
		select to_char(sum(t.bq_sales),'fm999,999,999,999') sale from fdm_state_sales_sub_model t
		where t.data_type_id=2 and t.ym=(select max(ym) from fdm_state_sales_sub_model where data_type_id=2)
		'''
		sqlsales=oracleSql.sqlHandle('172.16.1.37','DBFM','STRIDE','stride#96').sqlQuery(sql)[0][0]
		print('数据库：',sqlsales)
		self.assertEqual(sales,sqlsales)

	def tearDown(self):
		time.sleep(1)
		print('Close the browser')
		self.driver.quit()

if __name__=="__main__":
	unittest.main()
