__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/auth.py", globals())

class TestAuth(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testValidate:
		pass

	def testValidateWithWrongCredentials:
		pass

	def testLogin:
		pass

	def testLoginWithWrongUsername:
		pass

	def testLoginWithWrongPassword:
		pass

	def testIsLoggedIn:
		pass

	def testIsLoggedInWithUserNotLoggedIn:
		pass

	def testLogout:
		pass

	def testLogoutWithUserNotLoggedIn:
		pass

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAuth))
unittest.TextTestRunner(verbosity=2).run(suite)