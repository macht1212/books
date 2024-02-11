from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Summary
        The Base class is a subclass of DeclarativeBase from the SQLAlchemy ORM module. It serves as a base class for
        defining database models in SQLAlchemy.

    Main functionalities
        The main functionality of the Base class is to provide a base class for defining database models in SQLAlchemy.
        It inherits from the DeclarativeBase class, which provides the necessary functionality for creating and
        interacting with database tables.

    Methods
        The Base class does not define any additional methods. It inherits all the methods from the DeclarativeBase
        class, which include methods for creating and querying database tables.

    Fields
        The Base class does not define any additional fields. It inherits all the fields from the DeclarativeBase class,
        which include fields for defining database columns and relationships.
    """
    pass
