# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

# # if NOT running on Google App Engine use SQLite or other DB


db = DAL('postgres://postgres:1234asdf@127.0.0.1:5432/libman', pool_size=1, check_reserved=['all'],
         migrate= True, fake_migrate=True)  # postgres://username:password@localhost/db_name

db.define_table('library',
                Field('lib_name', length=20, unique=True, ondelete='CASCADE'),
                Field('address', length=50),
                primarykey=['lib_name'])

db.define_table('librarian',
                Field('librarian_id', unique=True, ondelete='CASCADE'),
                Field('lib_name', db.library.lib_name),
                Field('username', length=10),
                Field('password', 'password', length=20),
                Field('lname', length=15),
                Field('fname', length=15),
                primarykey=['librarian_id'])

db.define_table('book',
                Field('ISBN', length=20, unique=True, ondelete='CASCADE'),
                Field('lib_name', db.library.lib_name),
                Field('title', length=100),
                Field('pic', 'upload'),
                Field('publisher', length=100),
                Field('no_of_copies', 'integer'),
                Field('available_copies', 'integer'),
                Field('description', 'text'),
                #Field('borrow_count', 'integer'),
                #Field('return_count', 'integer'),
                primarykey=['ISBN'])

db.define_table('author',
                Field('ISBN', db.book.ISBN),
                Field('lname', length=15),
                Field('fname', length=15),
				Field('middle_initial', length=1))

db.define_table('borrower',
                Field('borrower_id', length=15),
                Field('lib_name', db.library.lib_name),
                Field('lname', length=15),
                Field('fname', length=15),
                primarykey=['borrower_id'])

db.define_table('borrow_book',
                Field('ISBN', db.book.ISBN),
                Field('borrow_date', 'date'),
                Field('return_date', 'date'))

#populate database
#dummy values
'''
#library
db.library.insert(**{'lib_name': 'COE-Library', 'address': 'MSU-IIT SCS'})
db.library.insert(**{'lib_name': 'SET-Library', 'address': 'MSU-IIT SET'})

#book

db.book.insert(**{'ISBN': '0-07-013151-1', 'lib_name': 'COE-Library','publisher': 'MIT Press',
                  'title': 'Introduction to Algorithms', 'no_of_copies': 20, 'available_copies': 5,
				  'pic': 'book.pic.8f51fb150a423756.362d3034366a6630352e6a7067.jpg',
				  'description': 'This book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. '})

db.book.insert(**{'ISBN': '0-07-013151-2', 'lib_name': 'COE-Library','publisher': 'MIT Press',
                  'title': 'Data Structures Using C++', 'no_of_copies': 11, 'available_copies': 10,
				  'pic': 'book.pic.81914475beb94577.646174612d737472756374757265732d7573696e672d632d642d732d6d616c696b2d70617065726261636b2d636f7665722d6172742e6a7067.jpg',
                  'description': 'This book takes a gentle approach to the data structures course in C++. Providing an early, self-contained review of object-oriented programming and C++, this text gives students a firm grasp of key concepts and allows those experienced in another language to adjust easily. Flexible by design, professors have the option of emphasizing object-oriented programming, covering recursion and sorting early, or accelerating the pace of the course.'})

db.author.bulk_insert([{'ISBN': '0-07-013151-1', 'lname': 'Cormen', 'fname': 'Thomas', 'middle_initial': 'H'},
                        {'ISBN': '0-07-013151-1', 'lname': 'Leiserson', 'fname': 'Charles', 'middle_initial': 'E'},
                        {'ISBN': '0-07-013151-2', 'lname': 'Malik', 'fname': 'D.', 'middle_initial': 'S'}
                    ])

db.commit()
'''
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
