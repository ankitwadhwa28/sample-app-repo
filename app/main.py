from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Sample App", version="1.0.0")

_users = [
    {"id": 1, "name": "Alice", "email": "alice4@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]


class User(BaseModel):
    id: int
    name: str
    email: str


@app.get("/")
def root():
    return {"message": "Hello from Sample App!", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/users", response_model=List[User])
def list_users():
    return _users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in _users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
