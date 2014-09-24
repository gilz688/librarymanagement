import os
import unittest
from splinter import Browser           

class TestViewBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('firefox')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        
    def testBorrowBook(self):
        # Visit URL 
        url = "http://127.0.0.1:8000/librarymanagement/default/" 
        self.browser.visit(url) 

        # User clicks the "Introduction to Algorithm"
        book = self.browser.find_by_xpath('//a[text()=\"Introduction to Algorithms\"]').first
        book.click()

        # View is checked if data expected is displayed
        assert self.browser.is_text_present('Cormen, Thomas H.; Leiserson, Charles E.')
        assert self.browser.is_text_present('MIT Press')
        assert self.browser.is_text_present('0-07-013151-1')
        assert self.browser.is_text_present('Available')

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestViewBook))
unittest.TextTestRunner(verbosity=2).run(suite)        