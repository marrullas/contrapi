from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    email:str
    role:int

class UserCreate(UserBase):
    #password:str
    ... #no entiendo muy bien que hacen los 3 puntos

class User(UserBase):
    is_active: bool
    bio: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True