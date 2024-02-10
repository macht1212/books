from sqlalchemy.orm import relationship, mapped_column, Mapped

from models_orm.base import Base


class Category(Base):

    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    # book = relationship('books')

    def __repr__(self):
        return self.title



