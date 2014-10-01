
__author__ = 'librarymanagementteam'

def getAvailableCopies(isbn):
	book_copies = getBookByISBN(isbn)
	return book_copies.available_copies	

def getNumOfCopies(isbn):
	book_copies = getBookByISBN(isbn)
	return book_copies.no_of_copies

def canAddCopies(available_copies, num_of_copies):
	if(num_of_copies>available_copies):
		return True
	else:
		return False

def addAvailableCopies(isbn):
	
	available_copies = getAvailableCopies(isbn)
	num_of_copies = getNumOfCopies(isbn)

	if(canAddCopies(available_copies, num_of_copies)):
		addBookAvailableBookCopies(isbn, available_copies)
		book = {'available_copies': available_copies + 1,
			'num_of_copies': num_of_copies}
		return book
	else:
		raise Exception('Maximum number of copies reached')

def returnBook():
	isbn = request.vars.isbn
	library = getBookByISBN(isbn)

	if (session.status == 'logged in' and session.lib_name == library.lib_name):
		try:
			book = addAvailableCopies(isbn)
			bookData = {"message":"Book Returned",
						"available_copies":book['available_copies'],
						"num_of_copies":book['num_of_copies']
						}
			return response.json(bookData)
		except:
			raise Exception("Cannot return book")
	else:
		raise Exception("Insufficient Privileges")

def borrowBook():
	isbn = request.vars.isbn
	bookInfo = getBookByISBN(isbn)
	if (session.status == 'logged in' and session.lib_name == bookInfo.lib_name):
			try:
				book = removeAvailableCopies(isbn)
				bookData = {"message":"Book Borrowed",
							"available_copies":book['available_copies'],
							"num_of_copies":book['num_of_copies']
							}
				return response.json(bookData)
			except:
				raise Exception('Book is currently unavailable.')
	else: 
		raise Exception("Permission Denied")


def canRemoveCopies(available_copies, num_of_copies):
	if(available_copies > 0):
		return True
	else:
		return False

def removeAvailableCopies(isbn):

	available_copies = getAvailableCopies(isbn)
	num_of_copies = getNumOfCopies(isbn)

	if(canRemoveCopies(available_copies, num_of_copies)):
		reduceAvailableBookCopies(isbn, available_copies)
		book = {'available_copies': available_copies - 1,
			'num_of_copies': num_of_copies}
		return book
	else:
		raise Exception('No available copies left')

