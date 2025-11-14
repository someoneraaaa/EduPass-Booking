from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from app.adapters.http import bookings_router
import os

app = FastAPI(title="EduPass Booking Service", version="1.0.0")

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MongoDB ---
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/booking_db")
client = MongoClient(MONGO_URL)
db = client.get_database("booking_db")

# Делаем базу доступной во всём приложении
app.state.db = db

# --- Routers ---
app.include_router(bookings_router.router, prefix="/bookings", tags=["Bookings"])

@app.get("/")
def root():
    return {"message": "EduPass Booking microservice is running 🚀"}

from app.adapters.http import auth_router

app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
