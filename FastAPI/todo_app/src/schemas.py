from pydantic import BaseModel
from typing import List

class TodoBase(BaseModel):
    title : str
    description : str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    is_done : bool

class Todo(TodoUpdate):
    id : int
    owner_id : int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    name : str
    email : str

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id : int
    todos : List[Todo] = []
    class Config:
        orm_mode = True