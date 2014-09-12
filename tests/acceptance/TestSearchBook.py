import os
import time
import unittest
from splinter import Browser

class TestSearchBook(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.browser = Browser('firefox')

	@classmethod
	def tearDownClass(cls):
		cls.browser.quit()

	def visitBooksUrl(self):
		url = "http://127.0.0.1:8000/librarymanagement/default/" 
		self.browser.visit(url)

	def testWithBlankQuery(self):
		pass

	def testSuccessSearch(self):
		pass

	def testISBNSearchWithCompleteKeys(self):
		self.visitBooksUrl()

		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search')

		searchForm.fill('0-07-013151-2')
		searchButton.click()

		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('Data Structures Using C++')



	def testISBNSearchWithIncompleteKeys(self):
		self.visitBooksUrl()

		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search')

		searchForm.fill('0-07-013151')
		searchButton.click()

		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('Data Structures Using C++')
		assert self.browser.is_text_present('0-07-013151-1')
		assert self.browser.is_text_present('Introduction to Algorithms')

	def testISBNSearchWithInvalidKeys(self):
		self.visitBooksUrl()

		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search')

		searchForm.fill('asdf')
		searchButton.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('No Book Found')

	def testISBNSearchWithKeysNotInDatabase(self):
		self.visitBooksUrl()

		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search')

		searchForm.fill('0-07-013151-3')
		searchButton.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('No Book Found')
	



suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSearchBook))
unittest.TextTestRunner(verbosity=2).run(suite)