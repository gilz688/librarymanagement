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

	def testSearchByAuthorNoMatch(self):
		request.vars.author = 'Gwapo'
		expected = 'Book with author containing "Gwapo" is unavailable.'
		try:
			searchByAuthor()
		except Exception as e:
			self.assertEquals(expected, e.args[0])	

	def testSearchByTitle(self):
		request.vars.keyword = 'Introduction to Algorithms'
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}]'
		result = searchBookByTitle()
		self.assertEquals(expected,result.encode('ascii', 'ignore'))
		
		db.rollback()

	def testSearchByTitleGivenAKeyword(self):
		request.vars.keyword = 'n'

		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-9", "description": "No Available description.", "title": "Clean Code", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-6", "description": "No Available description.", "title": "Computability, Complexity and Languages", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 11}, {"publisher": "MIT Press", "ISBN": "0-07-013151-8", "description": "No Available description.", "title": "Fundamentals of Database Systems", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}, {"publisher": "MIT Press", "ISBN": "0-07-013151-3", "description": "No Available description.", "title": "Introduction to Electricity", "pic": "book.pic.9dcd44ba64bbba08.303133353034303837362e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-5", "description": "No Available description.", "title": "Introduction to Electricity(2nd Edition)", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-11", "description": "No Available description.", "title": "Java Foundations", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-12", "description": "No Available description.", "title": "Leanrning Python", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-4", "description": "No Available description.", "title": "Modern Physics for Science and Engineering", "pic": "book.pic.af6a3137da8c88a0.4d6f6465726e50687973696373436f7665722e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-10", "description": "No Available description.", "title": "SCRUM in Action", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}]'

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

			expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-7", "description": "No Available description.", "title": "3D Computer Graphics", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-9", "description": "No Available description.", "title": "Clean Code", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-6", "description": "No Available description.", "title": "Computability, Complexity and Languages", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 11}, {"publisher": "MIT Press", "ISBN": "0-07-013151-8", "description": "No Available description.", "title": "Fundamentals of Database Systems", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}, {"publisher": "MIT Press", "ISBN": "0-07-013151-3", "description": "No Available description.", "title": "Introduction to Electricity", "pic": "book.pic.9dcd44ba64bbba08.303133353034303837362e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-5", "description": "No Available description.", "title": "Introduction to Electricity(2nd Edition)", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-11", "description": "No Available description.", "title": "Java Foundations", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-12", "description": "No Available description.", "title": "Leanrning Python", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-4", "description": "No Available description.", "title": "Modern Physics for Science and Engineering", "pic": "book.pic.af6a3137da8c88a0.4d6f6465726e50687973696373436f7665722e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-10", "description": "No Available description.", "title": "SCRUM in Action", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}]'

			self.assertEquals(result, expected)
		except Exception as e:
			self.assertEquals(0, 1)
	
	def testSearchISBNWithNoMatch(self):
		try:
			request.args = ['0-07-013151-50']
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