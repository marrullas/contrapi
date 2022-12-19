from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]