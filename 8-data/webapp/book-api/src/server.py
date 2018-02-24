import sys
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps

# App 
app = Flask(__name__)

# Database Settings
CLIENT = MongoClient('mongodb://book-database:27017/')
DB = CLIENT.book_database

# Database helper functions
def jsonify_mongo(pymongo_object, status=200):
    """ Converts from non-serializable Pymongo object to json """
    return app.response_class(
        response=dumps(pymongo_object),
        status=status,
        mimetype='application/json'
    )

def initialize_db():
    """ Pre-populates the database with a book """
    if DB.books.count() == 0:
        DB.books.insert_one({ "title": "Enders Game", "author": "Orson Scott Card"}) 
        print("Initializing DB")
    else: 
        print("DB Initialized")
    sys.stdout.flush()     # Helps to refresh the console


# Routes
@app.route('/books', methods=["GET"])
def get_books():
    Books = DB.books.find().sort("author")
    return jsonify_mongo(Books)


@app.route('/create_book', methods=["POST"])
def create_book():
    json = request.get_json()
    book = {
            "title" : json['title'],
            "author":  json['author']
            }
    DB.books.insert_one(book)
    return jsonify(message="success")


if __name__ == '__main__':
    initialize_db()
    app.run(debug=True, host='0.0.0.0') 