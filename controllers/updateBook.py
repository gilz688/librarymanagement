
__author__ = 'librarymanagementteam'

# recieve ajax request with json key isbn and no_of_copies
def addAvaialbleCopies():
	isbn = request.vars.isbn
	no_of_copies = request.vars.no_of_copies
	db(db.book.isbn == isbn).update(available_copies = no_of_copies + 1)

def reduceAvailableCopies():