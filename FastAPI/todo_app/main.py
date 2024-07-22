from fastapi import FastAPI, HTTPException, Depends
from src import crud, models, schemas
from sqlalchemy.orm import Session
from src.settings import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#----------------------- Create DB Session --------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#---------------------------------------------------------------------------------
#-------------------------- Home -------------------------------------------------
@app.get("/")
async def home():
    return {'detail': 'This is home page'}
#---------------------------------------------------------------------------------
#------------------------ Create New User ---------------------------------------- 
@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return crud.create_user(db=db, user=user)
#---------------------------------------------------------------------------------
#------------------------- Get All Users -----------------------------------------
@app.get("/users/", response_model=List[schemas.User])
async def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    if db_users:
        return db_users
    return []
#---------------------------------------------------------------------------------
#--------------------------- Get User By ID -------------------------------------
@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user:
        return db_user
    raise HTTPException(status_code=400, detail="User not found")
#---------------------------------------------------------------------------------
#---------------------------- Get All Todos --------------------------------------
@app.get("/todos/", response_model=List[schemas.Todo])
async def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_todos = crud.get_todos(db=db, skip=skip, limit=limit)
    if db_todos:
        return db_todos
    return []
#----------------------------------------------------------------------------------
#-------------------------- Create New Todo For User ------------------------------
@app.post("/todos/", response_model=schemas.Todo)
async def create_user_todo(todo: schemas.TodoCreate, user_id: int, db: Session = Depends(get_db)):
    db_todo = crud.create_user_todo(db=db, todo=todo, user_id=user_id)
    return db_todo
#----------------------------------------------------------------------------------
#-------------------------- Get All Todos of a User -------------------------------
@app.get("/todos/{user_id}", response_model=List[schemas.Todo])
async def read_user_todos(user_id: int, db: Session = Depends(get_db)):
    db_todos = crud.get_user_todos(db=db, user_id=user_id)
    if db_todos:
        return db_todos
    return []
#-----------------------------------------------------------------------------------
#-------------------------------- Update User --------------------------------------
@app.put("/users/}", response_model=schemas.User)
async def update_user_details(user: schemas.UserBase, user_id: int, db: Session = Depends(get_db)):
    db_user = crud.update_user_details(db=db, user=user, user_id=user_id)
    return db_user
    
#-----------------------------------------------------------------------------------
#-------------------------------- Update Todo --------------------------------------
@app.put("/todos/", response_model=schemas.TodoUpdate)
async def update_todo_details(todo: schemas.TodoUpdate, todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.update_todo_details(db=db, todo=todo, todo_id=todo_id)
    return db_todo
#-----------------------------------------------------------------------------------
#-------------------------------- Delete Todo -------------------------------------- 
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo(db=db, todo_id=todo_id)