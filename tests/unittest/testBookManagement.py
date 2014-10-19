__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/bookManagement.py", globals())



class TestBookManagement(unittest.TestCase):

	def setUp(self):
		request = Request("")

	def testMonthTransaction(self):
		request.vars.month = '06'
		request.vars.year = '2014'
		result = generateMonthlyReport()
		expected = '[{"transact_date": "2014-06-14", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-1", "transact_time": "14:31:11", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "08:43:12", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "11:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-2", "transact_time": "09:54:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-2", "transact_time": "19:32:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-16", "transact_type": "return", "ISBN": "0-07-013151-2", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "09:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-4", "transact_time": "10:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-15", "transact_type": "return", "ISBN": "0-07-013151-3", "transact_time": "11:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "12:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "13:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-4", "transact_time": "14:43:55", "librarian_id": "1999-0002"}]'
		self.assertEquals(result.encode('ascii', 'ignore'),expected)

	def testYearTransaction(self):
		request.vars.year = '2014'
		result = generateYearlyReport()
		expected = '[{"transact_date": "2014-06-14", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-1", "transact_time": "14:31:11", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "08:43:12", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "11:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-2", "transact_time": "09:54:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-2", "transact_time": "19:32:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-16", "transact_type": "return", "ISBN": "0-07-013151-2", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "09:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-4", "transact_time": "10:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-15", "transact_type": "return", "ISBN": "0-07-013151-3", "transact_time": "11:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-15", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "12:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "13:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-4", "transact_time": "14:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-07-17", "transact_type": "borrow", "ISBN": "0-07-013151-4", "transact_time": "14:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-07-17", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "16:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-07-18", "transact_type": "borrow", "ISBN": "0-07-013151-5", "transact_time": "17:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-07-18", "transact_type": "return", "ISBN": "0-07-013151-3", "transact_time": "18:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-07-19", "transact_type": "return", "ISBN": "0-07-013151-4", "transact_time": "19:43:55", "librarian_id": "1999-0002"}]'
		self.assertEquals(result.encode('ascii', 'ignore'),expected)

	
	def testMostBorrowedBookInADay(self):
		request.vars.day = '17'
		request.vars.month = '06'
		request.vars.year = '2014'
		result = getMostBorrowedBookPerDay()
		expected = '{"ISBN": "0-07-013151-1", "max_occur": 4}'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)
		

	def testMostBorrowedBookInAMonth(self):
		request.vars.year = '2014'
		request.vars.month = '06'
		result = getMostBorrowedBookPerMonth()
		expected = '{"ISBN": "0-07-013151-1", "max_occur": 5}'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testMostBorrowedBookInAYear(self):
		request.vars.year = '2014'
		result = getMostBorrowedBookPerYear()
		expected = '{"ISBN": "0-07-013151-3", "max_occur": 6}'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testMostBorrowedBookInAWeek(self):
		pass

	def testGetDayReport(self):
		request.vars.day = '17'
		request.vars.month = '06'
		request.vars.year = '2014'
		result = getDayReport()
		expected = '[{"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-1", "transact_time": "14:31:11", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "08:43:12", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "11:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-2", "transact_time": "09:54:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-1", "transact_time": "09:43:55", "librarian_id": "1999-0001"}, {"transact_date": "2014-06-17", "transact_type": "borrow", "ISBN": "0-07-013151-3", "transact_time": "13:43:55", "librarian_id": "1999-0002"}, {"transact_date": "2014-06-17", "transact_type": "return", "ISBN": "0-07-013151-4", "transact_time": "14:43:55", "librarian_id": "1999-0002"}]'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)





suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestBookManagement))
unittest.TextTestRunner(verbosity=2).run(suite)