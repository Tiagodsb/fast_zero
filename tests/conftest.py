from fastapi.testclient import TestClient
from fast_zero.app import app
from pytest import fixture


@fixture
def client():
    client  = TestClient(app)
    return client
