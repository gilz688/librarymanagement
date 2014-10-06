__author__ = 'librarymanagementteam'

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def getBooks():
    enableCORS()
    lib_name= request.args[0]
    library = getLibrary(lib_name)
    if len(library) == 0:
        raise Exception('No library named ' + lib_name)
    books=getBookByLibrary(lib_name)
    return response.json(books)
    
def getBookAuthors():
    enableCORS()
    ISBN = request.vars.isbn
    authors=getBookAuthor(ISBN)
    if len(authors) == 0:
        raise Exception('No Book with ISBN ' + ISBN)
    return response.json(authors)

def getSpecificBookInfo():
    enableCORS()
    ISBN = request.vars.isbn
    bookInfo = getBookByISBN(ISBN)
    return response.json(bookInfo)

def enableCORS():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'