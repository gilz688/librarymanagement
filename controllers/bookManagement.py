
__author__ = 'librarymanagementteam'

'''
	Generate monthly report in a year
'''
def generateMonthlyReport():
	lib_name = request.vars.lib_name
	month = request.vars.month
	year = request.vars.year
	monthlyReport = getMonthReport(month,year,lib_name)
	return response.json(monthlyReport)

'''
	Generate yearly report
'''
def generateYearlyReport():
	lib_name = request.vars.lib_name
	year = request.vars.year
	yearlyReport = getYearReport(year,lib_name)
	return response.json(yearlyReport)

'''
	Get a report of a given year
'''
def getYearReport(year,lib_name):
	transactionHistory = getYearTransactions(year,lib_name)
	return transactionHistory

'''
	Get a report of a given month in a year
'''
def getMonthReport(month, year, lib_name):
	transactionHistory = getMonthTransactions(month, year, lib_name)
	return transactionHistory


'''
	Get a report for a day in a given month and year
'''
def getDayReport():
	day = request.vars.day
	month = request.vars.month
	year = request.vars.year
	booksBorrowed = getRecordsInADay(day, month, year)
	return response.json(booksBorrowed)

'''
	Get the most borrowed book of a year
'''
def getMostBorrowedBookPerYear():
	year = request.vars.year
	bookRecord = getMostBorrowedBookInAYear(year)
	isbn = bookRecord['book_manager']['ISBN']
	max_occur = bookRecord['_extra']['COUNT(book_manager.ISBN)']
	book = getBookByISBN(isbn)
	title = book.title
	library = book.lib_name
	record = {'ISBN': isbn, 'max_occur': max_occur, 'title': title, 'library': library}
	return response.json(record)

'''
	Get the most borrowed book of a month in a year
'''
def getMostBorrowedBookPerMonth():
	year = request.vars.year
	month = request.vars.month
	bookRecord = getMostBorrowedBookInAMonth(month, year)
	isbn = bookRecord['book_manager']['ISBN']
	max_occur = bookRecord['_extra']['COUNT(book_manager.ISBN)']
	book = getBookByISBN(isbn)
	title = book.title
	library = book.lib_name
	record = {'ISBN': isbn, 'max_occur': max_occur, 'title': title, 'library': library}
	return response.json(record)

'''
	Get the most borrowed book of a day in a month of a week
'''
def getMostBorrowedBookPerDay():
	day = request.vars.day
	month = request.vars.month
	year = request.vars.year
	bookRecord = getMostBorrowedBookInADay(day, month, year)
	isbn = bookRecord['book_manager']['ISBN']
	max_occur = bookRecord['_extra']['COUNT(book_manager.ISBN)']
	book = getBookByISBN(isbn)
	title = book.title
	library = book.lib_name
	record = {'ISBN': isbn, 'max_occur': max_occur, 'title': title, 'library': library}
	return response.json(record)
