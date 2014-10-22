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

	def testGetMostBorrowedBookYearlyNotLoggedIn(self):
		self.visitBooksUrl()

		option = self.browser.find_by_xpath('//span[text()=\"View most borrowed books\"]').first
		#optionList = self.browser.find_by_id('borrowListData')
		#submit = self.browser.find_by_id("borrowButtonM")
		#optionList = self.browser.find_by_id("borrowListData")
		#year = self.browser.find_by_xpath('//li[@id=\"borrowListData\"]/ul/li')[2]
		year = self.browser.find_by_id('borYear')
		#submit = self.browser.find_by_id('borrowButtonY')
		
		option.click()
		year.click()
		#submit.click()


	def testGetMostBorrowedBookYearlyLoggedIn(self):
		pass

	def testGetMostBorrowedBookMonthlyNotLoggedIn(self):
		pass

	def testGetMostBorrowedBookMonthlyLoggedIn(self):
		pass

	def testGetMostBorrowedBookDailyNotLoggedIn(self):
		pass
		'''
		self.visitBooksUrl()
		option = self.browser.find_by_xpath('//span[text()=\"View most borrowed books\"]').first
		day = self.browser.find_by_id('borDay')
		submit = self.browser.find_by_id('borrowButtonD')

		option.click()
		day.click()
		submit.click()
		'''

	def testGetMostBorrowedBookDailyLoggedIn(self):
		pass

	def testGetYearlyReportCOELib(self):
		pass

	def testGetYearlyReportSETLib(self):
		pass

	def testGetYearlyReportCEDLib(self):
		pass

	def testGetMonthlyReportCOELib(self):
		pass

	def testGetMonthlyReportSETLib(self):
		pass

	def testGetMonthlyReportCEDLib(self):
		pass

	def testGetDailyReportCOELib(self):
		pass

	def testGetDailyReportSETLib(self):
		pass

	def testGetDailyReportCEDLib(self):
		pass

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestBookManagement))
unittest.TextTestRunner(verbosity=2).run(suite)