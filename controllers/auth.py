__author__ = 'librarymanagementteam'

from passlib.hash import pbkdf2_sha256

def login():
	username = request.post_vars['username']
	password = request.post_vars['password']

	if validate(username, password):
		librarian = getLibrarian(username)
		createSession(username, librarian['lib_name'], librarian['librarian_id'])
		return response.json(librarian)
	else:
		raise Exception("Wrong username or password")

def logout():
	session.clear()

'''
	Helper Functions
'''

def validate(username,password):
	try:
		librarian=getLibrarianPassword(username)
		if(pbkdf2_sha256.verify(password, librarian.password)):
			return True
		else:
			return False
	except Exception as e:
		return False

def isLoggedIn():
	if (session.username is not None) and (session.status is not None) and (session.lib_name is not None):
		return True
	else:
		return False

def createSession(username, lib_name, lib_id):
	session.username = username
	session.lib_name = lib_name
	session.status = 'logged in'
	session.lib_id = lib_id

def getSession():
	if(isLoggedIn()):
		mySession = {'username': session.username,
			'lib_name': session.lib_name,
			'status': session.status}
		return response.json(mySession)
	else:
		return response.json(None)

def getLibrarian(username):
	librarian=getLibrarianUsingUsername(username)
	return dict(librarian)