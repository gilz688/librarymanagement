__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/searchBook.py", globals())

class TestSearchBook(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testSearchByAuthor(self):
		request.vars.author = 'Cormen'
		result = searchByAuthor()
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}]'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testSearchByIncompleteAuthorName1Result(self):
		request.vars.author = 'Cor'
		result = searchByAuthor()
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}]'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testSearchByIncompleteAuthorNameWith2Results(self):
		request.vars.author = 'i'
		result = searchByAuthor()
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}, {"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 11}]'
		self.assertEquals(result.encode('ascii', 'ignore'), expected)

	def testSearchByTitle(self):
		request.vars.keyword = 'Introduction to Algorithms'
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}]'
		result = searchBookByTitle()
		self.assertEquals(expected,result.encode('ascii', 'ignore'))
		
		db.rollback()

	def testSearchByTitleGivenAKeyword(self):
		request.vars.keyword = 'n'
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 11}, {"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}]'
		result = searchBookByTitle()
		self.assertEquals(expected,result.encode('ascii', 'ignore'))
		
		db.rollback()

	def testSearchByTitleException(self):
		request.vars.keyword = 'Dummy Title'
		expected = 'No book found for keyword "Dummy Title"'
		try:
			searchBookByTitle()
		except Exception as e:
			self.assertEquals(expected, e.args[0])
			
	def testSearchByISBNMathcingAllCase(self):
		try:
			request.args = ['0-07-013151-2']
			result = searchByISBN()
			expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 11}]'
			"""
			for item in expected:
				if item in result:
					continue
				else:
					self.assertEquals(0, 1)
			
			self.assertEquals(0, 0)
			"""
			self.assertEquals(result, expected)
		except Exception as e:
			self.assertEquals(0, 1)
	
	def testSearchISBNNotMatchingAllCase(self):
		try:
			request.args = ['0-07-013151-']
			result = searchByISBN()
			expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}, {"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 11}]'
			"""
			for item in expected:
				if item in expected:
					continue
				else:
					self.assertEquals(0, 1)
				
				self.assertEquals(0, 0)
			"""
			self.assertEquals(result, expected)
		except Exception as e:
			self.assertEquals(0, 1)
	
	def testSearchISBNWithNoMatch(self):
		try:
			request.args = ['0-07-013151-3']
			result = searchByISBN()
			self.assertEquals(0, 1)
		except Exception as e:
			self.assertEquals('No Book Found', e.args[0])
	
	def testSearchISNWithInvalidISBN(self):
		try:
			request.args = ['asdf']
			result = searchByISBN()
			self.assertEquals(0, 1)
		except Exception as e:
			self.assertEquals('No Book Found', e.args[0])
	
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSearchBook))
unittest.TextTestRunner(verbosity=2).run(suite)