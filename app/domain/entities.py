from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Booking(BaseModel):
    id: Optional[str] = None
    user_id: str
    course_id: str
    lesson_time: datetime
    status: str = "pending"
    notes: Optional[str] = None