
__author__ = 'librarymanagementteam'

def searchBookByTitle():
	book_title = request.args[0]

	book_list = getBooks(book_title)

	if (len(book_list) == 0):
		raise Exception('NO book found for keyword ' + book_title)

	return response.json(book_list)

def getBooks(book_title):
	book_list = db(db.book.title==book_title).select()
	return book_list