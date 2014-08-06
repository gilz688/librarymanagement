from splinter import Browser           
with Browser() as browser: 
    # Visit URL 
    url = "http://localhost:8000/librarymanagement/default/" 
    browser.visit(url) 

    # User clicks the "Introduction to Algorithm"
    browser.find_by_name('Introduction to Algorithm').click()
    book.click()

    # View is checked if data expected is displayed
    assert browser.is_text_present('Introduction to Algorithm')
    assert browser.is_text_present('Cormen, Thomas H., Leiserson, Charles E.')
    assert browser.is_text_present('MIT Press')
    assert browser.is_text_present('0-07-013151-1')
    assert browser.is_text_present('Available')