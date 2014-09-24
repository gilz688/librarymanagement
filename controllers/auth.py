__author__ = 'librarymanagementteam'

from passlib.hash import pbkdf2_sha256

def login():
	username = 'librarian1' #request.post_vars['username']
	password = 'password1' #request.post_vars['password']

	librarian = validate(username, password)

	if len(librarian) == 0:
		raise Exception("Wrong username or password")

	session.username = username
	session.status = 'logged in'
	return response.json(librarian)

def isLoggedIn():
	if (session.username is not None) and (session.status is not None):
		return True
	else:
		return False

def validate(username,password):
	try:
		librarian=db(db.librarian.username==session.username).select(db.librarian.password).first()
	except Exception as e:
		return False

	if(pbkdf2_sha256.verify(password, librarian.password)):
		return True
	else:
		return False

def logout():
	session.username = None
	session.status = None

def getLibrarian():
	if(isLoggedIn()):
		librarian=db(db.librarian.username==session.username).select(db.librarian.ALL).first()
		return librarian
	else:
		return None