#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2019年6月21日
@author: yuejing
'''
from common import fileHandle
from common import requestHandle
from common import HTMLTestRunner
from common import eml
from common import login
import unittest
import requests
import json
import ddt
import time

#DDT数据驱动测试：调用函数excel获取用例
testdata = fileHandle.excelHandle('./InterfaceCase/销量预测.xls').excelRead()
@ddt.ddt
class test_Api(unittest.TestCase):
	@classmethod
	def setUpClass(self):#在所有用例执行前，执行一次
		#导出列表，设置全局变量
		globals()["results"]=[]
		#登录获取token，设置全局变量
		globals()["token"] = login.login('itways','itways.abc').IWAY_Token()

	@ddt.data(*testdata)
	def test_all(self,data):
		#执行接口测试
		res=requestHandle.sendRequests(data,globals()["token"])
		#测试结果插入导出列表
		globals()["results"].append(res)
		#结果断言
		if res['Execute']=='Y':
			if len(res['Sql'])>0:
				self.assertIn(str(res['Sqlresult']),res['Text'])
			else:
				self.assertIn(str(res['Checkpoint']),res['Text'])
		else:
			print('Test case not executed!')
			self.assertEqual(1+1,2)

	@classmethod
	def tearDownClass(self):#在所有用例执行后，执行一次
		#导出测试结果
		now = time.strftime("%Y%m%d", time.localtime(time.time()))
		file_name='./Result/Interface-'+now+'.xls'
		fileHandle.excelHandle(file_name).excelWrite(globals()["results"],0)

def report():
	cases = unittest.TestLoader().loadTestsFromTestCase(test_Api)
	suite = unittest.TestSuite([cases])
	now = time.strftime("%Y%m%d", time.localtime(time.time()))
	file_path = "./Result/Interface-"+now+".html"
	file_result = open(file_path, 'wb')
	HTMLTestRunner.HTMLTestRunner(stream=file_result,verbosity=3,title='接口自动化测试报告',description=u'测试结果：').run(suite)
	file_result.close()
	print('\nThe html report has just been completed!')

def emlsend():
	emailist=['yuejing@way-s.cn']
	subject='接口自动化测试报告'
	contents=['Dear all:','附件为接口自动化测试报告，请查收！']
	attachment=["./Result/Interface-"+time.strftime("%Y%m%d", time.localtime(time.time()))+'.xls',"./Result/Interface-"+time.strftime("%Y%m%d", time.localtime(time.time()))+'.html']
	eml.emlHandle().emilSend(emailist,subject,contents,attachment)

if __name__ == "__main__":
	#unittest.main()
	report()			#输出报告
	emlsend()			#发送邮件


