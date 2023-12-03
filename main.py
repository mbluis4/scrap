from fastapi.responses import FileResponse
from fastapi import FastAPI
from getPricesSp import getPrices

app = FastAPI()


@app.get('/')
def hello_w():
    return {
        'message': 'hola'
    }


@app.get('/price')
def get_price():
    return FileResponse(getPrices())
