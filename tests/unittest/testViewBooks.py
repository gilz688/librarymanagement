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

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestViewBook))
unittest.TextTestRunner(verbosity=2).run(suite)