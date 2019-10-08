from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class webHandle:
	def __init__(self,driver):
		self.driver=driver

	def findElement(self,*loc):
		"""封装id、name、xpath、link_text、class、css定位方法"""
		"""显性等待单个元素是否出现，再对网页元素进行定位操作"""
		try:
			return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
		except NoSuchElementException as e:
			print('Error Details {0}'.format(e.args[0]))

	def findsElement(self,*loc):
		"""封装id、name、xpath、link_text、class、css定位方法"""
		"""显性等待多个元素是否出现，再对网页元素进行定位操作"""
		try:
			return WebDriverWait(self.driver,20).until(lambda x:x.find_elements(*loc))
		except NoSuchElementException as e:
			print('Error Details {0}'.format(e.args[0]))




