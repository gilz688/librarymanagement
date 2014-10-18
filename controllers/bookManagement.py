
import pygal
from pygal.style import CleanStyle
__author__ = 'librarymanagementteam'

def plot_pygal():
    response.headers['Content-Type']='image/svg+xml'
    bar_chart = pygal.Bar(style=CleanStyle)                                            
    # Then create a bar graph object
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values    
    return bar_chart.render()

'''
	Generate monthly report in a year
'''
def generateMonthlyReport(year):
	pass

'''
	Generate weekly report in a month of a year
'''
def generateWeeklyReport(year, month):
	pass

'''
	Generate yearly report
'''
def generateYearlyReport():
	pass

'''
	Get a report of a given year
'''
def getYearReport(year):
	pass

'''
	Get a report of a given month in a year
'''
def getMonthReport(month, year):
	pass

'''
	Get a report in a given week of a month and year
'''
def getWeekReport(week, month, year):
	pass

'''
	Get a report for a day in a given month and year
'''
def getDayReport(day, month, year):
	pass

'''
	Get the most borrowed book of a year
'''
def getMostBorrowedBookPerYear(year):
	pass

'''
	Get the most borrowed book of a month in a year
'''
def getMostBorrowedBookPerMonth(year, month):
	pass

'''
	Get the most borrowed book of a week in a month of a week
'''
def getMostBorrowedBookPerWeek(year, month, week):
	pass

'''
	Get the most borrowed book of a day in a month of a week
'''
def getMostBorrowedBookPerDay(year, month, day):
	pass