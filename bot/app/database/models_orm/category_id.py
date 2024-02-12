from sqlalchemy.orm import Mapped, mapped_column

from bot.app.database.models_orm.base import Base


class CategoryID(Base):

    __tablename__ = 'categoryid'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

    def __repr__(self):
        return self.title
