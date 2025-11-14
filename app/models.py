from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
import datetime

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, index=True)
    course_id = Column(Integer, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="pending")
