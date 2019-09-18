#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2019年7月15日
@author: yuejing
'''
from common import HTMLTestRunner
from common import eml
from UiCase import SalesWhole
from UiCase import SalesSegment
from UiCase import SalesArea
from UiCase import SalesManf
from UiCase import SalesModel
import unittest
import time

def emlsend():
	emailist=['yuejing@way-s.cn']
	subject='UI自动化测试报告'
	contents=['Dear all:','附件为UI自动化测试报告，请查收！']
	attachment=["./Result/Ui-"+time.strftime("%Y%m%d", time.localtime(time.time()))+'.html']
	eml.emlHandle().emilSend(emailist,subject,contents,attachment)

def report():
	suite=unittest.TestSuite()
	#将测试用例加入到测试容器中，用例会按添加顺序执行
	suite.addTest(unittest.makeSuite(SalesWhole.TestUi))
	suite.addTest(unittest.makeSuite(SalesSegment.TestUi))
	suite.addTest(unittest.makeSuite(SalesArea.TestUi))
	suite.addTest(unittest.makeSuite(SalesManf.TestUi))
	suite.addTest(unittest.makeSuite(SalesModel.TestUi))
	#输出测试报告
	now=time.strftime("%Y%m%d", time.localtime(time.time()))
	file_path = "./Result/Ui-"+now+".html"
	file_result = open(file_path, 'wb')
	HTMLTestRunner.HTMLTestRunner(stream=file_result,verbosity=3,title=u'UI自动化测试报告',description=u'测试结果:').run(suite)
	file_result.close()
	print('\nThe html report has just been completed!')

if __name__ == "__main__":
	report()			#输出报告
	emlsend()			#发送邮件