from typing import Optional
from pydantic import BaseModel
from schemas.user import User

class Plan(BaseModel):
    id: str
    user: User
    desc: Optional[str]