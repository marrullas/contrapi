from fastapi import FastAPI
from routes.user import user


app = FastAPI()

app.include_router(user)

@app.get('/')
async def root():
    return{'message': 'Hola Magola'}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}