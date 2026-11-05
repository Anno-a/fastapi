from datetime import datetime
from sqlalchemy import create_engine, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine(r'sqlite:///test.db', echo=False, future=True)

class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), comment='创建时间')
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), onupdate=func.now(), comment='更新时间')

def get_session():
    session = Session(bind=engine)
    try:
        yield session
    finally:
        session.close()
