import os
import time
import unittest
from splinter import Browser
from selenium import webdriver

class TestSearchBook(unittest.TestCase):
	
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
	
	def testWithBlankQuery(self):
		self.visitBooksUrl()
		searchButton = self.browser.find_by_id('search-button')

		searchButton.click()
		
		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present("Please don't leave blank.")

	"""
		start of Title searches acceptance tests
	"""

	def testTitleSearchWithCompleteKeys(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		authorMode = self.browser.find_by_xpath('//li[@class="mode-menu"]/a[text()=\"Title\"]').first
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		authorMode.click()
		searchForm.fill('Introduction To Algorithms')
		searchButton.click()
		assert self.browser.is_text_present('0-07-013151-1')
		assert self.browser.is_text_present('Introduction to Algorithms')


	def testTitleSearchWithIncompleteKeys(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		authorMode = self.browser.find_by_xpath('//li[@class="mode-menu"]/a[text()=\"Title\"]').first
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		authorMode.click()
		searchForm.fill('tr')
		searchButton.click()
		assert self.browser.is_text_present('0-07-013151-1')
		assert self.browser.is_text_present('Introduction to Algorithms')
		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('Data Structures Using C++')
	
	def testTitleSearchWithKeysNotInDatabase(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		authorMode = self.browser.find_by_xpath('//li[@class="mode-menu"]/a[text()=\"Title\"]').first
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		authorMode.click()
		searchForm.fill('Fundamentals of Computing')
		searchButton.click()
		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('Not found!')

	#end of Title search acceptance tests

	"""
		start of ISBN searches acceptance tests
	"""

	def testISBNSearchWithCompleteKeys(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		category = self.browser.find_by_xpath('//li[@class="mode-menu"]')[1]
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		category.click()
		searchForm.fill('0-07-013151-2')
		searchButton.click()

		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('Data Structures Using C++')
	
	

	def testISBNSearchWithIncompleteKeys(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		category = self.browser.find_by_xpath('//li[@class="mode-menu"]')[1]
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		category.click()
		searchForm.fill('0-07-013151')
		searchButton.click()

		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('Data Structures Using C++')
		assert self.browser.is_text_present('0-07-013151-1')
		assert self.browser.is_text_present('Introduction to Algorithms')

	def testISBNSearchWithInvalidKeys(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		category = self.browser.find_by_xpath('//li[@class="mode-menu"]')[1]
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		category.click()
		searchForm.fill('asdf')
		searchButton.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('No Book Found')

	def testISBNSearchWithKeysNotInDatabase(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		category = self.browser.find_by_xpath('//li[@class="mode-menu"]')[1]
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		category.click()
		searchForm.fill('0-07-013151-20')
		searchButton.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('No Book Found')
	
	#end of ISBN search acceptance tests
	"""
		start of AUTHOR searches acceptance tests
	"""

	def testAuthorSearchCompleteLName(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		authorMode = self.browser.find_by_xpath('//li[@class="mode-menu"]/a[text()=\"Author\"]').first
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		authorMode.click()
		searchForm.fill('Malik')
		searchButton.click()

		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('Data Structures Using C++')

	def testAuthorSearchIncompleteLName(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		authorMode = self.browser.find_by_xpath('//li[@class="mode-menu"]/a[text()=\"Author\"]').first
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		authorMode.click()
		searchForm.fill('cor')
		searchButton.click()
		assert self.browser.is_text_present('0-07-013151-1')
		assert self.browser.is_text_present('Introduction to Algorithms')

	def testAuthorSearchIncompleteLName2Results(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		authorMode = self.browser.find_by_xpath('//li[@class="mode-menu"]/a[text()=\"Author\"]').first
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		authorMode.click()
		searchForm.fill('i')
		searchButton.click()
		assert self.browser.is_text_present('0-07-013151-1')
		assert self.browser.is_text_present('Introduction to Algorithms')
		assert self.browser.is_text_present('0-07-013151-2')
		assert self.browser.is_text_present('Data Structures Using C++')

	def testAuthorNotInDatabase(self):
		self.visitBooksUrl()

		dropDown = self.browser.find_by_xpath('//a[@class="dropdown-toggle"]').first
		authorMode = self.browser.find_by_xpath('//li[@class="mode-menu"]/a[text()=\"Author\"]').first
		form = self.browser.find_by_tag('form').first
		searchForm = form.find_by_tag('input').first
		searchButton = self.browser.find_by_id('search-button')

		dropDown.click()
		authorMode.click()
		searchForm.fill('Gwapo')
		searchButton.click()

		assert self.browser.is_text_present('Error!')
		assert self.browser.is_text_present('Not found!')
	
	# end of search by AUTHOR acceptance tests

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSearchBook))
unittest.TextTestRunner(verbosity=2).run(suite)