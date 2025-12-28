from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI(
    title="Library Management API",
    description="API для управления библиотекой книг с использованием FastAPI и OpenAPI",
    version="1.0.0"
)

# Модель данных книги
class Book(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    title: str = Field(..., example="Мастер и Маргарита")
    author: str = Field(..., example="Михаил Булгаков")
    year: int = Field(..., gt=0, example=1967)
    is_available: bool = True

# Имитация базы данных в оперативной памяти
db: List[Book] = []

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Добро пожаловать в Library API! Перейдите на /docs для работы с Swagger UI."}

@app.get("/books", response_model=List[Book], tags=["Books"])
def get_books():
    """Получить список всех книг"""
    return db

@app.get("/books/{book_id}", response_model=Book, tags=["Books"])
def get_book(book_id: UUID):
    """Получить информацию о книге по ID"""
    for book in db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@app.post("/books", response_model=Book, status_code=201, tags=["Books"])
def create_book(book: Book):
    """Добавить новую книгу"""
    book.id = uuid4()
    db.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book, tags=["Books"])
def update_book(book_id: UUID, updated_book: Book):
    """Обновить данные существующей книги"""
    for index, book in enumerate(db):
        if book.id == book_id:
            updated_book.id = book_id
            db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@app.delete("/books/{book_id}", tags=["Books"])
def delete_book(book_id: UUID):
    """Удалить книгу из библиотеки"""
    for index, book in enumerate(db):
        if book.id == book_id:
            db.pop(index)
            return {"message": "Книга успешно удалена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")