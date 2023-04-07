from jwt import encode
from datetime import datetime, timedelta
from os import getenv

def expire_date(days:int =2):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def create_token(data: dict):
    token: str = encode(payload={**data, "exp": expire_date()}, key=getenv("SECRET"), algorithm="HS256")
    return token