from db.run_sql import run_sql

from models.books import Book
from models.authors import Author
import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title,author, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title,book.author, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        user = author_repository.select(row['author_id'])
        book = Book(row['title'], row['author'], row['id'] )
        books.append(book)
    return books