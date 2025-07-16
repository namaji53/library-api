# 📚 Library Management API

A simple RESTful API built using **FastAPI** and **Pydantic** to manage a digital library.  
This project loads book and genre data from CSV files, allows classification into fiction/non-fiction, and supports adding new books and genres via API.

---

## 🚀 Features

- ✅ Get a list of all books
- ✅ Classify books as **Fiction** or **Non-Fiction**
- ✅ Add a new book to the library
- ✅ Add a new genre and its type (Fiction/Non-Fiction)
- ✅ Uses **CSV files** as the data source
- ✅ Interactive API documentation with Swagger UI

---

## 🗂️ Project Structure
library_api/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── routes.py # API route definitions
│ ├── models.py # Pydantic data models
│ ├── services.py # Business logic and CSV operations
│ ├── utils.py # Helper functions (optional)
│ └── data/ # CSV files for books, genres, authors
│ ├── books.csv
│ ├── genres.csv
│ └── authors.csv
├── requirements.txt # Python dependencies
└── README.md





📘 API Documentation
Once the server is running, visit:

🔹 Swagger UI → http://127.0.0.1:8000/docs
