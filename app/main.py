from fastapi import FastAPI, HTTPException
from app.models import User
from app.database import users_db
from app.config import settings

app = FastAPI(title=settings.app_name)


@app.get("/")
def home():
    return {"message": "API is running"}


# CREATE USER
@app.post("/users", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user


# GET ALL USERS
@app.get("/users", response_model=list[User])
def get_users():
    return users_db


# GET SINGLE USER
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

