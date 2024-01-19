# FastAPI Book Library API

This is a FastAPI-based API for managing a book library, using MongoDB as the database.

## API Endpoints

- **POST /books**: Add a new book.
- **GET /books**: List all books.
- **GET /books/{id}**: Get details of a single book by ID.
- **PUT /books/{id}**: Update a book by ID.
- **DELETE /books/{id}**: Delete a book by ID.

## Data Model

- **Title**: Title of the book.
- **Author**: Author of the book.
- **Published Year**: Year the book was published.
- **Genre**: Genre of the book.
- **Is Available**: Availability status of the book.

## Project Structure

├── config
│ └── db.py
├── models
│ └── user.py
├── routes
│ └── user.py
├── schemas
│ └── user.py
├── main.py
└── README.md


## Getting Started

### Prerequisites

- Python 3.12.1
- MongoDB installed and running on `localhost:27017`.Then, use the following command in the terminal:

uvicorn main:app --reload

### Installation

1. Clone the repository:

   git clone https://github.com/Vishva-8184/FastAPI-project/tree/Book_Library

2. FastAPI:

   pip install fastapi

3. Uvicorn:

   pip install "uvicorn[standard]"  

4. Motor:

   pip install motor

5. Pydantic:

   pip install pydantic
