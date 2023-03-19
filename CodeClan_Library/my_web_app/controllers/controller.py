from flask import render_template, request, redirect
from app import app
from models.book import Book
from models.books_list import books, add_book

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def show_all_books():
    return render_template('books/index.html', book_list=books)

# @app.route("/books/<index>")
# def books_show(index):
#     book = books[int(index)]
#     return render_template("books/show.html", book=book, index=index)

@app.route("/books", methods=["POST"])
def books_create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre, False)
    add_book(new_book)
    books.append(new_book)
    return redirect("/books")