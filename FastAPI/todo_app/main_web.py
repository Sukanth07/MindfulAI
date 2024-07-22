from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src import models, schemas, crud
from src.settings import SessionLocal, engine

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        "login.html", {"request": request}
    )

@app.post("/", response_class=HTMLResponse)
async def login_validate(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db=db, email=email)
    if user is None:
        return templates.TemplateResponse("login.html", {"request": request, 
                                                         "error": "Email doesn't exist"})
    if not crud.verify_pwd(password, user.password):
        return templates.TemplateResponse("login.html", {"request": request, 
                                                         "error": "Invalid Password"})
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="user_id", value=str(user.id))
    return response

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        "register.html", {"request": request}
    )

@app.post("/register", response_class=HTMLResponse)
async def register_validate(request: Request, uname: str = Form(...), email: str = Form(...), pass1: str = Form(...), pass2: str = Form(...), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db=db, email=email)
    if user:
        return templates.TemplateResponse("register.html", {"request": request,
                                                            "error": "Email already registerd"})
    if pass1 != pass2:
        return templates.TemplateResponse("register.html", {"request": request,
                                                            "error": "Passwords doesn't match"})
    user_create = schemas.UserCreate(name=uname, email=email, password=pass1)
    crud.create_user(db=db, user=user_create)
    return RedirectResponse(url="/", status_code=303)

@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    response = RedirectResponse(url="/")
    response.delete_cookie(key="user_id")
    return response

@app.get("/dashboard")
async def dashboard(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if user_id:
        user_id = int(user_id)
        user = crud.get_user(db=db, user_id=user_id)
        user_todos = crud.get_user_todos(db=db, user_id=user_id)
        print(user_todos)
        return templates.TemplateResponse("dashboard.html", {"request": request,
                                                        "username": user.name,
                                                        "user_todos": user_todos})
    return {"message": "No user_id cookie found"}

@app.post("/dashboard")
async def create_user_todo(request: Request, title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if user_id:
        user_id = int(user_id)
        todo_create = schemas.TodoCreate(title=title, description=description)
        crud.create_user_todo(db=db, todo=todo_create, user_id=user_id)
        return RedirectResponse(url="/dashboard", status_code=303)
    return {"message": "No user_id cookie found"}

@app.post("/delete-todo")
async def delete_user_todo(request: Request, todo_id: int = Form(...), db: Session = Depends(get_db)):
    crud.delete_todo(db=db, todo_id=todo_id)
    return RedirectResponse(url="/dashboard", status_code=303)