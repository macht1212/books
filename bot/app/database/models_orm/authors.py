from sqlalchemy.orm import Mapped, mapped_column

from bot.app.database.base import Base


class Authors(Base):
    """
    Summary
        The Authors class is a subclass of the Base class from the SQLAlchemy ORM library. It represents a table named
        'authors' in a database and defines three columns: 'id', 'firstname', and 'lastname'. The class also provides a
        string representation of an author object.

    Main functionalities
        Represents a table named 'authors' in a database
        Defines three columns: 'id', 'firstname', and 'lastname'
        Provides a string representation of an author object

    Methods
        __repr__(): Returns a string representation of an author object. It includes the author's ID, first name, and
        last name.

    Fields
        id: An integer column representing the author's ID. It is a primary key column.
        firstname: A string column representing the author's first name. It has a default value of 'ND' (Not Defined).
        lastname: A string column representing the author's last name. It has a default value of 'ND' (Not Defined).
    """

    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(default='ND')
    lastname: Mapped[str] = mapped_column(default='ND')

    def __repr__(self):
        return f'{self.id}, First name: {self.firstname}, Last name: {self.lastname}'



