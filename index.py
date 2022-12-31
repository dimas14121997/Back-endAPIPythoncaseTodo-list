from fastapi import FastAPI
from routes.index import todolistz
app = FastAPI()

app.include_router(todolistz)