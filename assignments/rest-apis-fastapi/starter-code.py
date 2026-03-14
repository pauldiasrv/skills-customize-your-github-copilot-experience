from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- Pydantic Model ---
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# --- In-memory "database" ---
books: list[Book] = []

# --- Task 1: Root endpoint ---
@app.get("/")
def read_root():
    # TODO: Return a JSON welcome message
    pass

# --- Task 2: CRUD Endpoints ---

@app.get("/books")
def get_books():
    # TODO: Return all books
    pass

@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the book with the given ID
    # Raise HTTPException with status_code=404 if not found
    pass

@app.post("/books")
def create_book(book: Book):
    # TODO: Add the new book to the list and return it
    pass

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    # TODO: Find the book by ID, update its fields, and return the updated book
    # Raise HTTPException with status_code=404 if not found
    pass

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the book with the given ID and return a confirmation message
    # Raise HTTPException with status_code=404 if not found
    pass
