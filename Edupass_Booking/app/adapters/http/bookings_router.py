from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.core.database import db
from app.core.auth import get_current_user  # ✅ добавили
from bson import ObjectId

router = APIRouter()

class Booking(BaseModel):
    user_id: str
    course_id: str
    date: str


# CREATE (только для авторизованных)
@router.post("/")
async def create_booking(booking: Booking, user: str = Depends(get_current_user)):
    result = await db.bookings.insert_one(booking.dict())
    return {"id": str(result.inserted_id)}


# READ ALL
@router.get("/")
async def get_all_bookings(user: str = Depends(get_current_user)):
    bookings = await db.bookings.find().to_list(100)
    for b in bookings:
        b["_id"] = str(b["_id"])
    return bookings


# READ ONE
@router.get("/{booking_id}")
async def get_booking(booking_id: str, user: str = Depends(get_current_user)):
    booking = await db.bookings.find_one({"_id": ObjectId(booking_id)})
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    booking["_id"] = str(booking["_id"])
    return booking


# UPDATE
@router.put("/{booking_id}")
async def update_booking(booking_id: str, booking: Booking, user: str = Depends(get_current_user)):
    result = await db.bookings.update_one({"_id": ObjectId(booking_id)}, {"$set": booking.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking updated"}


# DELETE
@router.delete("/{booking_id}")
async def delete_booking(booking_id: str, user: str = Depends(get_current_user)):
    result = await db.bookings.delete_one({"_id": ObjectId(booking_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted"}
