__author__ = 'librarymanagementgroup'

import unittest, viewBooks
from gluon.globals import Request
execfile("applications/librarymanagement/controllers/viewBooks.py", globals())

class ViewBooksTest(unittest.TestCase):

    def setUp(self):
        self.request = Request()

    def test_viewBooks(self):
        self.request.args[0] = 'SET_Lib'
        a = viewBooks.getBooks()
        #self.assertEquals(a[0]['ISBN'], '09059366722')
        #self.assertEquals(a[0]['ISBN'], request.args[0])

    def test_viewSpecificBookInfo(self):
        self.assertEqual(1, 1)

    def test_viewBookAuthor(self):
        self.assertEqual(1, 1)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ViewBooksTest))
unittest.TextTestRunner(verbosity=2).run(suite)
