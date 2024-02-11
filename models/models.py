from pydantic import BaseModel


class AuthorModel(BaseModel):
    id: int
    firstname: str
    lastname: str


class CategoryModel(BaseModel):
    id: int
    title: str


class PublisherModel(BaseModel):
    id: int
    title: str


class BookModel(BaseModel):
    id: int
    author: int
    category: int = 0
    publisher: int = 0
    title: str
    description: str
    rating: float = .0
    votes: int = 0
