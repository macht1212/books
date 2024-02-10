from sqlalchemy.orm import relationship, Mapped, mapped_column

from models_orm.base import Base


class Publisher(Base):
    __tablename__ = 'publisher'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    # book = relationship('books')

    def __repr__(self):
        return self.title
