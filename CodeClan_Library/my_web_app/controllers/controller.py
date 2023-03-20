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

@app.route("/books/<index>")
def books_show(index):
    book = books[int(index)]
    return render_template("books/show.html", book=book, index=index)

@app.route('/books', methods=['POST'])
def add_book():
  bookTitle = request.form['title']
  newBook = Book(title=bookTitle, author = "", genre = "")
  books.append(newBook)

  return redirect('/books')

@app.route('/books/delete', methods=['POST'])
def remove_book():
  # value_from_form = request.form["book_to_remove"]
  # print(f"book to remove is {value_from_form}")
  book_to_be_removed = [book for book in books if book.title == request.form["book_to_remove"]]
  books.remove(book_to_be_removed[0])

  return redirect('/books')