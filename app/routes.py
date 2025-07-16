from fastapi import APIRouter
from app.models import Book, NewBook, Genre, NewGenre
from app import services

router = APIRouter()

@router.get("/books", response_model=list[Book])
def get_all_books():
    df = services.load_books()
    return df.to_dict(orient="records")

@router.get("/books/fiction", response_model=list[Book])
def get_fictional_books():
    df = services.classify_books()
    fiction = df[df["type"] == "Fiction"]
    return fiction.to_dict(orient="records")

@router.get("/books/non-fiction", response_model=list[Book])
def get_nonfiction_books():
    df = services.classify_books()
    non_fiction = df[df["type"] == "Non-Fiction"]
    return non_fiction.to_dict(orient="records")

@router.post("/books", response_model=Book)
def post_new_book(book: NewBook):
    return services.add_book(book.dict())

@router.post("/genres", response_model=Genre)
def post_new_genre(genre: NewGenre):
    return services.add_genre(genre.dict())