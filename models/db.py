# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
	db=DAL("postgres://postgres:postgres@localhost:5432/librarymanagement", pool_size=1, lazy_tables=True)
	
	db.define_table('library',
				Field('name', unique=True))

	db.define_table('librarian',
					Field('library_id', 'reference library'),
					Field('username', unique=True),
					Field('password', 'password'))
					
	db.define_table('book',
					Field('ISBN', 'integer', unique=True, ondelete='CASCADE'),
					Field('library_id', 'reference library'),
					Field('title'),
					Field('publisher_last_name'),
					Field('publisher_first_name'),
					Field('isAvailable', 'boolean'),
					primarykey=['ISBN'])
					
	db.define_table('author',
					Field('ISBN', 'reference book'),
					Field('last_name'),
					Field('first_name'))

	db.define_table('manage',
					Field('ISBN', 'reference book'),
					Field('librarian_id', 'reference librarian'),
					Field('action'))

	db.define_table('borrower',
					Field('last_name'),
					Field('first_name'))

	db.define_table('borrowing',
					Field('ISBN' 'reference book'),
					Field('borrwer_id', 'reference borrower'),
					Field('date', 'date'))
	
	db.librarian.username.requires= IS_NOT_EMPTY()
	db.librarian.password.requiers= IS_NOT_EMPTY()

	db.book.ISBN.requires= IS_NOT_EMPTY()
	db.book.title.requires= IS_NOT_EMPTY()
	db.book.publisher_last_name.requires= IS_NOT_EMPTY()
	db.book.publisher_first_name.requires= IS_NOT_EMPTY()
	db.book.isAvailable.requires= IS_NOT_EMPTY()

	db.author.last_name.requires= IS_NOT_EMPTY()
	db.author.first_name.requires= IS_NOT_EMPTY()

	db.manage.action.requires= IS_NOT_EMPTY()

	db.borrower.last_name.requires= IS_NOT_EMPTY()
	db.borrower.first_name.requires= IS_NOT_EMPTY()

else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################
#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
