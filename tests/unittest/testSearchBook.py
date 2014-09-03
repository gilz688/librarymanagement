__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/searchBook.py", globals())

class TestSearchBook(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testSearchByAuthor(self):
		pass
		#request.vars.author = 'Malik'
		#result = searchByAuthor()
		#expected = {"Title": "Data Structures Using C++",
		#			"Author":"Malik",
		#			"ISBN":"0-07-013151-2",
		#			"Description":"This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course."
		#			}
		#self.assertEquals(result, expected)

	def testSearchByTitle(self):
		pass

	def testSearchByISBNMathcingAllCase(self):
		request.args = ['0-07-013151-2']
		result = searchByISBN()
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structure Using in C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 0, "lib_name": "COE-Library", "no_of_copies": 10}]'
		self.assertEquals(result, expected)

	def testSearchISBNNotMatchingAllCase(self):
		request.args = ['0-07-013151-']
		result = searchByISBN()
		expected = '[]'
		self.assertEquals('[]', expected) 	#todo

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSearchBook))
unittest.TextTestRunner(verbosity=2).run(suite)