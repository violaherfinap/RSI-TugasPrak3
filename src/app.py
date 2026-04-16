from fastapi import FastAPI
from src.routes import api_router
from src.database.connection import create_db_and_tables

app = FastAPI(
    title="Event API",
    description="API untuk manajemen event",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "API is running"}