from fastapi import  APIRouter
from bson import ObjectId
from models.user import DetailsOfBook
from config.db import conn
from schemas.user import serializeDict, serializeList

book = APIRouter()

# To add a new book
@book.post('/books')
async def add_new_book(book:DetailsOfBook):
    conn.Book_library.books.insert_one(dict(book))
    return serializeList(conn.Book_library.books.find())

# To list all book
@book.get('/books')
async def find_all_book():
    # print(conn.Book_library.books.find())
    # print(booksEntity(conn.Book_library.books.find()))
    return serializeList(conn.Book_library.books.find())

# To get a single book by ID
@book.get('/books/{id}')
async def find_one_book(id):
    return serializeDict(conn.Book_library.books.find_one({"_id":ObjectId(id)}))

# To update a book by ID
@book.put('/books/{id}')
async def update_book(id,book:DetailsOfBook):
    conn.Book_library.books.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(book)
    })
    return serializeDict(conn.Book_library.books.find_one({"_id":ObjectId(id)}))

# To delete a book by ID
@book.delete('/books/{id}')
async def delete_book(id,book:DetailsOfBook):
    return serializeDict(conn.Book_library.books.find_one_and_delete({"_id":ObjectId(id)}))
