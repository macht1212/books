from sqlalchemy.orm import mapped_column, Mapped

from models_orm.base import Base


class Category(Base):
    """
    Summary
        The Category class is a subclass of the Base class from the SQLAlchemy ORM module. It represents a database
        table named 'category' and defines two columns: 'id' and 'title'.

    Main functionalities
        The main functionality of the Category class is to define a database table named 'category' and provide a
        representation of a category object.

    Methods
        __repr__(self): Returns the title of the category object when it is printed.

    Fields
        id: Represents the primary key column of the 'category' table. It is of type int and is mapped to the 'id'
            column in the database.
        title: Represents the title column of the 'category' table. It is of type str and is mapped to the 'title'
            column in the database. It is required and cannot be null.
    """

    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return self.title



