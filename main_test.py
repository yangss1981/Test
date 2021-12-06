from fastapi.testclient import TestClient

from main import *

def test_read_main():
    response = read_main()
    assert response == {"msg": "Hello World"}