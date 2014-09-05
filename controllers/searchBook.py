
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