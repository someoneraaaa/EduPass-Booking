from typing import List
from app.domain.entities import Booking

class BookingUseCase:
    def __init__(self):
        # Простая "база" в памяти
        self.bookings = []

    def create_booking(self, booking: Booking) -> Booking:
        self.bookings.append(booking)
        return booking

    def get_all_bookings(self) -> List[Booking]:
        return self.bookings

    def get_booking_by_id(self, booking_id: str) -> Booking | None:
        for b in self.bookings:
            if b.id == booking_id:
                return b
        return None

    def cancel_booking(self, booking_id: str) -> bool:
        for b in self.bookings:
            if b.id == booking_id:
                self.bookings.remove(b)
                return True
        return False