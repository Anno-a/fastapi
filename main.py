from starlette.staticfiles import StaticFiles
from fastapi import FastAPI

from ch01.views import ch1
from ch02.views import ch2
from ch03.views import ch3
from function.shop.car import shop



# 127.0.0.1:8000/docs#/default
# uvicorn main:app --reload



app = FastAPI()
app.mount('/static', StaticFiles(directory='static'))

app.include_router(shop)
app.include_router(ch1)
app.include_router(ch2)
app.include_router(ch3)

@app.get('/')
async def root():
    return {'message': 'silly'}

@app.get('/hello/{name}', description='测试一下描述功能')
async def say_hello(name: str):
    return {'message': f'hello {name}'}

@app.post('/test')
def test():
    print('Silly-B')
    return {'msg': 'ok!'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

