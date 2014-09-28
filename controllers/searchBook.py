
__author__ = 'librarymanagementteam'


def searchByAuthor():
	authorLName = request.vars.author
	booksByAuthor = getAuthor(authorLName)
	if (len(booksByAuthor) == 0):
		raise Exception('Book with author containing '+'"'+authorLName+'"'+' is unavailable.')
	else:
		return response.json(booksByAuthor)

def searchBookByTitle():
	book_title = request.vars.keyword

	book_list = getBooks(book_title)

	if (len(book_list) == 0):
		raise Exception('No book found for keyword ' +'"'+book_title+'"')

	return response.json(book_list)

def searchByISBN():
	isbn = request.args[0]
	result = findBookByISBN(isbn)

	#bookData = filterResultByISBN(result, isbn)

	if len(result) == 0:
		raise Exception("No Book Found")
	else:
		return response.json(result)
	
"""HELPER FUNCTIONS DOWN"""

def getBooks(book_title):
	book_list = findBookByTitle(book_title)
	return book_list

def getAuthor(book_author):
	authors = findBookByAuthor(book_author)
	books = getBooksOrderedByISBN()
	booksByAuthor = []
	for i in books:
		for auths in authors:
			if (auths.ISBN == i.ISBN):
				booksByAuthor.append(i)
			else:
				continue
	return booksByAuthor
