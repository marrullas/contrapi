from fastapi import APIRouter, Path
from schemas.user import User

user = APIRouter(
    tags=["user"],
    
)

users = []

@user.get("/users", response_model=User)
async def getUsers():
    return users

@user.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"Message": "Usuario agregado"}

@user.get("users/{id}")
async def get_user(id: int = Path(..., description="Id del usuario a retornar")):
    return user[id]