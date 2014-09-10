
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
	result = db(db.book.ISBN.like('%' + isbn + '%')).select(orderby=db.book.ISBN)

	#bookData = filterResultByISBN(result, isbn)

	if len(result) == 0:
		raise Exception("No Book Found")
	else:
		return response.json(result)
	
"""HELPER FUNCTIONS DOWN"""

def getBooks(book_title):
	book_list = db(db.book.title.like('%'+book_title+'%')).select(orderby=db.book.title)
	return book_list

def getAuthor(book_author):
	authors = db(db.author.lname.like('%'+book_author+'%')).select(orderby=db.author.lname)
	books = db(db.book).select(orderby=db.book.ISBN)
	booksByAuthor = []
	for i in books:
		for auths in authors:
			if (auths.ISBN == i.ISBN):
				booksByAuthor.append(i)
			else:
				continue
	return booksByAuthor