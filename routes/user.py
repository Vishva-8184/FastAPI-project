from fastapi import  APIRouter, HTTPException
from bson import ObjectId
from models.user import DetailsOfBook
from config.db import conn
from schemas.user import serializeDict, serializeList

book = APIRouter()

# To add a new book
@book.post('/books')
async def add_new_book(book:DetailsOfBook):
    existing_book = conn.Book_library.books.find_one({"title": book.title})
    if existing_book:
        raise HTTPException(status_code=400, detail="Book with the same title already exists.")
    
    conn.Book_library.books.insert_one(dict(book))
    return serializeList(conn.Book_library.books.find())
    
# To list all book
@book.get('/books')
async def find_all_book():
      books = list(conn.Book_library.books.find())
      if not books:
        raise HTTPException(status_code=404, detail="Books not found.")
      return serializeList(books)
    # return serializeList(conn.Book_library.books.find())
 
# To get a single book by ID
@book.get('/books/{id}')
async def find_one_book(id):
 try:   
    return serializeDict(conn.Book_library.books.find_one({"_id":ObjectId(id)}))
 except Exception as e:
        raise HTTPException(status_code=404, detail=f"Iitem not found")
 
# To update a book by ID
@book.put('/books/{id}')
async def update_book(id,book:DetailsOfBook):
 try:      
    conn.Book_library.books.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(book)
    })
    return serializeDict(conn.Book_library.books.find_one({"_id":ObjectId(id)}))
 except Exception as e:
        raise HTTPException(status_code=404, detail=f"Iitem not found")

# To delete a book by ID
@book.delete('/books/{id}')
async def delete_book(id,book:DetailsOfBook):
 try:   
    return serializeDict(conn.Book_library.books.find_one_and_delete({"_id":ObjectId(id)}))
 except Exception as e:
        raise HTTPException(status_code=404, detail=f"Iitem not found")
