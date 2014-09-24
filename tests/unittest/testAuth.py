__author__ = 'librarymanagementgroup'

import unittest
import json

from gluon.globals import Request

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

	def testLogin(self):
		try:
			request.post_vars['username'] = 'librarian1'
			request.post_vars['password'] = 'password1'

			result = login()
			expected = {'librarian_id': '1999-0001', 'lib_name': 'COE-Library', 'username': 'librarian1', 'password': '$pbkdf2-sha256$200000$BwCgdM75X6u19p4TAiDkXA$JKHzME6MeIzbUP270RhyIle8L83Q7VNgIMMj3QGxQE', 'lname': 'Wiggins', 'fname': 'Adrew'}
			self.assertEquals(result, expected)
			#self.assertEquals(1, 1)
		except Exception as e:
			self.fail()

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

		logout()
		self.assertFalse(isLoggedIn())

	def testGetLibrarian(self):
		request.post_vars['username'] = 'librarian1'
		request.post_vars['password'] = 'password1'
		login()
		result = getLibrarian()
		expected = {'librarian_id': '1999-0001', 'lib_name': 'COE-Library', 'username': 'librarian1', 'password': '$pbkdf2-sha256$200000$BwCgdM75X6u19p4TAiDkXA$JKHzME6MeIzbUP270RhyIle8L83Q7VNgIMMj3QGxQE', 'lname': 'Wiggins', 'fname': 'Adrew'}
		self.assertEquals(result, expected)

	def testGetLibrarianWithNoUserLoggedIn(self):
		logout()
		result = getLibrarian()
		expected = None
		self.assertEquals(result, expected)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAuth))
unittest.TextTestRunner(verbosity=2).run(suite)