from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.auth import create_access_token, get_password_hash, verify_password
from app.core.database import db

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register(user: User):
    existing = await db.users.find_one({"username": user.username})
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pw = get_password_hash(user.password)
    await db.users.insert_one({"username": user.username, "password": hashed_pw})
    return {"message": "User registered"}

@router.post("/login")
async def login(user: User):
    db_user = await db.users.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
