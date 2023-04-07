from fastapi import APIRouter, Path, status, HTTPException
from fastapi.responses import JSONResponse

from typing import List

from schemas.user import User

user = APIRouter(
    tags=["user"],
    
)

users = []

@user.get("/users", response_model=List[User], status_code=status.HTTP_200_OK)
async def getUsers()-> List[User]:
    return users

@user.post("/users",status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    users.append(user)
    return {"Message": "Usuario agregado"}
#raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")

@user.get("users/{id}", response_model=User)
async def get_user(id: int = Path(..., description="Id del usuario a retornar"))->User:
    return user[id]

@user.put("users/{id}", status_code=status.HTTP_200_OK)
async def update_user(id:int, user: User):
    return user[id]

@user.delete("users/{id}", response_model=dict, status_code=status.HTTP_200_OK)
async def delete_user(id:int):
    return JSONResponse({"message": "usuario eliminado"})

@user.post("/login", tags=['auth'])
async def login(user: User):
    return user