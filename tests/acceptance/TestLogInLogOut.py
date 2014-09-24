import os
import time
import unittest
from splinter import Browser
from selenium import webdriver

class TestLogInLogOut(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.browser = Browser('firefox')

	@classmethod
	def tearDownClass(cls):
		time.sleep(3)
		cls.browser.quit()

	def visitBooksUrl(self):
		url = "http://127.0.0.1:8000/librarymanagement/default/" 
		self.browser.visit(url)

	def testCorrectCredentials:
		pass

	def testIncorrectCredentials:
		pass

	def testBlankUsername:
		pass

	def testBlankPassword:
		pass

	def testLogOut(self):
		self.visitBooksUrl()

		session_value = self.browser.evaluate_script('$("#session a").html()')
		
		if(session_value == "Log In"):
			self.browser.find_by_css('#session').click()
			time.sleep(1)
			self.browser.find_by_css("#username").fill("username 1234")
			self.browser.find_by_css("#password").fill("password")
			self.browser.find_by_css("#logIn").click()
			time.sleep(2)
			self.browser.find_by_css('#session').click()
		else:
			self.browser.find_by_css('#session').click()

		assert 'Log In' == self.browser.evaluate_script('$("#session a").html()')

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogInLogOut))
unittest.TextTestRunner(verbosity=2).run(suite)