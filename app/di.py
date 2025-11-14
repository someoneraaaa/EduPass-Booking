from app.infrastructure.db import db
from app.adapters.repo.mongo_booking_repo import MongoBookingRepository
from app.usecase.booking import BookingUseCase

def get_booking_usecase() -> BookingUseCase:
    repo = MongoBookingRepository(db)
    return BookingUseCase(repo)