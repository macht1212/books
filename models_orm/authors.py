from sqlalchemy.orm import Mapped, mapped_column

from models_orm.base import Base


class Authors(Base):

    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(default='ND')
    lastname: Mapped[str] = mapped_column(default='ND')

    def __repr__(self):
        return f'{self.id}, First name: {self.firstname}, Last name: {self.lastname}'



