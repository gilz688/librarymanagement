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
		expected = 220
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
		db.commit()
		isbn = '0-07-013151-2'
		request.vars.isbn = isbn
		expected = getAvailableCopies(isbn) + 1
		addAvailableCopies()
		result = getAvailableCopies(isbn)
		db.rollback()
		self.assertEquals(expected, result)

	def testAddAvailableCopiesException(self):
		pass	

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)