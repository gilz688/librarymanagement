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
        time.sleep(3)
        cls.browser.quit()
    
    def getAvailableCopies(self):
        time.sleep(2)
        return int(self.browser.find_by_xpath('//span[@id=\"availcopies\"]').first.value)

    def getStatus(self):
        time.sleep(2)
        return self.browser.find_by_xpath('//span[@id=\"status\"]').first.value

    def visitBooksUrl(self):
        url = "http://127.0.0.1:8000/librarymanagement/default/" 
        self.browser.visit(url) 

    def testBorrowBook(self):
        self.visitBooksUrl()

        # User clicks the "Introduction to Algorithm"
        book = self.browser.find_by_xpath('//td[text()=\"Introduction to Algorithms\"]').first
        book.click()

        expected = self.getAvailableCopies() - 1

        # User clicks Borrow button
        borrowButton = self.browser.find_by_xpath('//button[text()=\"Borrow\"]').first
        
        borrowButton.click()

        self.browser.get_alert().accept()
        alert = self.browser.get_alert()
        if alert != None:
            alert.accept()

        actual = self.getAvailableCopies()
        
        self.assertEqual(expected,actual)

    def testReturnBook(self):
        self.visitBooksUrl()

        # User clicks the "Introduction to Algorithm"
        book = self.browser.find_by_xpath('//td[text()=\"Introduction to Algorithms\"]').first
        book.click()

        
        expected = self.getAvailableCopies() + 1

        # User clicks Borrow button
        borrowButton = self.browser.find_by_xpath('//button[text()=\"Return\"]').first
        
        borrowButton.click()
        self.browser.get_alert().accept()
        alert = self.browser.get_alert()
        if alert != None:
            alert.accept()

        actual = self.getAvailableCopies()
        
        self.assertEqual(expected,actual)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)        