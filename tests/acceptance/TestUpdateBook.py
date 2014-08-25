import os
import time
import unittest
from splinter import Browser           

class TestUpdateBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('firefox')

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.browser.quit()
    
    def testBorrowBook(self):
        # Visit URL 
        url = "http://127.0.0.1:8000/librarymanagement/default/" 
        self.browser.visit(url) 

        # User clicks the "Introduction to Algorithm"
        book = self.browser.find_by_xpath('//td[text()=\"Introduction to Algorithms\"]').first
        book.click()

        # User clicks Borrow button
        borrowButton = self.browser.find_by_xpath('//button[text()=\"Borrow\"]').first
        time.sleep(1)
        borrowButton.click()
        self.browser.get_alert().accept()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)        