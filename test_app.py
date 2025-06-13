from app import add,app
import pytest


def test_add_positive_numbers():
    assert add(2,3) == 5

def test_add_zero():
    assert add(0,0) == 0

def test_add_negative_numbers():
    assert add(-1,-2) == -3

    
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_root_endpoint(client):
    response = client.get('/janusz')
    assert response.status_code == 200
    assert b"Hello, Janusz!" in response.data