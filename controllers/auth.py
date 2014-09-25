__author__ = 'librarymanagementteam'

from passlib.hash import pbkdf2_sha256

def login():
	username = request.post_vars['username']
	password = request.post_vars['password']

	if validate(username, password):
		session.username = username
		session.status = 'logged in'
		librarian = getLibrarian()
		return response.json(librarian)
	else:
		raise Exception("Wrong username or password")

def logout():
	session.username = None
	session.status = None

'''
	Helper Functions
'''

def isLoggedIn():
	if (session.username is not None) and (session.status is not None):
		return True
	else:
		return False

def validate(username,password):
	try:
		librarian=db(db.librarian.username==username).select(db.librarian.password).first()
		if(pbkdf2_sha256.verify(password, librarian.password)):
			return True
		else:
			return False
	except Exception as e:
		return False

def getLibrarian():
	if(isLoggedIn()):
		librarian=db(db.librarian.username==session.username).select(db.librarian.ALL).first()
		return librarian
	else:
		return None