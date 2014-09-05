
__author__ = 'librarymanagementteam'


def searchByAuthor():
	author = request.vars.author
	try:
		
		bookData = {"Title": book['title'],
					"Author":book['author'],
					"ISBN":book['isbn'],
					"Description":book['description']
					}
		return response.json(bookData)
	except:
		raise Exception('Book written by that author is unavailable.')

def searchBookByTitle():
	book_title = request.vars.keyword

	book_list = getBooks(book_title)

	if (len(book_list) == 0):
		raise Exception('No book found for keyword ' +'"'+book_title+'"')

	return response.json(book_list)

def getBooks(book_title):
	book_list = db(db.book).select()
	book_list = book_list.find(lambda eachRow: book_title in eachRow.title)
	return book_list

def searchByISBN():
	isbn = request.args
	if len(isbn[0]) == 13:
		bookData = searchWithCompleteISBN(isbn[0])
	else:
		bookData = searchWithIncompleteISBN(isbn[0])

	if len(bookData) == 0:
		raise Exception("No Book Found")
	return response.json(bookData)

"""HELPER FUNCTIONS DOWN"""


def searchWithCompleteISBN(isbn):
	result = db(db.book.ISBN==isbn).select()
	return result

def searchWithIncompleteISBN(isbn):
	result = db().select(db.book.ALL, having=isbn)
	return result

