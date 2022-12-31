from pydantic import BaseModel

class Todolist(BaseModel):
    id:int
    title:str
    description:str