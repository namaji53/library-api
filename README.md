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

<img width="1855" height="718" alt="Screenshot 2025-07-17 205920" src="https://github.com/user-attachments/assets/b5786f4d-527d-4dc0-8c3e-cef9c5424a0e" />

<img width="599" height="800" alt="Screenshot 2025-07-17 122949" src="https://github.com/user-attachments/assets/2e178ebf-9b0b-46c6-9205-a4e29cbd8fd6" />

<img width="601" height="553" alt="Screenshot 2025-07-17 122935" src="https://github.com/user-attachments/assets/ed1b3c18-cd0a-4d4b-8f29-a8474b1af05f" />

<img width="601" height="593" alt="Screenshot 2025-07-17 122922" src="https://github.com/user-attachments/assets/a8199b0b-880d-4550-8714-4e985c87a836" />

<img width="644" height="718" alt="Screenshot 2025-07-17 122906" src="https://github.com/user-attachments/assets/6c1c6fd4-aaaf-4e3d-b59c-5a60c499b076" />

<img width="619" height="826" alt="Screenshot 2025-07-17 122853" src="https://github.com/user-attachments/assets/5891742f-f31d-46ac-a5eb-df0b33acf3ea" />

