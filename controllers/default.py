# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def index():
	response.view="libman/template.html"
	return dict()

def getBooks():
	lib_name= request.args(0)
	books=db(db.book.lib_name==lib_name).select(db.book.title, db.book.ISBN, orderby=db.book.title)
	return response.json(books)

#def getSpecificBook():
#	ISBN=request.args(0,cast=int, otherwise=URL('viewBooks'))
#	book_details=db(db.book.ISBN==ISBN).select().first()
	#authors=db(db.author.ISBN==ISBN).select(orderby=db.author.last_name)
#	return response.json(book_details)
	
def getBookAuthors():
    ISBN = request.args(0, cast=int,otherwise=URL('viewBooks'))
    authors=db(db.author.ISBN == ISBN).select(db.author.lname, db.author.fname, orderby=db.author.last_name)
    #authors=db(db.author).select(db.author.last_name, db.author.first_name, orderby=db.author.id)
    return response.json(authors)

def getSpecificBookInfo():
    ISBN = request.args(0)
    bookInfo = db(db.book.ISBN == ISBN).select(db.book.ISBN, db.book.lib_name, db.book.title, db.book.publisher, db.book.no_of_copies, db.book.available_copies, db.book.description).first()
    return response.json(bookInfo)
