import requests 
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for

BOOK_API_SERVER = os.environ['BOOK_API_SERVER']
app = Flask(__name__)

@app.route('/')
def show_books():
    Books = requests.get(BOOK_API_SERVER + "/books").json()
    return render_template('show_books.html', books=Books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return render_template('add_book.html')
    else:
        json = {
            'title': request.form['title'],
            'author': request.form['author']
        }
        response = requests.post(BOOK_API_SERVER + "/create_book", json=json)
        if response.status_code == 200:
            return redirect(url_for('show_books'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')