from typing import List

from sqlalchemy import String
from ch04.db_main import Base,engine
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker



class Dept(Base):
    __tablename__ = 't_dept'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), name='dname',)
    country: Mapped[str] = mapped_column(String(40))

    emp_list: Mapped[List['Employee']] = relationship(back_populates='dept')


if __name__ == '__main__':
    with sessionmaker(engine).begin() as session:
        pass