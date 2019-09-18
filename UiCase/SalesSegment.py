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

	def test_salesSegment(self):
		"""销量-细分市场"""
		browser = self.browser
		browser.find_element_located("link_text",u"细分市场").click()
		print('Title: ',browser.title())
		self.assertEqual(browser.title(),'销量分析-细分市场')
		browser.find_element_located("css","#selectMarket > a").click()
		time.sleep(1)
		browser.find_element_located("link_text",u"B-M").click()
		browser.find_element_located("css","#source > a").click()
		browser.find_element_located("link_text",u"乘联会销量").click()
		time.sleep(3)
		sales=browser.find_element_located("css","#summary > tbody > tr > td:nth-child(1) > p").text
		print('页面显示：',sales)
		sql='''
		select to_char(sum(t.bq_sales),'fm999,999,999,999') sale
		from fdm_state_sales_sub_model t
		left join da_sub_grade_sub_model sm on sm.sub_model_id=t.sub_model_id
		left join v_da_sub_grade g on g.sub_grade_id=sm.sub_grade_id
		where t.data_type_id=3 and t.ym=(
		select max(ym) from fdm_state_sales_sub_model
		where data_type_id=3)
		and g.show_flag=1 and g.level2_name='B-M'
		and g.unit_id=(select unit_id from v_da_user r where r.login_id='test')
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
