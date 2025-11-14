# Edupass Booking
FastAPI microservice (Bookings + Auth). Two MongoDB connections: bookings and
users.
## Local dev (docker-compose)
1. Copy `.env` locally with keys:
- MONGO_URI_BOOKING
- MONGO_URI_USERS
- DB_NAME_BOOKING
- DB_NAME_USERS
- JWT_SECRET
2. Run:
3. Swagger: http://127.0.0.1:8000/docs
## Deploy to Render
- Push repo to GitHub (remove .env)
- Create Web Service (Docker)
- In Render panel set environment variables
- Deploy
## Health endpoints
- `/health`
- `/health/db` (pings both DBs)