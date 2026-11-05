from fastapi import APIRouter

shop = APIRouter(prefix='/shop', tags=['购物车功能'])

@shop.post('/car_all',summary='查询购物车')
def find_car():
    print('check car')
    return {'msg': 'gain the list of car'}

@shop.post('/car')
def create_car():
    print('create a car')
    return {'msg': 'create a new car'}

@shop.get('/fule')
def silly():
    return {'msg': '哎我真服了'}