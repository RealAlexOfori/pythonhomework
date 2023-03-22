from flask import Flask, render_template
from repositories import book_repository
from repositories import author_repository
from models.books import Book


from flask import Blueprint

tasks_blueprint = Blueprint("books", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@tasks_blueprint.route("/books")
def books():
    books = book_repository.select_all() # NEW
    return render_template("books/index.html", all_books = books)