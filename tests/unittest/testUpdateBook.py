__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/updateBook.py", globals())

class TestUpdateBook(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testGetAvailableCopies(self):
		isbn = '0-07-013151-2'
		expected = 10
		result = getAvailableCopies(isbn)
		self.assertEquals(expected, result)

	def testGetNumOfCopies(self):
		isbn = '0-07-013151-2'
		expected = 11
		result = getNumOfCopies(isbn)
		self.assertEquals(expected, result)

	def testCanAddCopies(self):
		isbn = '0-07-013151-2'
		available_copies = getAvailableCopies(isbn)
		num_of_copies = getNumOfCopies(isbn)
		expected = True
		result = canAddCopies(available_copies, num_of_copies)
		self.assertEquals(expected, result)

	def testAddAvailableCopies(self):
		isbn = '0-07-013151-2'
		request.vars.isbn = isbn

		db.commit()

		expected = getAvailableCopies(isbn) + 1
		addAvailableCopies()
		result = getAvailableCopies(isbn)
		self.assertEquals(expected, result)

		db.rollback()
		
	def testAddAvailableCopiesException(self):
		isbn = '0-07-013151-2'
		request.vars.isbn = isbn
		expected = 'Maximum number of copies reached'

		db.commit

		try:
			addAvailableCopies()
			addAvailableCopies()
		except Exception as e:
			self.assertEquals(expected, e.args[0])

		db.rollback()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)