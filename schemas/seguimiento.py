from typing import Optional
from pydantic import BaseModel

from plan import Plan

class Seguimiento(BaseModel):
    id: str
    plan: Plan
    bio: Optional[str]