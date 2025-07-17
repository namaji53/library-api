import pandas as pd  # Import pandas for working with CSV data
from pathlib import Path  # Used to manage file paths in a platform-independent way

# Define the path to the data directory relative to this script
DATA_DIR = Path(__file__).resolve().parent / "data"

# ✅ Function to load all books from books.csv as a DataFrame
def load_books():
    return pd.read_csv(DATA_DIR / "books.csv")

# ✅ Function to load all genres from genres.csv as a DataFrame
def load_genres():
    return pd.read_csv(DATA_DIR / "genres.csv")

# ✅ Function to classify each book as Fiction or Non-Fiction based on its genre
def classify_books():
    books = load_books()       # Load the book data
    genres = load_genres()     # Load the genre data

    # Create a dictionary that maps genre name to its type (e.g., {"Sci-Fi": "Fiction"})
    genre_type_map = dict(zip(genres["name"], genres["type"]))

    # Add a new column 'type' to the books DataFrame by mapping genre to type
    books["type"] = books["genre"].map(genre_type_map)
    return books  # Return the updated books with 'type' column

# ✅ Function to add a new book to the books.csv file
def add_book(new_book: dict):
    books = load_books()  # Load existing books
    new_id = books["id"].max() + 1  # Generate a new unique ID for the new book
    new_book["id"] = new_id  # Assign the new ID to the book
    # Append the new book to the books DataFrame
    books = pd.concat([books, pd.DataFrame([new_book])], ignore_index=True)
    # Save the updated DataFrame back to the CSV file
    books.to_csv(DATA_DIR / "books.csv", index=False)
    return new_book  # Return the newly added book (as a dictionary)

# ✅ Function to add a new genre to the genres.csv file
def add_genre(new_genre: dict):
    genres = load_genres()  # Load existing genres
    new_id = genres["id"].max() + 1  # Generate a new unique ID for the genre
    new_genre["id"] = new_id  # Assign the new ID
    # Append the new genre to the genres DataFrame
    genres = pd.concat([genres, pd.DataFrame([new_genre])], ignore_index=True)
    # Save the updated genres DataFrame back to the CSV file
    genres.to_csv(DATA_DIR / "genres.csv", index=False)
    return new_genre  # Return the newly added genre (as a dictionary)
