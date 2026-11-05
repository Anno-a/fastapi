from typing import List

from fastapi import APIRouter
from pydantic import Field, BaseModel

ch3 = APIRouter(prefix='/ch3', tags=['请求体传参'])

class Address(BaseModel):
    country: str = Field('China')
    city: str = Field('shanghai')

class Message(BaseModel):
    name: str = Field(description='开盒姓名')
    address: Address
    size: List[int] = Field(description='三维')

@ch3.post('/emp', summary='开盒')
def check_gay(emp: Message):
    print(emp)
    return {'msg': 'ojbk'}
