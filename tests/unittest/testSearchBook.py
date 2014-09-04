__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/searchBook.py", globals())

class TestSearchBook(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testSearchByTitle(self):
		request.args = ['Introduction to Algorithms']
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 0, "lib_name": "COE-Library", "no_of_copies": 20}]'
		result = searchBookByTitle()
		self.assertEquals(expected,result.encode('ascii', 'ignore'))
		
		db.rollback()

	def testSearchByTitleGivenAKeyword(self):
		request.args = ['to']
		expected = '[{"publisher": null, "ISBN": "0-07-013151-3", "description": null, "title": "to be or not to be", "pic": null, "available_copies": 11, "lib_name": "COE-Library", "no_of_copies": 11}, {"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 0, "lib_name": "COE-Library", "no_of_copies": 20}]'
		result = searchBookByTitle()
		self.assertEquals(expected,result.encode('ascii', 'ignore'))
		
		db.rollback()

	def testSearchByTitleException(self):
		request.args = ['Dummy Title']
		expected = 'No book found for keyword "Dummy Title"'
		try:
			searchBookByTitle()
		except Exception as e:
			self.assertEquals(expected, e.args[0])

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSearchBook))
unittest.TextTestRunner(verbosity=2).run(suite)