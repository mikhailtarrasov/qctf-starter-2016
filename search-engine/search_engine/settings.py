import os


MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB_NAME = 'search_engine'

ES_INDEX_NAME = 'search_engine'

CRAWLER_THREADS = 3

SECRET_KEY = os.environ['FLASK_SECRET_KEY']