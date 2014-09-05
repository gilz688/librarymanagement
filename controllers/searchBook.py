
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
	result = db().select(db.book.ALL)

	bookData = filterResultByISBN(result, isbn[0])

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