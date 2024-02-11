from sqlalchemy.orm import Mapped, mapped_column

from models_orm.base import Base


class Publisher(Base):
    __tablename__ = 'publisher'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f'{self.title}'
