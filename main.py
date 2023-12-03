import io
import os.path
from fastapi.responses import Response
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

    buffer: io.BytesIO = None

    with open(getPrices(), "rb") as f:
        buffer = f.getvalue()

    headers = {
        # By adding this, browsers can download this file.
        'Content-Disposition': f'attachment; filename=test.xlsx',
        # Needed by our client readers, for CORS (cross origin resource sharing).
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control_Allow-Methods": "POST, GET, OPTIONS",
    }
    media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    return Response(
        content=buffer,
        headers=headers,
        media_type=media_type
    )
