__author__ = 'librarymanagementteam'


def searchByAuthor():
    authorLName = request.vars.author
    booksByAuthor = matchBookByAuthor(authorLName)
    if (len(booksByAuthor) == 0):
        raise Exception('Book with author containing ' + '"' + authorLName + '"' + ' is unavailable.')
    else:
        return response.json(booksByAuthor)


def searchBookByTitle():
    book_title = request.vars.keyword

    book_list = matchBookByTitle(book_title)

    if (len(book_list) == 0):
        raise Exception('No book found for keyword ' + '"' + book_title + '"')

    return response.json(book_list)


def searchByISBN():
    isbn = request.args[0]
    result = matchBookByISBN(isbn)

    if len(result) == 0:
        raise Exception("No Book Found")
    else:
        return response.json(result)


def searchAllBook():
    enableCORS()
    keyword = request.vars['keyword']
    start = request.vars['start']
    end = request.vars['end']
    if not keyword:
        result = None
    if not start or not end:
        result = matchBook(keyword)
    else:
        result = matchPaginatedBook(keyword,start,end)
    return response.json(result)


def enableCORS():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'




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