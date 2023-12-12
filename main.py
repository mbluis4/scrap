from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from getPricesSp import getPrices


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def hello_w():
    return {
        'body': 'hola',
    }


@app.get('/precios')
def precios():
    getPrices()
    return {
        'body': 'enviado'
    }


@app.get('/gen_excel')
def get_price():
    try:

        getPrices()

        return {
            'body': 'your excel file is being generated and will be sent to your email'
        }

    except Exception as e:
        # Handle exceptions, if any
        raise HTTPException(status_code=500, detail=str(e))
