from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ch04.db_main import get_session
from ch04.models import Employee
from ch06.schemas import EmpCreate

ch6 = APIRouter(prefix='/ch6', tags=['员工管理的案例'])

@ch6.post(path='/emp')
def create_emp(emp: EmpCreate, session: Session = Depends(get_session)):
    db_emp = Employee(**emp.dict())
    session.add(db_emp)
    session.commit()
