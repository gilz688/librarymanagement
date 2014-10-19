__author__ = 'librarymanagementteam'


'''
	Generate monthly report in a year
'''
def generateMonthlyReport():
	month = request.vars.month
	year = request.vars.year
	monthlyReport = getMonthReport(month,year)
	return response.json(monthlyReport)

'''
	Generate yearly report
'''
def generateYearlyReport():
	year = request.vars.year
	yearlyReport = getYearReport(year)
	return response.json(yearlyReport)

'''
	Get a report of a given year
'''
def getYearReport(year):
	transactionHistory = getYearTransactions(year)
	return transactionHistory

'''
	Get a report of a given month in a year
'''
def getMonthReport(month, year):
	transactionHistory = getMonthTransactions(month, year)
	return transactionHistory


'''
	Get a report for a day in a given month and year
'''
def getDayReport():
	if (session.status == 'logged in' and session.lib_name == library.lib_name):
		day = request.vars.day
		month = request.vars.month
		year = request.vars.year
		library = request.vars.library
		booksBorrowed = getRecordsInADay(day, month, year, library)
		return response.json(booksBorrowed)
	else:
		return response.json(None)

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
