from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities import Booking

class BookingRepository(ABC):
    @abstractmethod
    async def create(self, booking: Booking) -> Booking:
        pass

    @abstractmethod
    async def get_all(self) -> List[Booking]:
        pass

    @abstractmethod
    async def get_by_id(self, booking_id: str) -> Optional[Booking]:
        pass