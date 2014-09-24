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
		try:
			request.post_vars['username'] = 'librarian1'
			request.post_vars['password'] = 'password1'

			result = login()
			expected = {'librarian_id': '1999-0001', 'lib_name': 'COE-Library', 'username': 'librarian1', 'password': '$pbkdf2-sha256$200000$rfW.F4JQaq2VUiqltNaakw$Sh4DXKNrGLmUTOKI0GpungW3bM2rfFYx5jrm3yUyYgo', 'lname': 'Wiggins', 'fname': 'Adrew'}
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
		pass

	def testLogoutWithUserNotLoggedIn(self):
		pass

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAuth))
unittest.TextTestRunner(verbosity=2).run(suite)