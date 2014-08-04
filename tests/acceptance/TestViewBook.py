from splinter import Browser           
with Browser() as browser: 
    # Visit URL 
    url = "http://localhost:8000/wlbc" 
    browser.visit(url) 

    # User clicks the "Introduction to Algorithm"
    browser.find_by_name('Introduction to Algorithm').click()
    book.click()

    # View is checked if data expected is displayed
    if !browser.is_text_present('Introduction to Algorithm'):
    	print "Title is not displayed!"
    if !browser.is_text_present('Cormen, Thomas H., Leiserson, Charles E.'):
    	print "Author/s are not displayed!"
    if !browser.is_text_present('MIT Press'):
    	print "Publication is not displayed!"
    if !browser.is_text_present('0-07-013151-1'):
    	print "ISBN is not displayed!"
    if !browser.is_text_present('Available'):
    	print "Available"
