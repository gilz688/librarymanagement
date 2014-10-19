__author__ = 'librarymanagementteam'

def download():
    enableCORS()
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


def getBookInfo():
    enableCORS()
    ISBN = request.vars.isbn
    
    book = getBookByISBN(ISBN)
    authors = getBookAuthor(ISBN)
    library = getLibraryByBook(ISBN)
    
    if(book):
        book = dict(book)
        book['authors'] = authors
        book['library'] = library
        
    return response.json(book)

def getAllBooks():
    enableCORS()
    items = response.vars.items;
    page = response.vars.page;
    if (not page) | (not items):
        books = getBooksOrderedByISBN()
    else:
        books = getPaginatedBooksOrderedByISBN(items,page)
    return response.json(books)

def enableCORS():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'