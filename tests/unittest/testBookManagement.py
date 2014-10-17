__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/bookManagement.py", globals())



class TestBookManagement(unittest.TestCase):
	pass


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestBookManagement))
unittest.TextTestRunner(verbosity=2).run(suite)