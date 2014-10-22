__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/viewBooks.py", globals())



class TestViewBook(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testLibraryExistence(self):
		request.args=['Unknown-Library']
		try:
			resp = getBooks()
			db.commit()
			self.assertEquals(1, 2)
		except Exception as e:
			self.assertEquals('No library named Unknown-Library', e.args[0])

	def testGetBooks_empty(self):
		request.args=['CED-Library']
		try:
			resp = getBooks()
			db.commit()
			self.assertEquals('[]', resp.encode('ascii','ignore'))
		except Exception as e:
			self.assertEquals(1, 2)

	def testGetBooks_nonEmpty(self):
		request.args=['COE-Library']
		resp = getBooks()
		db.commit()
		self.assertEquals('[{"pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "ISBN": "0-07-013151-7", "title": "3D Computer Graphics"}, {"pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "ISBN": "0-07-013151-9", "title": "Clean Code"}, {"pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "ISBN": "0-07-013151-6", "title": "Computability, Complexity and Languages"}, {"pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "ISBN": "0-07-013151-2", "title": "Data Structures Using C++"}, {"pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "ISBN": "0-07-013151-8", "title": "Fundamentals of Database Systems"}, {"pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "ISBN": "0-07-013151-1", "title": "Introduction to Algorithms"}, {"pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "ISBN": "0-07-013151-11", "title": "Java Foundations"}, {"pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "ISBN": "0-07-013151-12", "title": "Leanrning Python"}, {"pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "ISBN": "0-07-013151-10", "title": "SCRUM in Action"}]', resp.encode('ascii','ignore'))


	def testGetBookInfo_availableBooks(self):
		request.vars.isbn = '0-07-013151-2'
		resp = getBookInfo()
		db.commit()
		self.assertEquals('{"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "library": {"lib_name": "COE-Library", "address": "MSU-IIT SCS"}, "available_copies": 10, "authors": [{"lname": "Malik", "middle_initial": "S", "fname": "D."}], "lib_name": "COE-Library", "no_of_copies": 11}', resp.encode('ascii','ignore'))
	
	def testGetSpecificBookInfo_notAvailableBooks(self):
		request.vars.isbn = ['0-07-013151-50']
		resp = getBookInfo()
		db.commit()
		self.assertEquals('null', resp.encode('ascii', 'ignore'))


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestViewBook))
unittest.TextTestRunner(verbosity=2).run(suite)

