import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

from models_orm import Authors, Category, Books, Publisher

load_dotenv('../.env')


def getenv(param: str) -> str:
    return str(os.getenv(param))


def create_engine_(user: str, password: str, echo: object = False, pool_size: object = 5,
                   max_overflow: object = 10) -> object:
    return create_engine(
        url=f'postgresql+psycopg://{user}:{password}@localhost:5432/Books_',
        echo=echo,
        pool_size=pool_size,
        max_overflow=max_overflow
    )


engine = create_engine(url=f'postgresql+psycopg://{getenv("USER")}:{getenv("PASSWORD")}@localhost:5432/Books_',
                       echo=True,
                       pool_size=5,
                       max_overflow=10
                       )

Session = sessionmaker(engine)


class Insert:

    def __init__(self):
        self.session = Session

    def insert_author(self, **kwargs):
        with self.session() as info:
            if info.get(Authors, kwargs['id']):
                pass
            else:
                author = Authors(**kwargs)
                info.add(author)
                info.commit()

    def insert_category(self, **kwargs):
        with self.session() as info:
            if info.get(Category, kwargs['id']):
                pass
            else:
                category = Category(**kwargs)
                info.add(category)
                info.commit()

    def insert_publisher(self, **kwargs):
        with self.session() as info:
            if info.get(Publisher, kwargs['id']):
                pass
            else:
                publisher = Publisher(**kwargs)
                info.add(publisher)
                info.commit()

    def insert_book(self, **kwargs):
        with self.session() as info:
            if info.get(Books, kwargs['id']):
                pass
            else:
                book = Books(**kwargs)
                info.add(book)
                info.commit()
