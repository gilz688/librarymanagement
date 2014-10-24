__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request
from gluon.dal import Rows

execfile("applications/librarymanagement/controllers/auth.py", globals())

class TestAuth(unittest.TestCase):
	def setUp(self):
		request = Request("")

	def testValidate(self):
		username = 'librarian1'
		password = 'password1'
		result = validate(username, password)
		self.assertTrue(result)

	def testValidateWithWrongCredentials(self):
		username = 'librarian1'
		password = 'wrongpass'
		result = validate(username, password)
		self.assertFalse(result)

	def testLogin1(self):
		try:
			request.post_vars['username'] = 'librarian1'
			request.post_vars['password'] = 'password1'

			result = login()
			expected = '{"username": "librarian1", "librarian_id": "1999-0001", "lname": "Wiggins", "fname": "Adrew", "lib_name": "COE-Library", "password": "$pbkdf2-sha256$20000$mZMSIkSo9V5rLWUsxfh/Lw$82WC7e84b4BWFxvf/RFRxvXP5c0l0e5IlArPTdOmrms"}'
			self.assertEquals(result, expected)
		except Exception as e:
			self.assertEquals(0,1)

	def testLoginWithWrongUsername(self):
		try:
			request.post_vars['username'] = 'wrong_username'
			request.post_vars['password'] = 'password1'

			result = login()
			self.fail()
		except Exception as e:
			expected = 'Wrong username or password'
			self.assertEquals(expected, e.args[0])


	def testLoginWithWrongPassword(self):
		try:
			request.post_vars['username'] = 'librarian1'
			request.post_vars['password'] = 'wrong_password'

			result = login()
			self.fail()
		except Exception as e:
			expected = 'Wrong username or password'
			self.assertEquals(expected, e.args[0])


	def testIsLoggedIn(self):
		request.post_vars['username'] = 'librarian1'
		request.post_vars['password'] = 'password1'

		login()
		self.assertTrue(isLoggedIn())


	def testIsLoggedInWithUserNotLoggedIn(self):
		logout()
		self.assertFalse(isLoggedIn())

	def testLogout(self):
		request.post_vars['username'] = 'librarian1'
		request.post_vars['password'] = 'password1'

		login()
		self.assertTrue(isLoggedIn())

		logout()
		self.assertFalse(isLoggedIn())

	def testLogoutWithUserNotLoggedIn(self):
		logout()
		self.assertFalse(isLoggedIn())


	def testGetLibrarian(self):
		request.post_vars['username'] = 'librarian1'
		request.post_vars['password'] = 'password1'
		login()
		result = getLibrarian('librarian1')
		expected = {'username': 'librarian1', 'librarian_id': '1999-0001', 'lname': 'Wiggins', 'fname': 'Adrew', 'lib_name': 'COE-Library', 'password': '$pbkdf2-sha256$20000$mZMSIkSo9V5rLWUsxfh/Lw$82WC7e84b4BWFxvf/RFRxvXP5c0l0e5IlArPTdOmrms'}
		self.assertEquals(result, expected)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAuth))
unittest.TextTestRunner(verbosity=2).run(suite)