import os
import time
import unittest
from splinter import Browser

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

	def testCorrectCredentials(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#logIn").click()
		time.sleep(2)
		assert 'Log Out' == self.browser.find_by_css('#session').value

		# logout
		self.browser.find_by_css('#session').click()


	def testIncorrectCredentials(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("wrongpass")
		self.browser.find_by_css("#logIn").click()
		time.sleep(2)
		assert self.browser.is_text_present('Invalid username and/or password')
		assert 'Log In' == self.browser.find_by_css('#session').value

	def testBlankUsername(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#logIn").click()
		time.sleep(2)
		assert self.browser.is_text_present('Invalid username and/or password')
		assert 'Log In' == self.browser.find_by_css('#session').value

	def testBlankPassword(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("")
		self.browser.find_by_css("#logIn").click()
		time.sleep(2)
		assert self.browser.is_text_present('Invalid username and/or password')
		assert 'Log In' == self.browser.find_by_css('#session').value

	def testLogOut(self):
		self.visitBooksUrl()

		session_value = self.browser.evaluate_script('$("#session a").html()')
		
		if(session_value == "Log In"):
			self.browser.find_by_css('#session').click()
			time.sleep(1)
			self.browser.find_by_css("#username").fill("librarian1")
			self.browser.find_by_css("#password").fill("password1")
			self.browser.find_by_css("#logIn").click()
			time.sleep(2)
			self.browser.find_by_css('#session').click()
		else:
			self.browser.find_by_css('#session').click()

		assert 'Log In' == self.browser.evaluate_script('$("#session a").html()')

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogInLogOut))
unittest.TextTestRunner(verbosity=2).run(suite)