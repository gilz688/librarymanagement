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

###
	def testCanReturnBook(self):
		isbn = '0-07-013151-1'
		expected = True
		result = canReturnBook(isbn) 
		self.assertEquals(expected,result)

	def testCannotReturnBook(self):
		isbn = '0-07-013151-1'

		# remove all available copies
		while getAvailableCopies(isbn) > 0:
				removeAvailableCopies(isbn)

		expected = False
		result = canReturnBook(isbn)
		self.assertEquals(expected,result)

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
###

	def testBorrowAvailableCopy(self):
		isbn = '0-07-013151-2'
		expected = getAvailableCopies(isbn) - 1 
		borrowBookCopy(isbn)
		result = getAvailableCopies(isbn)
		self.assertEquals(expected, result)

		db.rollback()

	def testBorrowUnavailableBook(self):
		isbn = '0-07-013151-1'
		reduceToZeroCopies(isbn)
		expected = 'Book is currently unavailable.'
		try:
			borrowBookCopy(isbn)
		except Exception as e:
			self.assertEquals(expected, e.args[0])

		db.rollback()

	def testCanBorrowBook(self):
		isbn = '0-07-013151-1'
		expected = True
		result = canBorrowBook(isbn)
		self.assertEquals(expected,result)

	def testCannotBorrowBook(self):
		isbn = '0-07-013151-1'
		reduceToZeroCopies(isbn)
		expected = False
		result = canBorrowBook(isbn)
		self.assertEquals(expected,result)

		db.rollback()

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)