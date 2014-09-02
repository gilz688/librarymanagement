
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
	

def searchByISBN():
	
