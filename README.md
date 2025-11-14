# EduPass Booking Microservice

This is a **FastAPI microservice** for managing EduPass bookings. It supports basic CRUD operations using **MongoDB** as a database.

> ⚠️ **Warning:** Currently, this microservice is **broken**.  
> The code was modified and some parts do not work. Instructions below are for reference only.

---

## Features

- Create, read, update, and delete bookings  
- Swagger UI for API documentation (`/docs`)  
- Uses MongoDB via Motor (async Python client)

---

## Requirements

- Python 3.12+  
- MongoDB (Atlas or local instance)  
- Docker (optional)

---

## Setup Instructions (Local)

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/EduPass-Booking.git
cd EduPass-Booking]
```
2. **Create a .env file and add your MongoDB URL:**
```bash
MONGO_URL=mongodb+srv://<user>:<password>@cluster0.mongodb.net/edupass_db?retryWrites=true&w=majority
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. Run the service:
```bash
uvicorn app.main:app --reload
```
5. Open Swagger UI in your browser:

```bash
http://127.0.0.1:8000/docs
```


## Future Improvements
- Fix broken MongoDB CRUD operations
- Add proper error handling and validation
- Implement authentication for secure API access
