
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

	#filteredBooks = filterResult(book_list)
	return response.json(book_list)

def searchByISBN():
	isbn = request.args[0]
	result = matchBookByISBN(isbn)

	#bookData = filterResultByISBN(result, isbn)

	if len(result) == 0:
		raise Exception("No Book Found")
	else:
		return response.json(result)
	
"""HELPER FUNCTIONS DOWN"""

def getBooks(book_title):
	book_list = matchBookByTitle(book_title)
	return book_list

def getAuthor(book_author):
	authors = matchBookByAuthor(book_author)
	books = getBooksOrderedByISBN()
	booksByAuthor = []
	for i in books:
		for auths in authors:
			if (auths.ISBN == i.ISBN):
				booksByAuthor.append(i)
			else:
				continue
	return booksByAuthor

'''

def filterResult(books):
	filteredBooks = dict()
	currLibrary = books[0]['lib_name']
	libraryBooks = []
	for i in books:
		if(currLibrary == i.lib_name):
			libraryBooks.append(i)
		else:
			filteredBooks.update({currLibrary : libraryBooks})
			currLibrary = i['lib_name']
			libraryBooks = [i]
	filteredBooks.update({currLibrary : libraryBooks})
	
	return dict(filteredBooks)
'''