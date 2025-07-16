from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int

class NewBook(BaseModel):
    title: str
    author: str
    genre: str
    year: int

class Genre(BaseModel):
    id: int
    name: str
    type: str  # Fiction or Non-Fiction

class NewGenre(BaseModel):
    name: str
    type: str