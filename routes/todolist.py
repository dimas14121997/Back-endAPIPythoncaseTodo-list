from fastapi import APIRouter
from config.db import conn
from models.index import todolist
from schema.index import Todolist

todolistz = APIRouter()

@todolistz.get("/")
async def read_data():
    return conn.execute(todolist.select()).fetchall()

@todolistz.get("/{id}")
async def read_data_by_id(id:int):
    return conn.execute(todolist.select().where(todolist.id == id)).fetchall()

@todolistz.post("/")
async def add_data(todolists:Todolist):
    conn.execute(todolist.insert().values(
        title=todolists.title,
        description=todolists.description
    ))

    return conn.execute(todolist.select()).fetchall()


@todolistz.put("/{id}")
async def update_data(id:int,todolists:Todolist):
    conn.execute(todolist.update(
        title=todolists.title,
        description=todolists.description
    ).where(todolist.id == id))

    return conn.execute(todolist.select()).fetchall()

@todolistz.delete("/")
async def delete_data():
    conn.execute(todolist.delete().where(todolist.id == id)).fetchall()
    return conn.execute(todolist.select()).fetchall()