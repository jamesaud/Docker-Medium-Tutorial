from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_books():
    Books = [{"title": "Eragon", "author": "Christopher Paolini"}] 
    return render_template('show_books.html', books=Books)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')