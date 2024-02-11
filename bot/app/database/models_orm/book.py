from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from bot.app.database.models_orm.base import Base


class Books(Base):
    """
    Summary
        The Books class is a subclass of the Base class from the SQLAlchemy ORM module. It represents a database table
        for storing information about books.

    Main functionalities
        The main functionality of the Books class is to define the structure and behavior of the books table in the
        database. It inherits the functionality from the Base class, which includes creating and querying the table.

    Methods
        The Books class does not define any additional methods. It inherits all the methods from the Base class, which
        include methods for creating and querying the books table.

    Fields
        id: An integer field that serves as the primary key for the books table.
        author: A string field that represents the foreign key to the authors table. It is required and has a default
            value of 0.
        category: An integer field that represents the foreign key to the category table. It has a default value of 0.
        publisher: An integer field that represents the foreign key to the publisher table. It has a default value of 0.
        title: A string field that represents the title of the book. It is required.
        description: A string field that represents the description of the book. It has a default value of 'No text'.
        rating: A float field that represents the rating of the book. It has a default value of 0.0.
        votes: An integer field that represents the number of votes for the book. It has a default value of 0.
    """
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(ForeignKey('authors.id', ondelete="CASCADE"), nullable=False, default=0)
    category: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete="CASCADE"), default=0)
    publisher: Mapped[int] = mapped_column(ForeignKey('publisher.id', ondelete='CASCADE'), default=0)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(default='No text')
    rating: Mapped[float] = mapped_column(default=0.0)
    votes: Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return f'Title: {self.title}, description: {self.description}'
