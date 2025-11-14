from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Загружаем строку подключения из .env
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "edupass_db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def get_db_status():
    try:
        client.admin.command('ping')
        return {"status": "connected"}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)}
