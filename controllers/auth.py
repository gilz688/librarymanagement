
__author__ = 'librarymanagementteam'


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

#gil, gamit atong verify na method sa password :D
def validate():
	pass

def logout():
	pass
