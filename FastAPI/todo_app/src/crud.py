from sqlalchemy.orm import Session
from src import models, schemas
from passlib.context import CryptContext
from fastapi import HTTPException
#pip install passlib[argon2]  argon2 is the hashing algorithm name
'''
We should store the hashed/encrypted password in database.
So passlib library is used to convert the text password into a hashed/encrypted password
and we store the encrypted password in database.
'''

# Initialize CryptContext with bcrypt algorithm
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_pwd(password: str) -> str:
    return pwd_context.hash(password)

def verify_pwd(password: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(password, hashed_pwd)

#--------------------------------------------------------------------------------

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_pwd(user.password)
    # db_user = models.User(dict(**user))
    db_user = models.User(
        name = user.name,
        email = user.email,
        password = hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_user_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_todo = models.Todo(
        title = todo.title,
        description = todo.description,
        owner_id = user_id
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_user_todos(db: Session, user_id: int):
    return db.query(models.Todo).filter(models.Todo.owner_id == user_id).all()

def update_user_details(db: Session, user: schemas.UserBase, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

def update_todo_details(db: Session, todo: schemas.TodoUpdate, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=400, detail="Todo not found")
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.is_done = todo.is_done
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=400, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"detail": "Todo deleted"}