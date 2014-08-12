__author__ = 'librarymanagementteam'

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def getBooks():
	lib_name= request.args[0]
	books=db(db.book.lib_name==lib_name).select(db.book.title, db.book.ISBN, orderby=db.book.title)
	return response.json(books)

def getBookAuthors():
    ISBN = request.vars.isbn
    authors=db(db.author.ISBN == ISBN).select(db.author.lname, db.author.fname, db.author.middle_initial, orderby=db.author.lname)
    #authors=db(db.author).select(db.author.last_name, db.author.first_name, orderby=db.author.id)
    return response.json(authors)

def getSpecificBookInfo():
    ISBN = request.vars.isbn
    bookInfo = db(db.book.ISBN == ISBN).select(db.book.ALL).first()
    return response.json(bookInfo)

#def getSpecificBook():
#	ISBN=request.args(0,cast=int, otherwise=URL('viewBooks'))
#	book_details=db(db.book.ISBN==ISBN).select().first()
	#authors=db(db.author.ISBN==ISBN).select(orderby=db.author.last_name)
#	return response.json(book_details)