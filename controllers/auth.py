
__author__ = 'librarymanagementteam'


def login():
	username = request.post_vars['username']
	password = request.post_vars['password']

	list = []
	list.append(username)
	list.append(password)

	return response.json(list)

def isLoggedIn():
	pass

def validate():
	pass

def logout():
	pass
