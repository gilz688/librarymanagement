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
    db = DAL('postgres://postgres:1234asdf@localhost/libman',pool_size=1,check_reserved=['all']) # postgres://username:password@localhost/db_name
    
    db.define_table('library',
				Field('name', unique=True),
                Field('address', length=50))
    
    db.define_table('librarian',
                    Field('id_num', length=9),
                    Field('name', length=50),
                    Field('username', length=30),
                    Field('password', 'password', length=30),
                    primarykey=['id_num'])
    
    db.define_table('book',
					Field('ISBN', 'integer', unique=True, ondelete='CASCADE'),
					Field('library_id', 'reference library'),
					Field('title', length=100),
					Field('publisher_last_name', length=50),
					Field('publisher_first_name', length=50),
					Field('isAvailable', 'boolean'),
					primarykey=['ISBN'])
    
    db.define_table('author',
					Field('ISBN', 'reference book'),
					Field('last_name', length=20),
					Field('first_name', length=30))
    
    db.define_table('manage',
					Field('ISBN', 'reference book'),
					Field('librarian_id', 'reference librarian'),
					Field('trans'),
                    Field('transdate', 'date'))
    
    db.define_table('borrower',
                    Field('id_num', length=9),
					Field('last_name', length=20),
					Field('first_name', length=30),
                    primarykey=['id_num'])
    
    db.define_table('borrowing',
					Field('ISBN', 'reference book'),
					Field('borrwer_id', 'reference borrower'),
					Field('startdate', 'date'),
                    Field('duedate', 'date'))
    
    db.librarian.username.requires= IS_NOT_EMPTY()
    db.librarian.password.requiers= IS_NOT_EMPTY()
    
    db.book.ISBN.requires= IS_NOT_EMPTY()
    db.book.title.requires= IS_NOT_EMPTY()
    db.book.publisher_last_name.requires= IS_NOT_EMPTY()
    db.book.publisher_first_name.requires= IS_NOT_EMPTY()
    db.book.isAvailable.requires= IS_NOT_EMPTY()
    
    db.author.last_name.requires= IS_NOT_EMPTY()
    db.author.first_name.requires= IS_NOT_EMPTY()
    
    db.manage.trans.requires= IS_NOT_EMPTY()
    db.manage.transdate.requires= IS_NOT_EMPTY()
    
    db.borrower.last_name.requires= IS_NOT_EMPTY()
    db.borrower.first_name.requires= IS_NOT_EMPTY()
    
    db.borrowing.startdate.requires= IS_NOT_EMPTY()
    db.borrowing.duedate.requires= IS_NOT_EMPTY()
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

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

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
# auth.enable_record_versioning(db)
