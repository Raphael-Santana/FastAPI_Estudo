from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/world', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def teste_html():
    return """
    <html>
        <head>
            <tittle>Primeiro Olá Mundo!</tittle>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>"""


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user
