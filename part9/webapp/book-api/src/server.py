import sys
from flask import Flask
from flask import jsonify
from pymongo import MongoClient
from bson.json_util import dumps

# App 
app = Flask(__name__)

# Database Settings
CLIENT = MongoClient('mongodb://book-database:27017/')
DB = CLIENT.book_database

# Database helper functions
def jsonify_mongo(pymongo_object):
    """ Converts from non-serializable Pymongo object to a Python object """
    return app.response_class(
        response=dumps(pymongo_object),
        status=200,
        mimetype='application/json'
    )

def initialize_db():
    """ Pre-populates the database with a book """
    if DB.books.count() == 0:
        DB.books.insert_one(
            {
                "title": "Enders Game",
                "author": "Orson Scott Card"
            }
        ) 
        print("Initializing DB", file=sys.stdout)
    else:
        print("DB Initialized", file=sys.stdout)

    sys.stdout.flush()     # Helps to refresh the console

# Routes
@app.route('/books', methods=["GET"])
def get_books():
    Books = DB.books.find()
    return jsonify_mongo(Books)


if __name__ == '__main__':
    initialize_db()
    app.run(debug=True, host='0.0.0.0') 