from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


# Схема данных для бронирования
class Booking(BaseModel):
    id: Optional[str] = None
    user_id: str
    meal_name: str
    booking_time: datetime
    pickup_time: datetime
    status: str = "pending"


# Простейший use case (логика бронирования)
class BookingUseCase:
    def __init__(self):
        # Временно имитация базы данных
        self._bookings: List[Booking] = []

    def create_booking(self, booking: Booking) -> Booking:
        booking.id = str(len(self._bookings) + 1)
        self._bookings.append(booking)
        return booking

    def list_bookings(self) -> List[Booking]:
        return self._bookings

    def get_booking(self, booking_id: str) -> Optional[Booking]:
        for b in self._bookings:
            if b.id == booking_id:
                return b
        return None