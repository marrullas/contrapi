from fastapi import FastAPI
from dotenv import load_dotenv
from routes.user import user
from routes.plan import plan


app = FastAPI()

load_dotenv()

app.title = "Api Contraloría"

app.include_router(user)
app.include_router(plan)

@app.get('/')
async def root():
    return{'message': 'Hola Magola'}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
