import pytest
from app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    expected_text = 'GFGGGGGG'
    assert expected_text.encode() in response.data

def test_test(client):
    response=client.get('/test')
    assert response.status_code == 200
    expected_text = 'test'
    assert expected_text.encode() in response.data
