__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

execfile("applications/librarymanagement/controllers/auth.py", globals())

class TestAuth(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testValidate(self):
		pass

	def testValidateWithWrongCredentials(self):
		pass

	def testLogin(self):
		request.post_vars['username'] = 'librarian1'
		request.post_vars['password'] = 'password1'
		
		self.assertEquals(1, 1)

	def testLoginWithWrongUsername(self):
		pass

	def testLoginWithWrongPassword(self):
		pass

	def testIsLoggedIn(self):
		pass

	def testIsLoggedInWithUserNotLoggedIn(self):
		pass

	def testLogout(self):
		pass

	def testLogoutWithUserNotLoggedIn(self):
		pass

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAuth))
unittest.TextTestRunner(verbosity=2).run(suite)