#start with the Hello World
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
# run---  uvicorn main:app --reload
# import uvicorn
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
# import uvicorn
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
# @app.get("/hello/{name}")
# async def hello(name):
#    return {"name": name}


# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/hello/{name}")
# async def hello(name:str,age:int):
#    return {"name": name, "age":age}


# import uvicorn
# from fastapi import FastAPI
# from typing import List
# from pydantic import BaseModel, Field
# app = FastAPI()
# class Student(BaseModel):
#    id: int
#    name :str = Field(None, title="name of student", max_length=10)
#    subjects: List[str] = []
# @app.post("/students/")
# async def student_data(s1: Student):
#    return s1


# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")
# @app.get("/hello/{name}", response_class=HTMLResponse)
# async def hello(request: Request, name:str):
#    return templates.TemplateResponse("hello.html", {"request": request, "name":name})


#   <script src="{{ url_for('static', path='hello.js') }}"></script>
#   <img src="{{ url_for('static', path='fa-logo.png') }}" alt="" width="300">
# from fastapi import Form
# import uvicorn
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI, Request
# from fastapi.staticfiles import StaticFiles
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")
# @app.get("/", response_class=HTMLResponse)
# async def hello(request: Request):
#    return templates.TemplateResponse("hello.html", {"request": request})

# @app.get("/form", response_class=HTMLResponse)
# async def hello(request: Request):
#    return templates.TemplateResponse("form.html", {"request": request})
# #FastAPI - Accessing Form Data
# from pydantic import BaseModel
# class User(BaseModel):
#    username:str
#    password:str
# @app.post("/submit/", response_model=User)
# async def submit(nm: str = Form(...), pwd: str = Form(...)):
#    return User(username=nm, password=pwd)

#FastAPI - Uploading Files
# from fastapi import FastAPI, File, UploadFile, Request
# import uvicorn
# import shutil
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# @app.get("/upload/", response_class=HTMLResponse)
# async def upload(request: Request):
#    return templates.TemplateResponse("uploadfile.html", {"request": request})

# from fastapi import FastAPI, File, UploadFile
# import shutil
# @app.post("/uploader/")
# async def create_upload_file(file: UploadFile = File(...)):
#    with open("destination.png", "wb") as buffer:
#       shutil.copyfileobj(file.file, buffer)
#    return {"filename": file.filename}

#FastAPI - Response Model
# import uvicorn
# from typing import List
# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# app = FastAPI()
# class student(BaseModel):
#    id: int
#    name :str = Field(None, title="name of student", max_length=10)
#    marks: List[int] = []
#    percent_marks: float
# class percent(BaseModel):
#    id:int
#    name :str = Field(None, title="name of student", max_length=10)
#    percent_marks: float
# @app.post("/marks", response_model=percent)
# async def get_percent(s1:student):
#    s1.percent_marks=sum(s1.marks)/2
#    return s1


#FastAPI - Nested Models
import uvicorn
from typing import Tuple, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
# class supplier(BaseModel):
#    supplierID:int
#    supplierName:str
# class product(BaseModel):
#    productID:int
#    prodname:str
#    price:int
#    supp:supplier
# class customer(BaseModel):
#    custID:int
#    custname:str
#    prod:Tuple[product]
# @app.post('/invoice')
# async def getInvoice(c1:customer):
#    return c1
from fastapi import Depends, FastAPI
#FastAPI - Dependencies
# async def dependency(id: str, name: str, age: int):
#    return {"id": id, "name": name, "age": age}

# @app.get("/user/")
# async def user(dep: dict = Depends(dependency)):
#    return dep
# class dependency:
#    def __init__(self, id: str, name: str, age: int):
#       self.id = id
#       self.name = name
#       self.age = age 
      
# @app.get("/user/")
# async def user(dep: dependency = Depends(dependency)):
#    return dep
# @app.get("/admin/")
# async def admin(dep: dependency = Depends(dependency)):
#    return dep 
# async def validate(dep: dependency = Depends(dependency)):
#    if dep.age > 18:
#       raise HTTPException(status_code=400, detail="You are not eligible")
# @app.get("/user/", dependencies=[Depends(validate)])
# async def user():
#    return {"message": "You are eligible"}

#FastAPI - CORS
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()
# origins = [
#    "http://192.168.211.:8000",
#    "http://localhost",
#    "http://localhost:8080",
# ]
# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
# )
# @app.get("/")
# async def main():
#    return {"message": "Hello World"}

#FastAPI - CRUD Operations
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# data = []
# class Book(BaseModel):
#    id: int
#    title: str
#    author: str
#    publisher: str
   
# @app.post("/book")
# def add_book(book: Book):
#    data.append(book.dict())
#    return data
# @app.get("/list")
# def get_books():
#    return data
# @app.get("/book/{id}")
# def get_book(id: int):
#    id = id - 1
#    return data[id]
# @app.put("/book/{id}")
# def add_book(id: int, book: Book):
#    data[id-1] = book
#    return data
# @app.delete("/book/{id}")
# def delete_book(id: int):
#    data.pop(id-1)
#    return data

#FastAPI - SQL Databases
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from pydantic import BaseModel
import uvicorn

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model
class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    author = Column(String(50))
    publisher = Column(String(50))

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Model
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str

    class Config:
        orm_mode = True

# FastAPI setup
app = FastAPI()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add a new book
@app.post('/add_new', response_model=Book)
def add_book(book: Book, db: Session = Depends(get_db)):
    bk = Books(id=book.id, title=book.title, author=book.author, publisher=book.publisher)
    db.add(bk)
    db.commit()
    db.refresh(bk)
    return bk

# List all books
@app.get('/list', response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    recs = db.query(Books).all()
    return recs

# Get a single book by id
@app.get('/book/{id}', response_model=Book)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Books).filter(Books.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update a book by id
@app.put('/update/{id}', response_model=Book)
def update_book(id: int, book: Book, db: Session = Depends(get_db)):
    b1 = db.query(Books).filter(Books.id == id).first()
    if not b1:
        raise HTTPException(status_code=404, detail="Book not found")
    b1.title = book.title
    b1.author = book.author
    b1.publisher = book.publisher
    db.commit()
    db.refresh(b1)
    return b1

# Delete a book by id
@app.delete('/delete/{id}')
def del_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Books).filter(Books.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"delete status": "success"}

# Main entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#run-- python main.py