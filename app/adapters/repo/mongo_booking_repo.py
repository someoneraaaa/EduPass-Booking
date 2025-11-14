from typing import List, Optional
from bson import ObjectId
from app.domain.entities import Booking
from app.domain.repositories import IBookingRepository

class MongoBookingRepository(IBookingRepository):
    def __init__(self, db):
        self.collection = db["bookings"]

    async def create(self, booking: Booking) -> Booking:
        data = booking.dict(by_alias=True, exclude={"id"})
        result = await self.collection.insert_one(data)
        booking.id = str(result.inserted_id)
        return booking

    async def get_all(self) -> List[Booking]:
        bookings = await self.collection.find().to_list(100)
        return [Booking(**b) for b in bookings]

    async def get_by_id(self, booking_id: str) -> Optional[Booking]:
        booking = await self.collection.find_one({"_id": ObjectId(booking_id)})
        return Booking(**booking) if booking else None

    async def delete(self, booking_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(booking_id)})
        return result.deleted_count > 0