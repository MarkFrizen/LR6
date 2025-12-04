from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import List
app = FastAPI()
# Простой HTML для Pydantic-схем
file = open('templates/users.html', 'r')
html = file.read()
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
users : List[User] = []
@app.get("/")
async def get():
    return HTMLResponse(html)
# Создание пользователя по данным из html-формы
@app.post("/")
async def create_user(
        name: str = Form(...),
        email: str = Form(...),
        age: int = Form(None)
):
    user = User(
        id=len(users),
        name=name,
        email=email,
        age=age)
    users.append(user)
    return HTMLResponse(html)
# Проверка пользователя
@app.get("/testuser", response_model=User)
def test_user():
    user = User(
        id=1,
        name="Mark Frizen",
        email="mf@gmail.com",
        age=20
    )
    return user
# Проверка списка созданных пользователей
@app.get("/checkusers", response_model=List[User])
def check_user():
    return users

