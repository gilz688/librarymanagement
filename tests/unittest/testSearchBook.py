__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/seachBook.py", globals())

class TestSearcgBook(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testSearchByAuthor(self):
		request.vars.author = 'Malik'
		result = searchByAuthor()
		expected = {"Title": "Data Structures Using C++",
					"Author":"Malik",
					"ISBN":"0-07-013151-2",
					"Description":"This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course."
					}
		self.assertEquals(result, expected)

	def testSearchByTitle(self):

	def testSearchByISBN(self):

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSearchBook))
unittest.TextTestRunner(verbosity=2).run(suite)