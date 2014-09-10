
__author__ = 'librarymanagementteam'


def searchByAuthor():
	authorLName = request.vars.author
	booksByAuthor = getAuthor(authorLName)
	if (len(booksByAuthor) == 0):
		raise Exception('Book with author containing '+'"'+authorLName+'"'+' is unavailable.')
	else:
		return response.json(booksByAuthor)
		

def getAuthor(book_author):
	authors = db(db.author).select(orderby=db.author.lname)
	authors = authors.find(lambda eachRow: book_author in eachRow.lname)
	books = db(db.book).select(orderby=db.book.ISBN)
	booksByAuthor = []
	for i in books:
		for auths in authors:
			if (auths.ISBN == i.ISBN):
				booksByAuthor.append(i)
			else:
				continue
	#booksByAuthor = db(db.book.ISBN == auths.ISBN).select(orderby=db.book.ISBN)
	return booksByAuthor


def searchBookByTitle():
	book_title = request.vars.keyword

	book_list = getBooks(book_title)

	if (len(book_list) == 0):
		raise Exception('No book found for keyword ' +'"'+book_title+'"')

	return response.json(book_list)

def searchByISBN():
	isbn = request.args[0]
	result = db().select(db.book.ALL, orderby=db.book.ISBN)

	bookData = filterResultByISBN(result, isbn)

	if len(bookData) == 0:
		raise Exception("No Book Found")
	else:
		return response.json(bookData)
	
"""HELPER FUNCTIONS DOWN"""

def filterResultByISBN(unfilteredList, isbn):
	result = []
	for item in unfilteredList:
		if isbn in item.ISBN:
			result.append(item)
		else:
			continue
	return result

def getBooks(book_title):
	book_list = db(db.book.title.like('%'+book_title+'%')).select(orderby=db.book.title)
	return book_list