from pydantic import BaseModel  # BaseModel from Pydantic is used to define data validation and serialization
from typing import Optional  # Optional type hint in case you need optional fields later

# Model to represent a complete Book entry
class Book(BaseModel):
    id: int  # Unique identifier for the book
    title: str  # Title of the book
    author: str  # Author's name
    genre: str  # Genre of the book (e.g., Fiction, Non-Fiction)
    year: int  # Year the book was published

# Model used when adding a new book (ID is auto-generated)
class NewBook(BaseModel):
    title: str  # Title of the new book
    author: str  # Author's name
    genre: str  # Genre the new book belongs to
    year: int  # Year of publication

# Model to represent a complete Genre entry
class Genre(BaseModel):
    id: int  # Unique identifier for the genre
    name: str  # Name of the genre (e.g., Science Fiction)
    type: str  # Type of genre - Fiction or Non-Fiction

# Model used when adding a new genre (ID is auto-generated)
class NewGenre(BaseModel):
    name: str  # Name of the new genre
    type: str  # Type of genre - Fiction or Non-Fiction
