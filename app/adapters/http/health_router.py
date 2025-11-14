from fastapi import APIRouter, Request
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()

class Booking(BaseModel):
    user_id: str
    course_name: str
    booking_time: datetime = datetime.now()
    status: str = "pending"

@router.get("/bookings/")
def list_bookings(request: Request):
    db = request.app.state.db
    bookings = list(db.bookings.find({}, {"_id": 0}))
    return {"bookings": bookings}

@router.post("/bookings/")
def create_booking(request: Request, booking: Booking):
    db = request.app.state.db
    db.bookings.insert_one(booking.dict())
    return {"message": "Booking created", "booking": booking}