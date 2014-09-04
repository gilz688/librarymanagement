
__author__ = 'librarymanagementteam'

def searchBookByTitle():
	book_title = request.args[0]

	book_list = getBooks(book_title)

	if (len(book_list) == 0):
		raise Exception('No book found for keyword ' +'"'+book_title+'"')

	return response.json(book_list)

def getBooks(book_title):
	book_list = db(db.book).select()
	book_list = book_list.find(lambda eachRow: book_title in eachRow.title)
	return book_list