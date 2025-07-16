from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Library Management API",
    description="A simple REST API to manage library data (books, genres)",
    version="1.0.0"
)

# Register API routes
app.include_router(router)