from fastapi import APIRouter, Query
from pydantic import field_validator

ch2 = APIRouter(prefix='/ch2', tags=['URL传参'])

@ch2.get('/emp', summary='员工查询')
def check(emp_id: int = Query(None, description='员工身份'),
          name: str = Query('Silly', description='员工姓名'),
          tele: int = Query(114, description='员工电话', regex=r'1[3-9]\d{9}'),
          age: int =Query(description='员工年龄', ge=18, le=60)):
    print(f'查询成功silly员工{emp_id}')
    print(f'ta是{name}')
    print(f'打爆{tele}这个电话,他{age}岁')

    @field_validator('age')
    def check_age(cls, v):
        if v < 18:
            raise ValueError('电')
        elif v > 60:
            raise ValueError('solider boy')
        else:
            return v

    return {'msg': "Don't be silly"}
