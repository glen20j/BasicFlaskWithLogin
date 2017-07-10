import os
basedir = os.path.abspath(os.path.dirname(__file__))

#POSTGREL DATABASE STRING
SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://YourUsername:YourPassword@localhost/AFL_Schedule'

#UPDATES CHANGES TO DATABASE FOR MIGRATION
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#USED BY WTF FORMS WHEN BUILDING tokens
WTF_CSRF_ENABLED = True
SECRET_KEY = 'SOME_SECRET_IN_HERE'
