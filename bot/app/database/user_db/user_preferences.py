from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from bot.app.database.base import Base


class User(Base):
    __tablename__ = 'user_preferences'

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))

    def __repr__(self):
        return f'user: {self.id}'
