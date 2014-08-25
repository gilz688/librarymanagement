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

        # User clicks Return button
        borrowButton = self.browser.find_by_xpath('//button[text()=\"Return\"]').first
        
        borrowButton.click()
        self.browser.get_alert().accept()
        alert = self.browser.get_alert()
        if alert != None:
            alert.accept()

        actual = self.getAvailableCopies()
        
        self.assertEqual(expected,actual)

    
    def testCannotBorrowBook(self):
        self.visitBooksUrl()
        
        #User clicks the Introduction to Algorithm"
        book = self.browser.find_by_xpath('//td[text()=\"Introduction to Algorithms\"]').first
        book.click()


        expectedStatus = 'Not Available'
        expectedAvailableCopies = 0

        n = self.getAvailableCopies()
        
        #User clicks Borrow button n times (to make the availabe copies 0)
        borrowButton = self.browser.find_by_xpath('//button[text()=\"Borrow\"]').first
        
        for i in range(n):
            borrowButton.click()
            self.browser.get_alert().accept()
            alert = self.browser.get_alert()
            if alert != None:
                alert.accept()

        actualStatus = self.getStatus()
        actualAvailableCopies = self.getAvailableCopies()

        self.assertEqual(expectedStatus,actualStatus)
        self.assertEqual(expectedAvailableCopies,actualAvailableCopies)
        assert self.browser.is_element_present_by_xpath('//button[text()=\"Borrow\" and @disabled]')

        
        #Rollback
        returnButton = self.browser.find_by_xpath('//button[text()=\"Return\"]').first
        for i in range(n):
            returnButton.click()
            self.browser.get_alert().accept()
            alert = self.browser.get_alert()
            if alert != None:
                alert.accept()


    def testCannotReturnBook(self):
        self.visitBooksUrl()
        
        #User clicks the Introduction to Algorithm"
        book = self.browser.find_by_xpath('//td[text()=\"Introduction to Algorithms\"]').first
        book.click()


        expectedStatus = 'Available'
        expectedAvailableCopies = 20

        n = self.getAvailableCopies()
        
        #User clicks return button n times (to make the availabe copies 20)
        returnButton = self.browser.find_by_xpath('//button[text()=\"Return\"]').first
        
        for i in range(n):
            returnButton.click()
            self.browser.get_alert().accept()
            alert = self.browser.get_alert()
            if alert != None:
                alert.accept()

        actualStatus = self.getStatus()
        actualAvailableCopies = self.getAvailableCopies()

        self.assertEqual(expectedStatus,actualStatus)
        self.assertEqual(expectedAvailableCopies,actualAvailableCopies)
        assert self.browser.is_element_present_by_xpath('//button[text()=\"Borrow\" and @disabled]')

        
        #Rollback
        borrowButton = self.browser.find_by_xpath('//button[text()=\"Borrow\"]').first
        for i in range(n):
            borrowButton.click()
            self.browser.get_alert().accept()
            alert = self.browser.get_alert()
            if alert != None:
                alert.accept()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)       