from motor.motor_asyncio import AsyncIOMotorClient
from app.settings import settings

client = AsyncIOMotorClient(settings.MONGO_URL)
database = client[settings.MONGO_DB]
bookings_collection = database.get_collection("bookings")