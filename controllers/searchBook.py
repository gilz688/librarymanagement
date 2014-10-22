__author__ = 'librarymanagementteam'


def searchByAuthor():
    authorLName = request.vars.author
    booksByAuthor = getAuthor(authorLName)
    if (len(booksByAuthor) == 0):
        raise Exception('Book with author containing ' + '"' + authorLName + '"' + ' is unavailable.')
    else:
        return response.json(booksByAuthor)


def searchBookByTitle():
    book_title = request.vars.keyword

    book_list = getBooks(book_title)

    if (len(book_list) == 0):
        raise Exception('No book found for keyword ' + '"' + book_title + '"')

        # filteredBooks = filterResult(book_list)
    return response.json(book_list)


def searchByISBN():
    isbn = request.args[0]
    result = matchBookByISBN(isbn)

    # bookData = filterResultByISBN(result, isbn)

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


""""""

def searchAllBook():
    enableCORS()
    keyword = request.var['keyword']
    start = request.var['start']
    end = request.var['end']
    if not keyword:
        result = None
    if not start or not end:
        result = searchBookByTitleAuthorISBN(keyword)
    else:
        result = searchLimitedBookByTitleAuthorISBN(keyword,start,end)
    return response.json(result)

def searchLimitedBookByTitleAuthorISBN(keyword,start,end):
    pass
    
def searchBookByTitleAuthorISBN(key):
    booksByTitle = matchBookByTitle(key)
    booksByISBN = matchBookByISBN(key)
    booksByAuthor = matchBookByAuthor(key)
    new_book = booksByTitle | booksByISBN | booksByAuthor
    return new_book


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