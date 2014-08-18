__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/updateBook.py", globals())

class TestUpdateBook(unittest.TestCase):
	def setUp(self):
		request = Request("")	

	def testAddAvailableCopies(self):
		db.commit()
		isbn = '0-07-013151-2'
		request.vars.isbn = isbn
		expected = getAvailableCopies(isbn) + 1
		addAvailableCopies()
		result = getAvailableCopies(isbn)
		db.rollback()
		self.assertEquals(expected, result)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)