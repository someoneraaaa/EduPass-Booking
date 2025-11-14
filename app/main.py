from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI(title="EduPass Booking Microservice")

# создаем таблицы
models.Base.metadata.create_all(bind=database.engine)

@app.post("/bookings/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(database.get_db)):
    return crud.create_booking(db, booking)

@app.get("/bookings/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int, db: Session = Depends(database.get_db)):
    db_booking = crud.get_booking(db, booking_id)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@app.get("/bookings/", response_model=list[schemas.Booking])
def list_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_bookings(db, skip, limit)

@app.put("/bookings/{booking_id}", response_model=schemas.Booking)
def update_booking(booking_id: int, booking: schemas.BookingUpdate, db: Session = Depends(database.get_db)):
    db_booking = crud.update_booking(db, booking_id, booking)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@app.delete("/bookings/{booking_id}", response_model=schemas.Booking)
def delete_booking(booking_id: int, db: Session = Depends(database.get_db)):
    db_booking = crud.delete_booking(db, booking_id)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking
