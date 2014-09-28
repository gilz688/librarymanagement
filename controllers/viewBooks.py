__author__ = 'librarymanagementteam'

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def getBooks():
	lib_name= request.args[0]
	library = getLibrary(lib_name)
	if len(library) == 0:
		raise Exception('No library named ' + lib_name)
	books=getBookByLibrary(lib_name)
	return response.json(books)

def getBookAuthors():
    ISBN = request.vars.isbn
    authors=getBookAuthor(ISBN)
    if len(authors) == 0:
        raise Exception('No Book with ISBN ' + ISBN)
    return response.json(authors)

def getSpecificBookInfo():
    ISBN = request.vars.isbn
    bookInfo = getBookByISBN(ISBN)
    return response.json(bookInfo)