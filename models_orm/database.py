import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

from models_orm import Authors, Category, Books, Publisher

load_dotenv('../.env')

metadata = MetaData()


def getenv(param: str) -> str:
    return str(os.getenv(param))


engine = create_engine(
    url=f'postgresql+psycopg://{getenv("USER")}:{getenv("PASSWORD")}@localhost:5432/Books_',
    echo=True,
    pool_size=5,
    max_overflow=10
)

Session = sessionmaker(bind=engine)


class Actions:

    # @staticmethod
    @staticmethod
    def _session(data):
        with Session() as session:
            session.add(data)
            session.commit()


class Insert(Actions):

    def __init__(self, **kw):
        super().__init__(**kw)

    def insert_author(self, **kwargs):
        author = Authors(**kwargs)
        self._session(author)

    def insert_category(self, **kwargs):
        category = Category(**kwargs)
        self._session(category)

    def insert_publisher(self, **kwargs):
        publisher = Publisher(**kwargs)
        self._session(publisher)

    def insert_book(self, **kwargs):
        book = Books(**kwargs)
        self._session(book)



