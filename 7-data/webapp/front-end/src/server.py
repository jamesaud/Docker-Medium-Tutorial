import requests, os
from flask import Flask, render_template

BOOK_API_SERVER = os.environ['BOOK_API_SERVER']
app = Flask(__name__)

@app.route('/')
def show_books():
    Books = requests.get(BOOK_API_SERVER + "/books").json()
    return render_template('show_books.html', books=Books)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')