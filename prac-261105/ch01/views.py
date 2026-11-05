from enum import Enum
from typing import List

from fastapi import APIRouter, Path, Query
from pydantic import BaseModel, Field, field_validator

ch1 = APIRouter(prefix='/ch1', tags=['路由1'])
ch2 = APIRouter(prefix='/ch2', tags=['URL传参'])
ch3 = APIRouter(prefix='/ch3', tags=['Body传参'])

class emp_name(Enum):
    zs = "张三"
    ls = "李四"
    ww = "王五"

class Address(BaseModel):
    country: str = Field(default='中国')
    city: str = Field(default='上海')

class Emp(BaseModel):
    id: int
    name: str
    is_silly: bool = Field(default=True)
    address: Address

    @field_validator('id')
    def check_id(cls, value):
        assert value <= 10
        return value


@ch1.get('/add', summary='summary', description='description')
def add_car():
    return {'msg': '已添加！'}

@ch1.get('/check/{id}', summary='装饰器-summary', description='装饰器-description')
def check_id(id: int = Path(description='Path-description')):
    return {'msg': f'第{id}个员工是silly-b'}

@ch1.get('/name/{name}', summary='姓名查找')
def check_name(name: emp_name):
    return {'msg': f'可以找到，{name.value}是silly-b'}

@ch2.get('/check', summary='url传参查询多人')
def check_many(emp_ids: List[int] = Query(default=[], description='所有人的id')):
    for i in emp_ids:
        print(f'找到编号为{i}的人了')
    return {'msg': 'ojbk'}

@ch3.post('/add', summary='body添加多个信息')
def add_info(emp:Emp):
    print(emp)
    return emp