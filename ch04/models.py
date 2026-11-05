import enum
from datetime import date
from decimal import Decimal
from typing import Optional

from sqlalchemy import String, DECIMAL, Boolean, select, delete, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, relationship
from ch04.db_main import Base, engine



class SexValue(enum.Enum):
    MALE = '男'
    FEMALE = '女'

class Employee(Base):

    __tablename__ = 't_emp'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    sal: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=True, comment='员工工资')
    bonus: Mapped[int] = mapped_column(default=0, comment='员工津贴')
    is_leave: Mapped[bool] = mapped_column(Boolean, default=False)
    skill: Mapped[int]
    is_silly: Mapped[bool] = mapped_column(Boolean, default=False)
    dept_id: Mapped[int] = mapped_column(ForeignKey('t_dept.id'))
    dept: Mapped[Optional['Dept']] = relationship(back_populates='emp_list')


    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}')"

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
'''
alembic revision --autogenerate -m 'init'
alembic upgrade head
'''

if __name__ == '__main__':
    with sessionmaker(engine).begin() as session:
        # emp1 = Employee(name='zs', sal=2000, bonus=300, gender=SexValue.MALE)
        # emp2 = Employee(name='ls', sal=8000, bonus=250, gender=SexValue.MALE)
        # emp3 = Employee(name='ww', sal=9000, bonus=3000, gender=SexValue.FEMALE)
        # emp4 = Employee(name='jb', sal=1000, bonus=15, gender=SexValue.MALE)
        # session.add_all([emp2, emp3, emp4])

        # 拿取单个,session.get只接受主键查询-为轻量级查询 <--> select & execute
        emp = session.get(Employee, 1)

        '''拿取多个'''
        stmt = select(Employee)
        list_emp = session.scalars(stmt).all()
        # for e in list_emp:
        #     print(e)

        sst = select(Employee.name, Employee.sal)
        list_sst = session.execute(sst).all()
        # for o in list_sst:
        #     print(o.name, o.sal)

        # 修改与删除
        rev1 = session.get(Employee, 1)
        # rev1.name = 'silly-b'
        # 1
        emp1 = session.get(Employee, 1)
        # session.delete(emp1)
        # 2
        emp2 = delete(Employee).where(Employee.id == 6)
        session.execute(stmt)

        stmt1 = select(Employee).where(Employee.id == 2)
        result1 = session.execute(stmt1).scalars()
        # for o in result1:
        #     print(o)

        ## 高级检索
        stmt2 = select(Employee).where(Employee.id >= 3, Employee.sal > 7000)
        result2 = session.execute(stmt2).scalars()
        # for o in result2:
        #     print(o)

        # 聚合函数
        stmt3 = select(func.avg(Employee.sal))
        result3 = session.execute(stmt3).scalars().first()
        # print(result3)

        # 排序、分页、限制
        result4 = session.execute(select(Employee).order_by(Employee.sal).offset(1).limit(2)).scalars()
        # for o in result4:
        #     print(o)

        # 多输出
        stmt5 = select(Employee.gender, func.count(Employee.id)).group_by(Employee.gender)
        result5 = session.execute(stmt5).all()
        # for o1, o2 in result5:
        #     print(o1.)

        stmt6 = select(Employee.name)
        result6 = session.execute(stmt6).scalars().all()
        # for i in result6:
        print(result6)
