from fastapi import FastAPI, HTTPException
from . import crud, models

app = FastAPI(title="EduPass Booking Microservice (MongoDB)")

@app.post("/bookings/", response_model=models.Booking)
async def create_booking(booking: models.BookingCreate):
    return await crud.create_booking(booking)

@app.get("/bookings/{booking_id}", response_model=models.Booking)
async def read_booking(booking_id: str):
    booking = await crud.get_booking(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.get("/bookings/", response_model=list[models.Booking])
async def list_bookings():
    return await crud.get_bookings()

@app.put("/bookings/{booking_id}", response_model=models.Booking)
async def update_booking(booking_id: str, booking: models.BookingUpdate):
    updated = await crud.update_booking(booking_id, booking)
    if not updated:
        raise HTTPException(status_code=404, detail="Booking not found")
    return updated

@app.delete("/bookings/{booking_id}", response_model=models.Booking)
async def delete_booking(booking_id: str):
    deleted = await crud.delete_booking(booking_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Booking not found")
    return deleted
