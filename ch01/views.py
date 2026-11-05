from ast import List
from enum import Enum
from fastapi import APIRouter, Path

ch1 = APIRouter(prefix='/ch1', tags=['路由传参'])

@ch1.get('/emp/{emp_id}')
def find_emp(emp_id: int, summary='查询单个员工'):
    print(f'传入参数为：{emp_id}')
    return {'msg': 'ok'}

class EmpName(Enum):
    zs = '张三'
    ls = '李四'
    ww = '王五'

@ch1.delete('/emp/{emp_name}',description='sillllllllllly!')
def delete_name(emp_name: EmpName):
    print(f'传入参数为：{emp_name.name}')
    print(f'传入参数为：{emp_name.value}')
    print('删除单个员工')
    return {'msg': 'okk!'}

@ch1.put('/emp/{emp_name}')
def delete_name(emp_name: EmpName = Path(description='选择员工名字')):
    print(f'传入参数为：{emp_name.name}')
    print(f'传入参数为：{emp_name.value}')
    print('修改单个员工')
    return {'msg': 'okk!'}