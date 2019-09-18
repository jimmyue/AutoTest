from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class webHandle:
	def __init__(self,driver):
		self.driver=driver

	def find_element_located(self,method,element):
		"""封装id、name、xpath、link_text、class、css定位方法"""
		"""显性等待元素是否出现，再对网页元素进行定位操作"""
		if str.upper(method)=='ID':
			try:
				locator = (By.ID,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='NAME':
			try:
				locator = (By.NAME,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='XPATH':
			try:
				locator = (By.XPATH,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='LINK_TEXT':
			try:
				locator = (By.LINK_TEXT,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='CLASS':
			try:
				locator = (By.CLASS_NAME,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='CSS':
			try:
				locator = (By.CSS_SELECTOR,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		else:
			print('该元素定位方法未定义！')

	def find_element_alert(self,method,element):
		"""封装id、name、xpath、link_text、class、css定位方法"""
		"""显性等待元素是否可见，再对网页元素进行定位操作"""
		if str.upper(method)=='ID':
			try:
				locator = (By.ID,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='NAME':
			try:
				locator = (By.NAME,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='XPATH':
			try:
				locator = (By.XPATH,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='LINK_TEXT':
			try:
				locator = (By.LINK_TEXT,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='CLASS':
			try:
				locator = (By.CLASS_NAME,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		elif str.upper(method)=='CSS':
			try:
				locator = (By.CSS_SELECTOR,element)
				ele=WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present(locator))
				return ele
			except:
				print("can't find '%s' through %s" % (element,method))
				self.driver.quit()
		else:
			print('该元素定位方法未定义！')

	def title(self):
		return self.driver.title

	def open_browser(self,url):
		self.driver.maximize_window()
		self.driver.implicitly_wait(30) #隐形等待,设置页面超时时间
		self.driver.get(url)

	def close_browser(self):
		self.driver.quit()



