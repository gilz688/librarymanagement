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

	def testSearchByIncompleteAuthorNameWith6Results(self):
		request.vars.author = 'boy'
		result = searchByAuthor()
		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-9", "description": "No Available description.", "title": "Clean Code", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-6", "description": "No Available description.", "title": "Computability, Complexity and Languages", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "Prentice Hall", "ISBN": "0-13-262226-2", "description": "Electronic Devices and Circuit Theory, Eleventh Edition,\u00a0offers a complete, comprehensive survey, focusing on all the essentials you will need to succeed on the job. Setting the standard for nearly 30 years, this highly accurate text is supported by strong pedagogy and content that is ideal for new students of this rapidly changing field. The colorful layout with ample photographs and examples helps you better understand important topics. This text is an excellent reference work for anyone involved with electronic devices and other circuitry applications, such as electrical and technical engineers.", "title": "Electronic Devices and Circuit Theory", "pic": "book.pic.838a2b9c48a17234.3431713174784b6166734c2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 3}, {"publisher": "McGraw-Hill", "ISBN": "0-07-243202-0", "description": "This book is well known and well respected in the civil engineering market and has a following among civil engineers. This book is for civil engineers that teach fluid mechanics both within their discipline and as a service course to mechanical engineering students.", "title": "Fluid Mechanics With Engineering Applications", "pic": "book.pic.bc339d1b7dcf5449.3531775376684a6f74444c2e6a7067.jpg", "available_copies": 6, "lib_name": "COE-Library", "no_of_copies": 6}, {"publisher": "MIT Press", "ISBN": "0-07-013151-3", "description": "No Available description.", "title": "Introduction to Electricity", "pic": "book.pic.9dcd44ba64bbba08.303133353034303837362e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-12", "description": "No Available description.", "title": "Leanrning Python", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}]'
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

		expected = '[{"publisher": "MIT Press", "ISBN": "0-07-013151-9", "description": "No Available description.", "title": "Clean Code", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-6", "description": "No Available description.", "title": "Computability, Complexity and Languages", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-2", "description": "This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.", "title": "Data Structures Using C++", "pic": "book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg", "available_copies": 10, "lib_name": "COE-Library", "no_of_copies": 11}, {"publisher": "Prentice Hall", "ISBN": "0-13-262226-2", "description": "Electronic Devices and Circuit Theory, Eleventh Edition,\u00a0offers a complete, comprehensive survey, focusing on all the essentials you will need to succeed on the job. Setting the standard for nearly 30 years, this highly accurate text is supported by strong pedagogy and content that is ideal for new students of this rapidly changing field. The colorful layout with ample photographs and examples helps you better understand important topics. This text is an excellent reference work for anyone involved with electronic devices and other circuitry applications, such as electrical and technical engineers.", "title": "Electronic Devices and Circuit Theory", "pic": "book.pic.838a2b9c48a17234.3431713174784b6166734c2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 3}, {"publisher": "McGraw-Hill", "ISBN": "0-07-352957-5", "description": "The hallmark feature of this classic text is its focus on the student - it is written so that students may teach the science of circuit analysis to themselves.", "title": "Engineering Circuit Analysis", "pic": "book.pic.b4c4fdb69ffb8951.353136684f47617941524c2e6a7067.jpg", "available_copies": 2, "lib_name": "COE-Library", "no_of_copies": 2}, {"publisher": "McGraw-Hill", "ISBN": "0-07-338066-0", "description": "First published just over 50 years ago and now in its Eighth Edition, Bill Hayt and John Buck\u2019s\u00a0Engineering Electromagnetics\u00a0is a classic text that has been updated for electromagnetics education today. This widely-respected book stresses fundamental concepts and problem solving, and discusses the material in an understandable and readable way.", "title": "Engineering Electromagnetics", "pic": "book.pic.86ebd8d29e30bab8.343141396c5674396f624c2e6a7067.jpg", "available_copies": 2, "lib_name": "COE-Library", "no_of_copies": 2}, {"publisher": "Prentice Hall", "ISBN": "0-13-291548-0", "description": "In his revision of Engineering Mechanics, R.C. Hibbeler empowers\u00bfreaders to succeed in the whole learning experience. Hibbeler achieves this by calling on his everyday classroom experience and his knowledge of how people learn inside and outside of lecture. This text is ideal for civil and mechanical engineering professionals.", "title": "Engineering Mechanics: Statics & Dynamics", "pic": "book.pic.9208293388898e2d.363165705643427772774c202831292e6a7067.jpg", "available_copies": 2, "lib_name": "COE-Library", "no_of_copies": 2}, {"publisher": "McGraw-Hill", "ISBN": "0-07-243202-0", "description": "This book is well known and well respected in the civil engineering market and has a following among civil engineers. This book is for civil engineers that teach fluid mechanics both within their discipline and as a service course to mechanical engineering students.", "title": "Fluid Mechanics With Engineering Applications", "pic": "book.pic.bc339d1b7dcf5449.3531775376684a6f74444c2e6a7067.jpg", "available_copies": 6, "lib_name": "COE-Library", "no_of_copies": 6}, {"publisher": "MIT Press", "ISBN": "0-07-013151-8", "description": "No Available description.", "title": "Fundamentals of Database Systems", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-1", "description": "This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. ", "title": "Introduction to Algorithms", "pic": "book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 20}, {"publisher": "MIT Press", "ISBN": "0-07-013151-3", "description": "No Available description.", "title": "Introduction to Electricity", "pic": "book.pic.9dcd44ba64bbba08.303133353034303837362e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-5", "description": "No Available description.", "title": "Introduction to Electricity(2nd Edition)", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-11", "description": "No Available description.", "title": "Java Foundations", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-12", "description": "No Available description.", "title": "Leanrning Python", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-4", "description": "No Available description.", "title": "Modern Physics for Science and Engineering", "pic": "book.pic.af6a3137da8c88a0.4d6f6465726e50687973696373436f7665722e6a7067.jpg", "available_copies": 3, "lib_name": "SET-Library", "no_of_copies": 5}, {"publisher": "McGraw-Hill", "ISBN": "0-07-322278-X", "description": "The hallmark feature of this classic text is its focus on the student - it is written so that students may teach the science of circuit analysis to themselves.", "title": "Principles of Electronic Communication Systems", "pic": "book.pic.a3321ba89a154bbc.636f6d7379732e6a706567.jpeg", "available_copies": 5, "lib_name": "COE-Library", "no_of_copies": 5}, {"publisher": "MIT Press", "ISBN": "0-07-013151-10", "description": "No Available description.", "title": "SCRUM in Action", "pic": "book.pic.82ce9fecdf325cb3.556e6b6e6f776e2d426f6f6b2e6a7067.jpg", "available_copies": 3, "lib_name": "COE-Library", "no_of_copies": 5}]'
		
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