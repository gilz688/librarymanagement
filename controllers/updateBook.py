
__author__ = 'librarymanagementteam'

def getAvailableCopies(isbn):
	no_of_copies = db(db.book.ISBN == isbn).select(db.book.available_copies)
	return no_of_copies[0].available_copies

#recieve ajax request with json key isbn	
def addAvailableCopies():
	isbn = request.vars.isbn
	no_of_copies = getAvailableCopies(isbn)
	db(db.book.ISBN == isbn).update(available_copies = no_of_copies + 1)


def reduceAvailableCopies():
	pass