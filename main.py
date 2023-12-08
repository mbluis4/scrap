from fastapi.responses import FileResponse
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


@app.get('/gen_excel')
def get_price():
    try:
        # Save DataFrame to Excel file
        excel_file_path = getPrices()

        # Return the Excel file as a response
        return FileResponse(excel_file_path, filename='output.xlsx', media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    except Exception as e:
        # Handle exceptions, if any
        raise HTTPException(status_code=500, detail=str(e))
