from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from ch01.views import ch1, ch2, ch3
app2 = FastAPI()
app2.mount('/static', StaticFiles(directory='../static'))

app2.include_router(ch1)
app2.include_router(ch2)
app2.include_router(ch3)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app2)
