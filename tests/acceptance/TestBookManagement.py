import os
import time
import unittest
from splinter import Browser
from selenium import webdriver

class TestBookManagement(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.browser = Browser('firefox')

	@classmethod
	def tearDownClass(cls):
		time.sleep(5)
		cls.browser.quit()

	def visitBooksUrl(self):
		url = "http://127.0.0.1:8000/librarymanagement/default/" 
		self.browser.visit(url)
	
	# Yearly
	def testGetMostBorrowedBookYearly(self):
		self.visitBooksUrl()

		option = self.browser.find_by_id('borrowList')
		option.click()
		time.sleep(5)
		year = self.browser.find_by_id('borYear')
		year.click()
		time.sleep(5)
		submit = self.browser.find_by_id('borrowButtonY')
		submit.click()
		time.sleep(5)

		assert self.browser.is_text_present('Introduction to Electricity')
		assert self.browser.is_text_present("0-07-013151-3")
		assert self.browser.is_text_present("SET-Library")
		assert self.browser.is_text_present("6")

	# Yearly blank query
	def testGetMostBorrowedBookYearlyWithBlankQuery(self):
		self.visitBooksUrl()

		option = self.browser.find_by_id('borrowList')
		option.click()
		time.sleep(5)
		year = self.browser.find_by_id('borYear')
		year.click()
		time.sleep(5)
		yearInput = self.browser.find_by_id('borYearInput')
		yearInput.fill("")
		submit = self.browser.find_by_id('borrowButtonY')
		submit.click()

		assert self.browser.is_text_present('Error')
		assert self.browser.is_text_present("Please enter the date")

	# Monthly blank query
	def testGetMostBorrowedBookMonthlyWithBlankQuery(self):
		self.visitBooksUrl()

		option = self.browser.find_by_id('borrowList')
		option.click()
		time.sleep(5)
		year = self.browser.find_by_id('borMonth')
		year.click()
		time.sleep(5)
		submit = self.browser.find_by_id('borrowButtonM')
		submit.click()

		assert self.browser.is_text_present('Error')
		assert self.browser.is_text_present("Please enter the date")

	# Daily blank query
	def testGetMostBorrowedBookDailyWithBlankQuery(self):
		self.visitBooksUrl()

		option = self.browser.find_by_id('borrowList')
		option.click()
		time.sleep(5)
		year = self.browser.find_by_id('borDay')
		year.click()
		time.sleep(5)
		submit = self.browser.find_by_id('borrowButtonD')
		submit.click()

		assert self.browser.is_text_present('Error')
		assert self.browser.is_text_present("Please enter the date")

	def testGetYearlyReportCOELib(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(5)

		option = self.browser.find_by_id('historyList')
		option.click()
		time.sleep(5)
		year = self.browser.find_by_id('histYear')
		year.click()
		time.sleep(5)
		submit = self.browser.find_by_id('historyButtonY')
		submit.click()

		assert self.browser.is_text_present('Data Structures Using C++')
		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('1999-0001')
		assert self.browser.is_text_present('2014-06-16')
		assert self.browser.is_text_present('09:43:55')	
		assert self.browser.is_text_present('return')

		# logout
		self.browser.find_by_css('#session').click()
	
	def testGetYearlyReportSETLib(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(5)

		option = self.browser.find_by_id('historyList')
		option.click()
		time.sleep(5)
		year = self.browser.find_by_id('histYear')
		year.click()
		time.sleep(5)
		dropDown = self.browser.find_by_id('hlibY')
		dropDown.click()
		time.sleep(2)
		library = self.browser.find_by_id('hSETY')
		library.click()
		time.sleep(5)
		submit = self.browser.find_by_id('historyButtonY')
		submit.click()

		assert self.browser.is_text_present('Introduction to Electricity')
		assert self.browser.is_text_present('0-07-013151-3')
		assert self.browser.is_text_present('1999-0002')
		assert self.browser.is_text_present('2014-06-15')
		assert self.browser.is_text_present('09:43:55')	
		assert self.browser.is_text_present('borrow')

		# logout
		self.browser.find_by_css('#session').click()

	def testGetMonthlyReportCOELibBlankQuery(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(5)

		option = self.browser.find_by_id('historyList')
		option.click()
		time.sleep(5)
		month = self.browser.find_by_id('histMonth')
		month.click()
		time.sleep(5)
		submit = self.browser.find_by_id('historyButtonM')
		submit.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('Please enter the date')

		# logout
		self.browser.find_by_css('#session').click()

	def testGetMonthlyReportSETLibBlankQuery(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian2")
		self.browser.find_by_css("#password").fill("password2")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(5)

		option = self.browser.find_by_id('historyList')
		option.click()
		time.sleep(5)
		month = self.browser.find_by_id('histMonth')
		month.click()
		time.sleep(5)
		submit = self.browser.find_by_id('historyButtonM')
		submit.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('Please enter the date')

		# logout
		self.browser.find_by_css('#session').click()


	def testGetDailyReportCOELibBlankQuery(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian1")
		self.browser.find_by_css("#password").fill("password1")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(5)

		option = self.browser.find_by_id('historyList')
		option.click()
		time.sleep(5)
		day = self.browser.find_by_id('histDay')
		day.click()
		time.sleep(5)
		submit = self.browser.find_by_id('historyButtonD')
		submit.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('Please enter the date')

		# logout
		self.browser.find_by_css('#session').click()

	def testGetDailyReportSETLibBlankQuery(self):
		self.visitBooksUrl()
		self.browser.find_by_css('#session').click()
		time.sleep(1)
		self.browser.find_by_css("#username").fill("librarian2")
		self.browser.find_by_css("#password").fill("password2")
		self.browser.find_by_css("#submitLogIn").click()
		time.sleep(5)

		option = self.browser.find_by_id('historyList')
		option.click()
		time.sleep(5)
		day = self.browser.find_by_id('histDay')
		day.click()
		time.sleep(5)
		submit = self.browser.find_by_id('historyButtonD')
		submit.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('Please enter the date')

		# logout
		self.browser.find_by_css('#session').click()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestBookManagement))
unittest.TextTestRunner(verbosity=2).run(suite)