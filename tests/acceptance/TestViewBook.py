from splinter import Browser           
import time
with Browser() as browser:

    # Visit URL 
    url = "http://127.0.0.1:8000/librarymanagement/default/" 
    browser.visit(url) 

    # User clicks the "Introduction to Algorithm"
    time.sleep(3)
    book = browser.find_by_xpath('//td[text()=\"Introduction to Algorithm\"]').first
    book.click()

    # View is checked if data expected is displayed
    assert browser.is_text_present('Cormen, Thomas H.; Leiserson, Charles E.')
    assert browser.is_text_present('MIT Press')
    assert browser.is_text_present('0-07-013151-1')
    assert browser.is_text_present('Available')