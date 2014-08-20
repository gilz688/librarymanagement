
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
def addAvailableCopies(isbn):
	
	available_copies = getAvailableCopies(isbn)
	num_of_copies = getNumOfCopies(isbn)

	if(canAddCopies(available_copies, num_of_copies)):
		db(db.book.ISBN == isbn).update(available_copies = available_copies + 1)
	else:
		raise Exception('Maximum number of copies reached')

def borrowBookCopy():
	isbn = request.vars.isbn
	if (canBorrowBook(isbn)):
		db(db.book.ISBN == isbn).update(available_copies = availableCopies - 1)
	else:
		raise Exception('Book is currently unavailable.')

def canBorrowBook(isbn):
	if(getAvailableCopies(isbn) > 0):
		return True
	else:
		return False

## Mao man ata ni ako gbuhat sa ibabaw
## def reduceAvailableCopies():
##	pass

## for testing purposes only
def reduceToZeroCopies(isbn):
	db(db.book.ISBN == isbn).update(available_copies = 0)