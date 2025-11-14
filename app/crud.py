from .database import db
from .models import BookingCreate, BookingUpdate
from bson import ObjectId
import datetime

async def create_booking(booking: BookingCreate):
    data = booking.dict()
    data["date"] = datetime.datetime.utcnow()
    result = await db["bookings"].insert_one(data)
    data["id"] = str(result.inserted_id)
    return data

async def get_booking(booking_id: str):
    booking = await db["bookings"].find_one({"_id": ObjectId(booking_id)})
    if booking:
        booking["id"] = str(booking["_id"])
    return booking

async def get_bookings():
    bookings = []
    cursor = db["bookings"].find()
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        bookings.append(doc)
    return bookings

async def update_booking(booking_id: str, booking: BookingUpdate):
    result = await db["bookings"].update_one(
        {"_id": ObjectId(booking_id)},
        {"$set": booking.dict()}
    )
    return await get_booking(booking_id)

async def delete_booking(booking_id: str):
    booking = await get_booking(booking_id)
    await db["bookings"].delete_one({"_id": ObjectId(booking_id)})
    return booking
