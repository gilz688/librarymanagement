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

	def testCannotAddCopies(self):
		isbn = '0-07-013151-2'

		available_copies = getAvailableCopies(isbn) #10
		num_of_copies = getNumOfCopies(isbn) #11

		expected = False

		while available_copies<num_of_copies:
			addAvailableCopies(isbn)
			available_copies = getAvailableCopies(isbn) # +1 per iteration

		result = canAddCopies(available_copies, num_of_copies)
		self.assertEquals(expected, result)

		db.rollback()

	def testAddAvailableCopies(self):
		isbn = '0-07-013151-2'
		expected = getAvailableCopies(isbn) + 1
		addAvailableCopies(isbn)
		result = getAvailableCopies(isbn)
		self.assertEquals(expected, result)

		db.rollback()
		
	def testAddAvailableCopiesException(self):
		isbn = '0-07-013151-2'
		available_copies = getAvailableCopies(isbn)
		num_of_copies = getNumOfCopies(isbn)

		expected = 'Maximum number of copies reached'

		try:
			while available_copies <= num_of_copies:
				addAvailableCopies(isbn)

		except Exception as e:
			self.assertEquals(expected, e.args[0])

		db.rollback()

	def testSuccessReturnBook(self):
		isbn = '0-07-013151-2'
		request.vars.isbn = isbn
		
		expected = '{"message": "Book Returned", "num_of_copies": 11, "available_copies": 11}'

		result = returnBook()
		
		self.assertEquals(expected,result.encode('ascii', 'ignore'))
		db.rollback()

	def testFailedReturnBook(self):
		isbn = '0-07-013151-1'

		while getAvailableCopies(isbn) < getNumOfCopies(isbn):
				addAvailableCopies(isbn)

		expected = 'Cannot return book'

		try:
			returnBook()
		except Exception as e:
			self.assertEquals(expected, e.args[0])

		db.rollback()

	def testCanRemoveCopies(self):
		expected = True
		result = canRemoveCopies(1, 5)
		self.assertEquals(expected, result)

	def testCannotRemoveCopies(self):
		expected = False
		result = canRemoveCopies(0, 5)
		self.assertEquals(expected, result)

	def testRemoveAvailableCopies(self):
		isbn = '0-07-013151-2'	
		expected = getAvailableCopies(isbn) - 1
		removeAvailableCopies(isbn)
		result = getAvailableCopies(isbn)
		self.assertEquals(expected, result)

		db.rollback()
	
	def testRemoveAvailableCopiesException(self):
		isbn = '0-07-013151-2'

		expected = 'No available copies left'

		try:
			while getAvailableCopies(isbn) > -1:
				removeAvailableCopies(isbn)
		except Exception as e:
			self.assertEquals(expected, e.args[0])

		db.rollback()
		

	def testBorrowAvailableCopy(self):
		request.vars.isbn = '0-07-013151-2'
		
		expected = '{"message": "Book Borrowed", "num_of_copies": 11, "available_copies": 9}'
		result = borrowBook()
		self.assertEquals(expected, result.encode('ascii', 'ignore'))

		db.rollback()

	def testBorrowUnavailableBook(self):
		request.vars.isbn = '0-07-013151-1'
		isbn = request.vars.isbn
		while getAvailableCopies(isbn) > 0:
			removeAvailableCopies(isbn)
		expected = 'Book is currently unavailable.'
		try:
			borrowBook()
		except Exception as e:
			self.assertEquals(expected, e.args[0])

		db.rollback()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)