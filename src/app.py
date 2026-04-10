from fastapi import FastAPI
from src.routes import api_router

app = FastAPI(
    title="Event API",
    description="API untuk manajemen event",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "API is running "}