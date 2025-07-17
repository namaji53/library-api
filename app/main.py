from fastapi import FastAPI  # Import FastAPI framework to build the API
from app.routes import router  # Import the router which holds the endpoint definitions

# Create an instance of FastAPI with metadata like title, description, and version
app = FastAPI(
    title="Library Management API",  # Title shown in automatic API docs
    description="A simple REST API to manage library data (books, genres)",  # Short description
    version="1.0.0"  # Version number of the API
)

# Register API routes from the router to the app instance
app.include_router(router)
