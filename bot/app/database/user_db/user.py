from sqlalchemy.orm import Mapped, mapped_column

from bot.app.database.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return f'user: {self.id}'
