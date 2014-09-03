
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

def searchByTitle():
	pass

def searchByISBN():
	isbn = request.args
	if len(isbn[0]) == 13:
		bookData = searchWithCompleteISBN(isbn[0])
	else:
		bookData = searchWithIncompleteISBN(isbn[0])

	if len(bookData) == 0:
		raise Exception("No Books Found")
	return response.json(bookData)

"""HELPER FUNCTIONS DOWN"""


def searchWithCompleteISBN(isbn):
	result = db(db.book.ISBN==isbn).select()
	return result

def searchWithIncompleteISBN(isbn):
	result = db().select(db.book.ALL, having=isbn)
	return result