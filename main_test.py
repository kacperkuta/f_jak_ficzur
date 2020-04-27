import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}

@pytest.mark.parametrize("name", ["Ala", "Zażółć", "Brzęczyszczykiewicz"])
def test_hello_name(name):
    response = client.get(f'/hello/{name}')
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}

def test_get_method():
    response = client.get('/method')
    assert response.status_code == 200
    assert response.json() == {"method":"GET"}

def test_post_method():
    response = client.post('/method')
    assert response.status_code == 200
    assert response.json() == {"method":"POST"}

def test_put_method():
    response = client.put('/method')
    assert response.status_code == 200
    assert response.json() == {"method":"PUT"}

def test_delete_method():
    response = client.delete('/method')
    assert response.status_code == 200
    assert response.json() == {"method":"DELETE"}

def test_post_patient():
    response = client.post('/patient', json={"name":"Marta", "surename":"Markocka"})
    assert response.status_code == 200
    assert response.json() == {"id":0, "patient":{"name":"Marta", "surename":"Markocka"}}

    response = client.post('/patient', json={"name":"Tomasz", "surename":"Aaaa"})
    assert response.status_code == 200
    assert response.json() == {"id":1, "patient":{"name":"Tomasz", "surename":"Aaaa"}}

    response = client.post('/patient', json={"name":"Kuba", "surename":"Byrdy"})
    assert response.status_code == 200
    assert response.json() == {"id":2, "patient":{"name":"Kuba", "surename":"Byrdy"}}

    response = client.get(f'/patient/{0}')
    assert response.status_code == 200
    assert response.json() == {"name":"Marta", "surename":"Markocka"}

    response = client.get(f'/patient/{1}')
    assert response.status_code == 200
    assert response.json() == {"name":"Tomasz", "surename":"Aaaa"}

    response = client.get(f'/patient/{2}')
    assert response.status_code == 200
    assert response.json() == {"name":"Kuba", "surename":"Byrdy"}

    response = client.get(f'/patient/{3}')

    assert response.status_code == 204

def test_get_welcome():
    response = client.get('/welcome')
    assert response.status_code == 200
    assert response == "testy"