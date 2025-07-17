from fastapi import APIRouter
from app.models import Book, NewBook, Genre, NewGenre
from app import services

# Create a router object to group and manage API routes
router = APIRouter()

# ✅ GET endpoint to return all books in the library
@router.get("/books", response_model=list[Book])
def get_all_books():
    df = services.load_books()  # Load book data from CSV
    return df.to_dict(orient="records")  # Convert to list of dictionaries for API response

# ✅ GET endpoint to return only fictional books
@router.get("/books/fiction", response_model=list[Book])
def get_fictional_books():
    df = services.classify_books()  # Load and classify books by genre type
    fiction = df[df["type"] == "Fiction"]  # Filter only fiction books
    return fiction.to_dict(orient="records")  # Return result as list of dictionaries

# ✅ GET endpoint to return only non-fictional books
@router.get("/books/non-fiction", response_model=list[Book])
def get_nonfiction_books():
    df = services.classify_books()  # Load and classify books
    non_fiction = df[df["type"] == "Non-Fiction"]  # Filter only non-fiction books
    return non_fiction.to_dict(orient="records")  # Return result as list of dictionaries

# ✅ POST endpoint to add a new book to the library
@router.post("/books", response_model=Book)
def post_new_book(book: NewBook):
    return services.add_book(book.dict())  # Convert input to dict and add book using service logic

# ✅ POST endpoint to add a new genre (fiction/non-fiction)
@router.post("/genres", response_model=Genre)
def post_new_genre(genre: NewGenre):
    return services.add_genre(genre.dict())  # Convert input to dict and add genre using service logic
