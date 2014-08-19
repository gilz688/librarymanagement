
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

#recieve ajax request with json key isbn	
def addAvailableCopies():
	isbn = request.vars.isbn
	
	available_copies = getAvailableCopies(isbn)
	num_of_copies = getNumOfCopies(isbn)

	if(canAddCopies(available_copies, num_of_copies)):
		db(db.book.ISBN == isbn).update(available_copies = available_copies + 1)
	else:
		raise Exception('Maximum number of copies reached')

def reduceAvailableCopies():
	pass