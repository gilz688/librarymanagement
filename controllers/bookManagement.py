
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
	book = getMostBorrowedBookInAYear(year)
	bookRecord = {'ISBN': book['book_manager']['ISBN'], 'max_occur': book['_extra']['COUNT(book_manager.ISBN)']}
	return response.json(bookRecord)

'''
	Get the most borrowed book of a month in a year
'''
def getMostBorrowedBookPerMonth():
	year = request.vars.year
	month = request.vars.month
	book = getMostBorrowedBookInAMonth(month, year)
	bookRecord = {'ISBN': book['book_manager']['ISBN'], 'max_occur': book['_extra']['COUNT(book_manager.ISBN)']}
	return response.json(bookRecord)

'''
	Get the most borrowed book of a week in a month of a week
'''
def getMostBorrowedBookPerWeek(year, month, week):
	pass

'''
	Get the most borrowed book of a day in a month of a week
'''
def getMostBorrowedBookPerDay():
	day = request.vars.day
	month = request.vars.month
	year = request.vars.year
	book = getMostBorrowedBookInADay(day, month, year)
	bookRecord = {'ISBN': book['book_manager']['ISBN'], 'max_occur': book['_extra']['COUNT(book_manager.ISBN)']}
	return response.json(bookRecord)
	