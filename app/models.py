from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookingBase(BaseModel):
    student_id: int
    course_id: int
    status: str = "pending"

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BookingBase):
    pass

class Booking(BookingBase):
    id: str
    date: Optional[datetime] = None

    class Config:
        orm_mode = True
