__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request




suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUpdateBook))
unittest.TextTestRunner(verbosity=2).run(suite)