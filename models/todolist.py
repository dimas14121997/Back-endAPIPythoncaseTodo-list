from sqlalchemy import MetaData,Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

todolist = Table(
    'todolist',meta,
    Column('id',Integer,primary_key =True),
    Column('title',String(30)),
    Column('description',String(255)),
)