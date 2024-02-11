import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

from models_orm import Authors, Category, Books, Publisher

load_dotenv('../.env')


def getenv(param: str) -> str:
    """
    Summary
        This code defines a function named getenv that takes a string parameter param and returns the value of the
        environment variable specified by param.

    Inputs
        param (string): The name of the environment variable to retrieve.

    Flow
        The getenv function is defined with a parameter param.
        Inside the function, the os.getenv function is called with the param parameter.
        The return value of os.getenv is converted to a string using the str function.
        The converted value is returned as the result of the getenv function.

    Outputs
        Returns the value of the environment variable specified by param as a string.
    """
    return str(os.getenv(param))


engine = create_engine(url=f'postgresql+psycopg://{getenv("USER")}:{getenv("PASSWORD")}@localhost:5432/Books_',
                       echo=True,
                       pool_size=5,
                       max_overflow=10
                       )

Session = sessionmaker(engine)


class Insert:
    """Summary
        The Insert class provides methods for inserting data into the database tables. It uses the SQLAlchemy ORM module
        to interact with the database.

    Main functionalities
        Inserting data into the authors, category, publisher, and books tables in the database.
        Checking if the data already exists in the respective tables before inserting.

    Methods
        insert_author(**kwargs): Inserts an author into the authors table. It takes keyword arguments for the author's
            attributes (id, firstname, lastname).
        insert_category(**kwargs): Inserts a category into the category table. It takes keyword arguments for the
            category's attributes (id, title).
        insert_publisher(**kwargs): Inserts a publisher into the publisher table. It takes keyword arguments for the
            publisher's attributes (id, title).
        insert_book(**kwargs): Inserts a book into the books table. It takes keyword arguments for the book's attributes
            (id, author, category, publisher, title, description, rating, votes).

    Fields
        session: An instance of the SQLAlchemy Session class used for database interactions.
    """

    def __init__(self):
        self.session = Session

    def insert_author(self, **kwargs):
        """
        Summary
            The insert_author method is a part of the Insert class and is used to insert an author into the authors
            table in the database. It checks if the author already exists in the table before inserting.

        Inputs
            **kwargs: A dictionary of keyword arguments representing the author's attributes (id, firstname, lastname).

        Flow
            Check if the author with the given ID already exists in the authors table.
            If the author exists, do nothing.
            If the author does not exist, create a new Authors object using the keyword arguments.
            Add the new author object to the session.
            Commit the changes to the database.

        Outputs
            None
        """
        with self.session() as info:
            if info.get(Authors, kwargs['id']):
                pass
            else:
                author = Authors(**kwargs)
                info.add(author)
                info.commit()

    def insert_category(self, **kwargs):
        """
        Summary
            The insert_category method is a part of the Insert class and is used to insert a category into the category
            table in the database. It checks if the category already exists in the table before inserting.

        Inputs
            **kwargs: A dictionary of keyword arguments representing the category's attributes (id, title).

        Flow
            Check if the category with the given ID already exists in the category table.
            If the category exists, do nothing.
            If the category does not exist, create a new Category object using the keyword arguments.
            Add the new category object to the session.
            Commit the changes to the database.

        Outputs
            None
        """
        with self.session() as info:
            if info.get(Category, kwargs['id']):
                pass
            else:
                category = Category(**kwargs)
                info.add(category)
                info.commit()

    def insert_publisher(self, **kwargs):
        """
        Summary
            The insert_publisher method is a part of the Insert class and is used to insert a publisher into the
            publisher table in the database. It checks if the publisher already exists in the table before inserting.

        Inputs
            **kwargs: A dictionary of keyword arguments representing the publisher's attributes (id, title).

        Flow
            Check if the publisher with the given ID already exists in the publisher table.
            If the publisher exists, do nothing.
            If the publisher does not exist, create a new Publisher object using the keyword arguments.
            Add the new publisher object to the session.
            Commit the changes to the database.

        Outputs
            None
        """
        with self.session() as info:
            if info.get(Publisher, kwargs['id']):
                pass
            else:
                publisher = Publisher(**kwargs)
                info.add(publisher)
                info.commit()

    def insert_book(self, **kwargs):
        """
        Summary
            The insert_book method is a part of the Insert class and is used to insert a book into the
            book table in the database. It checks if the book already exists in the table before inserting.

        Inputs
            **kwargs: A dictionary of keyword arguments representing the book's attributes.

        Flow
            Check if the book with the given ID already exists in the book table.
            If the book exists, do nothing.
            If the book does not exist, create a new Publisher object using the keyword arguments.
            Add the new book object to the session.
            Commit the changes to the database.

        Outputs
            None
        """
        with self.session() as info:
            if info.get(Books, kwargs['id']):
                pass
            else:
                book = Books(**kwargs)
                info.add(book)
                info.commit()
