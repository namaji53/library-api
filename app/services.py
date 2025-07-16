import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

def load_books():
    return pd.read_csv(DATA_DIR / "books.csv")

def load_genres():
    return pd.read_csv(DATA_DIR / "genres.csv")

def classify_books():
    books = load_books()
    genres = load_genres()

    genre_type_map = dict(zip(genres["name"], genres["type"]))
    books["type"] = books["genre"].map(genre_type_map)
    return books

def add_book(new_book: dict):
    books = load_books()
    new_id = books["id"].max() + 1
    new_book["id"] = new_id
    books = pd.concat([books, pd.DataFrame([new_book])], ignore_index=True)
    books.to_csv(DATA_DIR / "books.csv", index=False)
    return new_book

def add_genre(new_genre: dict):
    genres = load_genres()
    new_id = genres["id"].max() + 1
    new_genre["id"] = new_id
    genres = pd.concat([genres, pd.DataFrame([new_genre])], ignore_index=True)
    genres.to_csv(DATA_DIR / "genres.csv", index=False)
    return new_genre