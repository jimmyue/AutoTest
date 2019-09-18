#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2019年7月16日
@author: yuejing
'''
import sys
sys.path.append('..')
sys.path.append('./common')
from common import oracleSql
from common import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TestCar(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30) #隐形等待
		self.driver.get('http://car.waysdata.com')
		self.driver.find_element_by_css_selector(".el-form-item:nth-child(1) .el-input__inner").send_keys("test")
		self.driver.find_element_by_css_selector(".el-form-item:nth-child(2) .el-input__inner").send_keys("ways123" + Keys.RETURN)
		self.driver.find_element_by_css_selector("#modules > table > tbody > tr:nth-child(1) > td:nth-child(1) > a").click()

	#@unittest.skip('强制跳转')
	def test_salesWhole(self):
		driver = self.driver
		time.sleep(3)
		self.assertEqual(driver.title,'销量分析-整体市场')
		driver.find_element_by_css_selector("#source > a").click()
		driver.find_element_by_link_text(u"批发量").click()
		time.sleep(3)
		sales=driver.find_element_by_css_selector("#summary > tbody > tr > td:nth-child(1) > p").text
		sql='''
		select to_char(sum(t.bq_sales),'fm999,999,999,999') sale from fdm_state_sales_sub_model t
		where t.data_type_id=2 and t.ym=(select max(ym) from fdm_state_sales_sub_model where data_type_id=2)
		'''
		sqlsales=oracleSql.sqlHandle('172.16.1.37','DBFM','STRIDE','stride#96').sqlQuery(sql)[0][0]
		self.assertEqual(sales,sqlsales)

	#@unittest.skip('强制跳转')
	def test_salesSegment(self):
		driver = self.driver
		driver.find_element_by_link_text(u"细分市场").click()
		time.sleep(3)
		self.assertEqual(driver.title,'销量分析-细分市场')
		driver.find_element_by_css_selector("#selectMarket > a").click()
		driver.find_element_by_link_text("B-M").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#source > a").click()
		driver.find_element_by_link_text(u"乘联会销量").click()
		time.sleep(3)
		sales=driver.find_element_by_css_selector("#summary > tbody > tr > td:nth-child(1) > p").text
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
		self.assertEqual(sales,sqlsales)

	#@unittest.skip('强制跳转')
	def test_salesArea(self):
		driver = self.driver
		driver.find_element_by_link_text(u"区域市场").click()
		driver.find_element_by_css_selector("#source > a").click()
		driver.find_element_by_link_text(u"SP-零售量").click()
		time.sleep(3)
		driver.find_element_by_link_text(u"华南地区").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"广东").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"广州市").click()
		time.sleep(3)
		sales=driver.find_element_by_css_selector("#summary > tbody > tr > td:nth-child(1) > p").text
		sql='''
		select to_char(sum(bq_sales),'fm999,999,999,999') sale
		from fdm_CITY_REG_SUB_MODEL
		where ym=201512 and city_id=167
		'''
		sqlsales=oracleSql.sqlHandle('172.16.1.37','DBFM','STRIDE','stride#96').sqlQuery(sql)[0][0]
		self.assertEqual(sales,sqlsales)


	#@unittest.skip('强制跳转')
	def test_salesManf(self):
		driver = self.driver
		driver.find_element_by_link_text(u"厂商市场").click()
		driver.find_element_by_css_selector("#selectManf > a").click()
		driver.find_element_by_link_text(u"东风日产").click()
		time.sleep(3)
		self.assertEqual(driver.title,'销量分析-厂商市场')
		driver.find_element_by_css_selector("#source > a").click()
		driver.find_element_by_link_text(u"KP-终端销量").click()
		time.sleep(3)
		sales=driver.find_element_by_css_selector("#summary > tbody > tr > td:nth-child(1) > p").text
		sql='''
		select to_char(sum(t.bq_sales),'fm999,999,999,999') sale 
		from fdm_state_sales_sub_model t
		left join dm_sub_model m on m.sub_model_id=t.sub_model_id
		left join dm_manf f on f.manf_id=m.manf_id
		where t.data_type_id=6 and t.ym=(select max(ym) from fdm_state_sales_sub_model where data_type_id=6)
		and f.manf_name='东风日产'
		'''
		sqlsales=oracleSql.sqlHandle('172.16.1.37','DBFM','STRIDE','stride#96').sqlQuery(sql)[0][0]
		self.assertEqual(sales,sqlsales)

	#@unittest.skip('强制跳转')
	def test_salesModel(self):
		driver = self.driver
		driver.find_element_by_link_text(u"车型市场").click()
		time.sleep(3)
		self.assertEqual(driver.title,'销量分析-车型市场')
		driver.find_element_by_css_selector("#source > a").click()
		driver.find_element_by_link_text(u"SX-销量统计数").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#otherModel > a").click()
		driver.find_element_by_css_selector("#openPopupForOtherCarModel_radio > div.section > div.popselector > div.selectbox > div.sub-section > div:nth-child(1) > div.fast-word.clearfix > div > input").send_keys(u"天籁")
		driver.find_element_by_link_text(u"天籁").click()
		time.sleep(3)
		sales=driver.find_element_by_css_selector("#summary > tbody > tr > td:nth-child(1) > p").text
		sql='''
		select to_char(sum(t.bq_sales),'fm999,999,999,999') sale 
		from fdm_state_sales_sub_model t
		left join dm_sub_model m on m.sub_model_id=t.sub_model_id
		where t.data_type_id=7 and t.ym=(select max(ym) from fdm_state_sales_sub_model where data_type_id=7)
		and m.sub_model_name='天籁'
		'''
		sqlsales=oracleSql.sqlHandle('172.16.1.37','DBFM','STRIDE','stride#96').sqlQuery(sql)[0][0]
		self.assertEqual(sales,sqlsales)
		
	def tearDown(self):
		time.sleep(1)
		self.driver.quit()

if __name__=="__main__":
	suite = unittest.TestSuite()
	# 将测试用例，加入到测试容器中
	suite.addTest(TestCar("test_salesWhole"))
	suite.addTest(TestCar("test_salesSegment"))
	suite.addTest(TestCar("test_salesArea"))
	suite.addTest(TestCar("test_salesManf"))
	suite.addTest(TestCar("test_salesModel"))
	# 定义个报告存放的路径，支持相对路径
	now = time.strftime("%Y%m%d", time.localtime(time.time()))
	file_path = "../result/Ui-"+now+".html"
	file_result = open(file_path, 'wb')
	HTMLTestRunner.HTMLTestRunner(stream=file_result,verbosity=3,title='Ui Test Report',description=u'Result:').run(suite)
	file_result.close()
