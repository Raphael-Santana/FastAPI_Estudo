from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_funcao_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # assert (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello World'}
