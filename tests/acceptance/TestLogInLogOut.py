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

	def testCorrectCredentials1(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(15)
		assert 'Log Out' == self.browser.find_by_css('#session a').value
		assert 'Home Library: COE-Library' ==  self.browser.find_by_css('#header').value

		# logout
		self.browser.find_by_css('#session').click()


	def testCorrectCredentials2(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian2")
		self.browser.find_by_css("#password").fill("password2")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(3)
		assert 'Log Out' == self.browser.find_by_css('#session a').value
		assert 'Home Library: SET-Library' ==  self.browser.find_by_css('#header').value

		# logout
		self.browser.find_by_css('#session').click()


	def testIncorrectCredentials(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian2")
		self.browser.find_by_css("#password").fill("wrongpass")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(3)
		assert self.browser.is_text_present('Invalid username and/or password')
		assert 'Log In' == self.browser.find_by_css('#session a').value

	def testBlankUsername(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(2)
		assert self.browser.is_text_present('Username and Password field is required')
		assert 'Log In' == self.browser.find_by_css('#session a').value

	def testBlankPassword(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(2)
		assert self.browser.is_text_present('Username and Password field is required')
		assert 'Log In' == self.browser.find_by_css('#session a').value

	def testLogOut(self):
		self.visitBooksUrl()

		session_value = self.browser.evaluate_script('$("#session a").html()')
		
		if(session_value == "Log In"):
			self.browser.find_by_css('#session').click()
			time.sleep(1)
			self.browser.find_by_css("#username").fill("librarian2")
			self.browser.find_by_css("#password").fill("password2")
			self.browser.find_by_css("#submitLogIn").click()
			time.sleep(2)
			self.browser.find_by_css('#session a').click()
			time.sleep(3)
		else:
			self.browser.find_by_css('#session a').click()
			time.sleep(3)
		
		assert 'Log In' == self.browser.find_by_css('#session a').value

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogInLogOut))
unittest.TextTestRunner(verbosity=2).run(suite)