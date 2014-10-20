__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/bookManagement.py", globals())



class TestBookManagement(unittest.TestCase):

	def setUp(self):
		request = Request("")

	def testMonthTransaction(self):
		request.vars.lib_name = 'SET-Library'
		request.vars.month = '07'
		request.vars.year = '2014'
		result = generateMonthlyReport()
		expected = '[["0-07-013151-4", "1999-0002", "2014-07-17", "14:43:55", "borrow"], ["0-07-013151-3", "1999-0002", "2014-07-17", "16:43:55", "borrow"], ["0-07-013151-5", "1999-0002", "2014-07-18", "17:43:55", "borrow"], ["0-07-013151-3", "1999-0002", "2014-07-18", "18:43:55", "return"], ["0-07-013151-4", "1999-0002", "2014-07-19", "19:43:55", "return"]]'
		self.assertEquals(result.encode('ascii', 'ignore'),expected)

	def testYearTransaction(self):
		request.vars.lib_name = 'COE-Library'
		request.vars.year = '2014'
		result = generateYearlyReport()
		expected = '[["0-07-013151-1", "1999-0001", "2014-06-14", "09:43:55", "borrow"], ["0-07-013151-1", "1999-0001", "2014-06-17", "14:31:11", "return"], ["0-07-013151-1", "1999-0001", "2014-06-17", "08:43:12", "borrow"], ["0-07-013151-1", "1999-0001", "2014-06-17", "11:43:55", "borrow"], ["0-07-013151-2", "1999-0001", "2014-06-17", "09:54:55", "borrow"], ["0-07-013151-2", "1999-0001", "2014-06-15", "19:32:55", "borrow"], ["0-07-013151-2", "1999-0001", "2014-06-16", "09:43:55", "return"], ["0-07-013151-1", "1999-0001", "2014-06-17", "09:43:55", "borrow"]]'
		self.assertEquals(result.encode('ascii', 'ignore'),expected)

	
	def testMostBorrowedBookInADay(self):
		request.vars.day = '17'
		request.vars.month = '06'
		request.vars.year = '2014'
		result = getMostBorrowedBookPerDay()
		expected = '{"ISBN": "0-07-013151-1", "library": "COE-Library", "max_occur": 4, "title": "Introduction to Algorithms"}'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)
		

	def testMostBorrowedBookInAMonth(self):
		request.vars.year = '2014'
		request.vars.month = '06'
		result = getMostBorrowedBookPerMonth()
		expected = '{"ISBN": "0-07-013151-1", "library": "COE-Library", "max_occur": 5, "title": "Introduction to Algorithms"}'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testMostBorrowedBookInAYear(self):
		request.vars.year = '2014'
		result = getMostBorrowedBookPerYear()
		expected = '{"ISBN": "0-07-013151-3", "library": "SET-Library", "max_occur": 6, "title": "Introduction to Electricity"}'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testGetDayReportCOELib(self):
		request.vars.day = '17'
		request.vars.month = '06'
		request.vars.year = '2014'
		request.vars.library = 'COE-Library'
		result = getDayReport()
		expected = '[{"book_manager": {"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-1", "transact_time": "14:31:11", "librarian_id": "1999-0001"}, "book": {"lib_name": "COE-Library", "title": "Introduction to Algorithms"}}, {"book_manager": {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "08:43:12", "librarian_id": "1999-0001"}, "book": {"lib_name": "COE-Library", "title": "Introduction to Algorithms"}}, {"book_manager": {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "11:43:55", "librarian_id": "1999-0001"}, "book": {"lib_name": "COE-Library", "title": "Introduction to Algorithms"}}, {"book_manager": {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-2", "transact_time": "09:54:55", "librarian_id": "1999-0001"}, "book": {"lib_name": "COE-Library", "title": "Data Structures Using C++"}}, {"book_manager": {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, "book": {"lib_name": "COE-Library", "title": "Introduction to Algorithms"}}]'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)


	def testGetDayReportSETLib(self):
		request.vars.day = '17'
		request.vars.month = '06'
		request.vars.year = '2014'
		request.vars.library = 'SET-Library'
		result = getDayReport()
		expected = '[{"book_manager": {"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-4", "transact_time": "14:43:55", "librarian_id": "1999-0002"}, "book": {"lib_name": "SET-Library", "title": "Modern Physics for Science and Engineering"}}, {"book_manager": {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "13:43:55", "librarian_id": "1999-0002"}, "book": {"lib_name": "SET-Library", "title": "Introduction to Electricity"}}]'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testDayReportOtherLibrary(self):
		request.vars.day = '17'
		request.vars.month = '06'
		request.vars.year = '2014'
		
		request.vars.library = 'CED-Library'
		result = getDayReport()
		expected = '[]'

		self.assertEquals(result.encode('ascii', 'ignore'), expected)





suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestBookManagement))
unittest.TextTestRunner(verbosity=2).run(suite)