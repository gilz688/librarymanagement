
__author__ = 'librarymanagementteam'

def getAvailableCopies(isbn):
	book_copies = db(db.book.ISBN == isbn).select(db.book.available_copies).first()
	return book_copies.available_copies	

def getNumOfCopies(isbn):
	book_copies = db(db.book.ISBN == isbn).select(db.book.no_of_copies).first()
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
		db(db.book.ISBN == isbn).update(available_copies = available_copies + 1)
	else:
		raise Exception('Maximum number of copies reached')

def returnBook():
	isbn = request.vars.isbn

	try:
		addAvailableCopies(isbn)
		return response.json({"message":"Book Returned"})
	except:
		raise Exception("Cannot return book")

def borrowBook():
	isbn = request.vars.isbn
	availableCopies = getAvailableCopies(isbn)
	if (canBorrowBook(isbn)):
		db(db.book.ISBN == isbn).update(available_copies = availableCopies - 1)
		return response.json({"message":"Book Borrowed"})
	else:
		raise Exception('Book is currently unavailable.')

def canRemoveCopies(available_copies, num_of_copies):
	if(available_copies > 0):
		return True
	else:
		return False

def removeAvailableCopies(isbn):

	available_copies = getAvailableCopies(isbn)
	num_of_copies = getNumOfCopies(isbn)

	if(canRemoveCopies(available_copies, num_of_copies)):
		db(db.book.ISBN == isbn).update(available_copies = available_copies - 1)
	else:
		raise Exception('No available copies left')

