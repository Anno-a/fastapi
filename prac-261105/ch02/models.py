from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker

from db_main import engine, Base

class Emp(Base):
    __tablename__ = 't_emp'

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)

if __name__ == "__main__":
    with sessionmaker(engine).begin() as session:
        emp1 = Emp(name='zs')
        session.add(emp1)