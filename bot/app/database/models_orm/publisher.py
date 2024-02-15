from sqlalchemy.orm import Mapped, mapped_column

from bot.app.database.base import Base


class Publisher(Base):
    """
    Summary
        The Publisher class is a subclass of the Base class from the SQLAlchemy ORM module. It represents a database
        table named 'publisher' and defines two columns: 'id' and 'title'. It also overrides the __repr__ method to
        provide a string representation of the publisher's title.

    Main functionalities
        The main functionality of the Publisher class is to define a database table named 'publisher' and its columns.
        It inherits the functionality of the Base class, which includes creating and querying database tables.

    Methods
        __repr__(self): Overrides the __repr__ method to return a string representation of the publisher's title.

    Fields
        id: An integer column representing the primary key of the publisher.
        title: A string column representing the title of the publisher. It is required and cannot be null.
    """
    __tablename__ = 'publisher'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f'{self.title}'
