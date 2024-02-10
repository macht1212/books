from pydantic import BaseModel


class Author(BaseModel):
    id: int
    firstname: str
    lastname: str


class Category(BaseModel):
    id: int
    title: str


class Publisher(BaseModel):
    id: int
    title: str


class Book(BaseModel):
    id: int
    author1: int
    author2: int = 0
    author3: int = 0
    category: int = 0
    publisher: int = 0
    title: str
    description: str
    rating: float = .0
