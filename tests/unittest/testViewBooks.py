__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/viewBooks.py", globals())



class TestViewBook(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testGetBooks_empty(self):
		request.args=['Unknown-Library']
		resp = getBooks()
		db.commit()
		self.assertEquals('[]', resp.encode('ascii','ignore'))

	def testGetBooks_nonEmpty(self):
		request.args=['COE-Library']
		resp = getBooks()
		db.commit()
		self.assertEquals('[{"ISBN": "0-07-013151-2", "title": "Data Structure Using in C++"}, {"ISBN": "0-07-013151-1", "title": "Introduction To Algorithm"}]', resp.encode('ascii','ignore'))

	def testGetSpecificBookInfo_availableBooks(self):
		request.vars.isbn = '0-07-013151-2'
		resp = getSpecificBookInfo()
		db.commit()
		self.assertEquals('{"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structure Using in C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 220}', resp.encode('ascii', 'ignore'))

	def testGetSpecificBookInfo_notAvailableBooks(self):
		request.vars.isbn = ['0-07-013151-9']
		resp = getSpecificBookInfo()
		db.commit()
		self.assertEquals('null', resp.encode('ascii', 'ignore'))

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestViewBook))
unittest.TextTestRunner(verbosity=2).run(suite)